# Reproduce the finite checks

From the repository root, run the script with Python 3.9 or later.

```sh
python3 verification/check.py
```

The script uses the Python standard library. It enumerates computational-basis strings, groups them by their exact integer charges, and uses rational arithmetic for probabilities. It checks the affine-line decoder and the three-qubit circuit, including the accepted syndrome, the decoded phase, and the optimal yield in the scalar and two-mode examples. The two-mode twirl is evaluated symbolically in powers of the eighth root of unity. Tracing out any qubit gives the maximally mixed state on the remaining two qubits.

A finite scan of complex amplitudes checks the accepted fidelity and probability when the additive phase relation is perturbed. Exact counting also checks the field bound and the yield of independent repetitions for up to four triplets. See the [scientific account](../science/README.md) for the general proofs.

For five independently drifting source bundles, the same script enumerates the product charge sectors. It checks the number of binary parity labels in each sector and verifies that complementing a burst history multiplies its character by the total parity sign. The [burst converse](../science/burst-converse.md) establishes the general impossibility claims.
