# Three-input protocol

## Preparation and receiver

Let the source deliver three equatorial states with phase errors $`\phi_1,\phi_2,\phi_1+\phi_2`$. This is the two-mode instance

```math
a_1=(1,0),\qquad a_2=(0,1),\qquad a_3=(1,1)
```

of the [source model](model.md). The one-mode gain list $`(1,1,2)`$ gives the same cancellation. In both instances, bit strings $`001`$ and $`110`$ have the same unknown phase. Their nominal weights are one and two, respectively.

The receiver measures $`Z_1Z_2`$ and $`Z_1Z_3`$ and accepts $`(+1,-1)`$. The accepted pair is $`\{001,110\}`$. Applying CNOT from qubit one to qubits two and three maps the pair to $`\{001,101\}`$. Qubits two and three are left in $`\lvert 01\rangle`$, and the relative phase on the first qubit is exactly $`e^{i\pi/4}`$.

The receiver can fuse the parity checks and the decoder. Apply the two CNOTs, measure qubits two and three in the computational basis, then retain qubit one when the two measured bits are $`01`$. The two amplitudes each have probability $`1/8`$, so the success probability is $`1/4`$ at every input phase.

## Three inputs are minimal and the yield is sharp

A pair of opposite weight parity differs in an odd number of positions. Equality of charge for strings differing at one position would require zero sensitivity on that position. Thus, if every sensitivity is nonzero, at least three inputs are required for [the exact extraction criterion](exact-extraction.md).

For three nonzero sensitivities, every eligible pair consists of complementary strings. Its charge equality can be written as a sum of three signed sensitivities equal to zero. If two distinct sign patterns satisfied this equality and were different even up to an overall sign, one could flip the overall sign of one pattern so that they differ at exactly one position. Subtracting would force zero sensitivity there. Thus the triple has at most one eligible pair. Its sector has no third basis string, since such a string would have opposite parity to one member and make a second eligible pair.

Every accepted Kraus operator annihilates all other sectors by [the converse](exact-extraction.md#converse-for-adaptive-circuits). The trace-nonincreasing success map can accept the remaining sector with probability at most its input weight, which is $`1/4`$. This argument bounds success for each parameter value across all receiver circuits. For positive scalar gains, a qualifying triple exists exactly when the largest gain is the sum of the other two.

## How the coherence can evade two-qubit tomography

For the two-mode example, take $`\phi_1,\phi_2`$ to be independent and uniform on $`[0,2\pi)`$. In the averaged state, the only off-diagonal element up to conjugation is the one between $`110`$ and $`001`$. Indeed all other pairs of distinct strings have unequal two-component charges and integrate to zero. Writing $`\zeta=e^{i\pi/4}`$, the state is

```math
\rho
=\frac{I_8}{8}
+\frac{\zeta\lvert 110\rangle\langle 001\rvert
+\overline{\zeta}\lvert 001\rangle\langle 110\rvert}{8}.
```

Tracing out any qubit kills the off-diagonal entries because the two strings differ at all three positions. Every two-qubit reduction is $`I_4/4`$. The full state is separable by its preparation as a mixture of conditional product states. The joint receiver still extracts the exact target with probability $`1/4`$. The fully dephased state $`I_8/8`$ has the same two-qubit reductions, but every stabilizer circuit applied to it, including a postselected branch, outputs a stabilizer mixture.

## An additive source model

The weighted phases can arise when an additive detuning $`\Delta(t)`$ is shared across three source controls. In an ideal commuting $`Z`$-rotation model, source $`j`$ accumulates a nominal phase $`\int_{I_j}\Omega_j(t)\,dt`$ and an error $`\int_{I_j}\Delta(t)\,dt`$ during its exposure window $`I_j`$. Choose adjacent short windows $`I_1,I_2`$ and set the third window to their union. Program each nominal integral to $`\pi/4`$. Additivity of the error integrals then gives $`\phi_3=\phi_1+\phi_2`$ for any integrable common waveform during the preparation.

This model requires programmable nominal control independent of exposure and a means of isolating each prepared state from further differential phase accumulation before joint processing. The two short-window qubits and one long-window qubit are three counted carriers. If each short window has duration $`\tau`$, the total exposed-qubit time in an attempt is $`4\tau`$ and the preparation span is $`2\tau`$, before routing or receiver operations. These are ideal source charges. Transport/storage, stabilizer faults and platform-specific comparison with composite-pulse or echo control require their own physical models. The protocol applies downstream of the source, where the receiver receives the already prepared states.
