#!/usr/bin/env python3
"""Reproduce finite circuit and charge-sector checks with the standard library."""

from collections import Counter, defaultdict
from cmath import exp
from fractions import Fraction
from itertools import combinations, product
from math import isclose, pi, prod, sin


SCALAR_GAINS = ((1,), (1,), (2,))
VECTOR_GAINS = ((1, 0), (0, 1), (1, 1))
PAIR = ((0, 0, 1), (1, 1, 0))
ZETA = exp(1j * pi / 4)


def bit_strings(width):
    return product((0, 1), repeat=width)


def charge(gains, bits):
    return tuple(
        sum(bit * gain for bit, gain in zip(bits, component))
        for component in zip(*gains)
    )


def charge_sectors(gains):
    sectors = defaultdict(list)
    for bits in bit_strings(len(gains)):
        sectors[charge(gains, bits)].append(bits)
    return sectors


def parity_count(strings):
    even = sum(sum(bits) % 2 == 0 for bits in strings)
    return even, len(strings) - even


def mixed_sectors(sectors):
    return [tuple(strings) for strings in sectors.values() if all(parity_count(strings))]


def field_bound(sectors):
    """Sum the squared sector residuals after projecting out conjugate vectors."""
    size = sum(len(strings) for strings in sectors.values())
    bound = Fraction(0)
    for strings in sectors.values():
        even, odd = parity_count(strings)
        mass = Fraction(even + odd, size)
        overlap = Fraction(even - odd, size)
        residual = mass - overlap**2 / mass
        assert residual == Fraction(4 * even * odd, size * (even + odd))
        bound += residual
    return bound


def triple_decode(bits):
    a, b, c = bits
    return a, a ^ b, a ^ c


def affine_line_decode(bits, first, second):
    """Apply the basis permutation for a selected affine line."""
    difference = tuple(x ^ y for x, y in zip(first, second))
    pivot = difference.index(1)
    shifted = tuple(bit ^ x for bit, x in zip(bits, first))
    logical = shifted[pivot]
    helpers = tuple(
        bit ^ (logical & difference[j])
        for j, bit in enumerate(shifted)
        if j != pivot
    )
    return logical, helpers


def check_affine_line(gains):
    for sector in charge_sectors(gains).values():
        for first, second in combinations(sector, 2):
            difference = sum(second) - sum(first)
            if difference % 2 == 0:
                continue
            accepted = {}
            for bits in bit_strings(len(gains)):
                logical, helpers = affine_line_decode(bits, first, second)
                if not any(helpers):
                    accepted[logical] = bits
            assert accepted == {0: first, 1: second}
            s_power = ((1 - difference) // 2) % 4
            assert (difference + 2 * s_power) % 8 == 1


def check_minimal_triples():
    for gains in (SCALAR_GAINS, VECTOR_GAINS):
        sectors = charge_sectors(gains)
        assert mixed_sectors(sectors) == [PAIR]
        assert field_bound(sectors) == Fraction(1, 4)
        check_affine_line(gains)

    accepted = {
        bits: triple_decode(bits)[0]
        for bits in bit_strings(3)
        if triple_decode(bits)[1:] == (0, 1)
    }
    assert accepted == {PAIR[0]: 0, PAIR[1]: 1}
    assert sum(PAIR[1]) - sum(PAIR[0]) == 1
    assert Fraction(len(accepted), 2**3) == Fraction(1, 4)

    # Include negative gains and a pair whose relative phase needs a correction.
    check_affine_line(((1,), (2,), (-3,)))
    assert mixed_sectors(charge_sectors(((0,),))) == [((0,), (1,))]

    nonzero_gains = tuple(vector for vector in product((-1, 0, 1), repeat=2) if any(vector))
    for width in (1, 2, 3):
        for gains in product(nonzero_gains, repeat=width):
            sectors = charge_sectors(gains)
            mixed = mixed_sectors(sectors)
            if width < 3:
                assert not mixed
                continue
            signed_relations = sum(
                all(sum(sign * value for sign, value in zip(signs, component)) == 0
                    for component in zip(*gains))
                for signs in product((-1, 1), repeat=3)
            )
            assert signed_relations in (0, 2)
            assert len(mixed) == signed_relations // 2
            assert field_bound(sectors) == Fraction(signed_relations, 8)


def check_twirl():
    # For integer gains and uniform phases, only terms with equal charge survive.
    # Store each surviving matrix entry as its exponent of ζ, in units of 1/8.
    entries = {
        (left, right): (sum(left) - sum(right)) % 8
        for strings in charge_sectors(VECTOR_GAINS).values()
        for left in strings
        for right in strings
    }
    expected = {(bits, bits): 0 for bits in bit_strings(3)}
    expected[(PAIR[1], PAIR[0])] = 1
    expected[(PAIR[0], PAIR[1])] = 7
    assert entries == expected

    for discarded in range(3):
        marginal = defaultdict(Counter)
        for (left, right), exponent in entries.items():
            if left[discarded] == right[discarded]:
                ket = left[:discarded] + left[discarded + 1:]
                bra = right[:discarded] + right[discarded + 1:]
                marginal[(ket, bra)][exponent] += 1
        expected_marginal = {(bits, bits): Counter({0: 2}) for bits in bit_strings(2)}
        assert marginal == expected_marginal


def check_mismatch():
    # Use direct complex amplitudes for the conditional state and report the
    # exact formula they check over these sample input phases.
    for step in range(1, 25):
        phases = (step / 7, -step / 11, step / 7 - step / 11)
        for extras in ((0, 0, 0), (0.01, -0.03, 0.04), (0.2, 0.3, 0.5), (0, 0, pi)):
            raw_angles = [pi / 4 + phase + extra for phase, extra in zip(phases, extras)]
            states = [(2**-0.5, exp(1j * angle) * 2**-0.5) for angle in raw_angles]
            kept = {}
            for bits in bit_strings(3):
                logical, helper_one, helper_two = triple_decode(bits)
                if (helper_one, helper_two) == (0, 1):
                    kept[logical] = prod(state[bit] for state, bit in zip(states, bits))
            probability = sum(abs(amplitude)**2 for amplitude in kept.values())
            fidelity = abs((kept[0] + ZETA.conjugate() * kept[1]) * 2**-0.5)**2 / probability
            mismatch = extras[0] + extras[1] - extras[2]
            assert isclose(probability, 0.25, abs_tol=1e-12)
            assert isclose(1 - fidelity, sin(mismatch / 2)**2, abs_tol=1e-12)


def check_repetitions():
    for copies in range(1, 5):
        gains = []
        for k in range(copies):
            for gain in VECTOR_GAINS:
                gains.append((0,) * (2 * k) + gain + (0,) * (2 * (copies - k - 1)))
        accepted = sum(
            any(triple_decode(bits[start:start + 3])[1:] == (0, 1)
                for start in range(0, len(gains), 3))
            for bits in bit_strings(len(gains))
        )
        success = Fraction(accepted, 2**len(gains))
        assert success == 1 - Fraction(3, 4)**copies
        assert field_bound(charge_sectors(gains)) == success


def main():
    checks = (
        ("Affine-line decoder, small nonzero gains, and sharp triples", check_minimal_triples),
        ("Two-mode twirl and all two-qubit reductions", check_twirl),
        ("Yield and fidelity under phase mismatch", check_mismatch),
        ("Tight yield for independently drifting triplets", check_repetitions),
    )
    for label, check in checks:
        check()
        print(f"PASS {label}")


if __name__ == "__main__":
    main()
