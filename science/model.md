# Source and receiver model

## Delivered states

Let $`\lvert +_\alpha\rangle=(\lvert 0\rangle+e^{i\alpha}\lvert 1\rangle)/\sqrt{2}`$ and $`\lvert T\rangle=\lvert +_{\pi/4}\rangle`$. An attempt receives $`n`$ qubits in the conditional product state

```math
\lvert\Psi(\theta)\rangle
=\bigotimes_{j=1}^{n}\lvert +_{\pi/4+a_j\cdot\theta}\rangle .
```

The receiver knows the real sensitivity vectors $`a_j\in\mathbb R^m`$. The parameter $`\theta`$ is unknown and ranges over a nonempty open subset of $`\mathbb R^m`$. It may change between attempts. A one-dimensional $`\theta`$ describes a single common drift. The multi-dimensional model also describes integrated phase errors that satisfy a fixed linear relation. Averaging over an unobserved random $`\theta`$ gives a mixture of the conditional product states.

The receiver has a stable stabilizer frame and the same circuit must work for every allowed $`\theta`$. Its resources are the delivered block, stabilizer ancillas, Clifford gates, Pauli measurements, classical feedforward and randomness. It may discard registers and postselect. The task supplies no separate drift reference, nonstabilizer catalyst, or control of the source pulses. The accepted output is one qubit. For each $`\theta`$ of positive acceptance probability, the corrected accepted output must equal the pure state $`\lvert T\rangle`$ exactly. A circuit qualifies when it has positive acceptance for some allowed parameter. The attaining circuit in the main theorem achieves positive uniform acceptance.

Every supplied carrier counts, including those in rejected attempts. Gate and measurement costs refer to ideal receiver operations. A separate physical source model is needed to turn the block budget into exposure time, gate cost or fault-tolerant hardware overhead.

## Weighted charges

Use $`\zeta=e^{i\pi/4}`$ and let $`\lvert x\rvert`$ denote Hamming weight. For a bit string $`x`$, the total sensitivity is

```math
q(x)=\sum_{j=1}^{n}a_j x_j .
```

The source amplitude of $`\lvert x\rangle`$ is $`2^{-n/2}\zeta^{\lvert x\rvert}e^{i q(x)\cdot\theta}`$. All strings in a charge sector therefore acquire the same unknown phase. For those strings, the nominal weights alone determine their relative phases.

The sector vector

```math
v_q=2^{-n/2}\!\!\sum_{x:q(x)=q}\zeta^{\lvert x\rvert}\lvert x\rangle
```

is unnormalized. The $`v_q`$ have disjoint basis supports and reconstruct the full input as $`\lvert\Psi(\theta)\rangle=\sum_q e^{i q\cdot\theta}v_q`$. This decomposition is an analysis of the state. A circuit can select a suitable pair by ordinary parity checks without implementing a projective measurement of the full weighted charge.
