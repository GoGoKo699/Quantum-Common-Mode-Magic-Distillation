# Exact extraction criterion

## Theorem

For the [delivered-state model](model.md), exact $`T`$-state extraction with nonzero heralded probability is possible if and only if there exist bit strings $`x,y`$ with

```math
q(x)=q(y),\qquad \lvert x\rvert-\lvert y\rvert\equiv 1 \pmod 2 .
```

One such pair gives a stabilizer circuit with success probability $`2^{1-n}`$ uniformly in the unknown parameter.

## Constructing a successful branch

Write $`d=x\oplus y`$. Measure the $`Z`$-type Pauli checks whose binary support vectors form a basis of the subspace orthogonal to $`d`$ over the two-element field. Postselect the syndrome of $`x`$. The accepted computational-basis strings are exactly $`x`$ and $`y`$. This measurement retains their coherence. Each has squared amplitude $`2^{-n}`$, and their ratio after projection is $`\zeta^{\lvert y\rvert-\lvert x\rvert}`$ because their charges are equal.

To decode the pair, translate by bit flips on the support of $`x`$, choose any pivot where $`d`$ is one, and apply controlled bit flips from that pivot to the other positions in the support of $`d`$. The two strings become the all-zero string and the string with one at the pivot only. Their relative phase is an odd eighth root of unity, so a power of $`S=\mathrm{diag}(1,i)`$ on the pivot sets it to $`\zeta`$. The remaining qubits can be discarded. Equal positions of the original pair may also be discarded at the outset. If the circuit uses only the positions on which the pair differs, its success probability is $`2^{1-\lvert d\rvert}`$.

## Converse for adaptive circuits

Refine every success branch into Kraus operators $`K`$ from the input block to the one-qubit output. This can be done by retaining the classical history and refining discarded quantum systems by computational-basis measurement in the Kraus representation. A fine stabilizer Kraus operator is a matrix over $`\mathbb Q(i)`$ after multiplication by a common nonzero scalar. To see this, use Hadamard, $`S`$ and CNOT to implement the Clifford gates, introduce clean stabilizer ancillas by Clifford preparation, and conjugate each Pauli measurement to computational-basis form. Hadamard contributes a common factor of $`1/\sqrt{2}`$, while the other matrix entries and computational-basis contractions are Gaussian rational. A classical probability weight contributes only another common scalar.

For every $`\theta`$, each accepted branch sends $`\lvert\Psi(\theta)\rangle`$ into the span of $`\lvert T\rangle`$. Indeed, the accepted density matrix is a sum of positive branch contributions and has rank one if the success probability is positive. If it vanishes then every contribution vanishes. With $`\lvert T_\perp\rangle=Z\lvert T\rangle`$, this gives

```math
0=\langle T_\perp\rvert K\lvert\Psi(\theta)\rangle
=\sum_q e^{i q\cdot\theta}\langle T_\perp\rvert K v_q .
```

Choose a line through the open parameter region with direction separating the finitely many distinct charges under projection. Its restriction to a short interval is a sum of exponentials of distinct frequencies. Differentiating up to one fewer than the number of frequencies gives an invertible Vandermonde system. Thus each $`K v_q`$ separately lies in the span of $`\lvert T\rangle`$.

If all strings of a sector share one weight parity, $`v_q`$ is a common scalar times a vector over $`\mathbb Q(i)`$. Indeed, ratios of powers of $`\zeta`$ with the same parity are powers of $`i`$. The same holds for $`K v_q`$ as a vector. A nonzero vector proportional to $`\lvert T\rangle`$ has component ratio $`\zeta=(1+i)/\sqrt{2}`$, outside $`\mathbb Q(i)`$. Thus every success branch annihilates every sector with homogeneous weight parity. A block having only such sectors has zero success. This is the same number-field restriction used in [prior work on non-Clifford resources](../references/RELATED_WORK.md#exact-conversion-and-number-fields), applied here to each drift charge separately.

## Repeatable integer sensitivities

Suppose a source offers any finite number of states of each gain in a fixed positive integer alphabet. Finite extraction is possible exactly when two alphabet gains have different exponents of two in their factorizations.

If all gains have the same exponent, divide them by the shared power of two. All reduced gains are odd. Each charge then determines the bit-string parity, which rules out extraction by the theorem. If gains $`g,h`$ have different exponents and $`b=\gcd(g,h)`$, choose $`h/b`$ copies of gain $`g`$ and $`g/b`$ copies of gain $`h`$. The two strings selecting one gain type each have the same charge. One copy count is even and the other is odd, so the pair gives exact extraction. With only these two gain types, $`(g+h)/b`$ is the minimum number of inputs over all allocations. Any charge equality between opposite-parity strings requires a nonzero signed change in the selected counts. This change is an integer multiple of $`(h/b,-g/b)`$ and hence differs on at least $`(g+h)/b`$ bits.
