# From Pauli measurements to exact T-state extraction

The receiver is handed a block of equatorial qubits. Each carries an unknown phase shift, but the sensitivities of the qubits to the same unknown parameters are known. The aim is to return a fixed one-qubit T state on a heralded outcome. A useful parity measurement must reveal which subspace the block occupies while preserving the relative phase inside that subspace.

## Educational anchor

Daniel Gottesman, *An Introduction to Quantum Error Correction and Fault-Tolerant Quantum Computation*, arXiv:0904.2557v1, 16 April 2009. This is also the anchor for [Quantum Magic Burst Routing](https://github.com/GoGoKo699/Quantum-Magic-Burst-Routing). [Open the versioned text](https://arxiv.org/html/0904.2557v1)

| Section | Read for | Where it enters this project |
|---|---|---|
| §2.3, Eqs. (39)–(41) | Pauli parity measurements and their joint eigenspaces | See how the accepted syndrome leaves a two-dimensional code space and keeps its coherence. |
| §§3.1 and 3.4 | Binary linear codes and logical Pauli operations | Link parity equations to a surviving logical qubit, then track the signs of its Pauli faults. |
| §3.5 | Hadamard, phase gate, CNOT, and stabilizer encoding and decoding | Compile the two-input-string subspace into a single output wire. |
| §§4.5–4.6 | Phase-gate ancillas and selective ancilla preparation | Place the target T state in fault-tolerant computation and count the cost of a rejected herald. |

Here $`H`$ is the Hadamard and $`S=\mathrm{diag}(1,i)`$ is the Clifford phase gate. The desired state is $`|T\rangle=(|0\rangle+\zeta|1\rangle)/\sqrt2`$, with $`\zeta=e^{i\pi/4}`$. It has a relative phase of $`\pi/4`$, while $`S`$ changes a relative phase in steps of $`\pi/2`$.

## Work through the three-qubit circuit

For $`j=1,2,3`$, denote the phase error on the delivered qubit by $`\phi_j`$. The $`|1\rangle`$ amplitude is $`e^{i(\pi/4+\phi_j)}/\sqrt2`$. In the joint product, the amplitudes of $`|001\rangle`$ and $`|110\rangle`$ have the same magnitude and phases $`\pi/4+\phi_3`$ and $`\pi/2+\phi_1+\phi_2`$, respectively. Their ratio in the logical order $`001,110`$ is

```math
e^{i(\pi/4+\phi_1+\phi_2-\phi_3)}.
```

The receiver measures $`Z_1Z_2`$ and $`Z_1Z_3`$, retaining the $`(+1,-1)`$ syndrome. This learns $`x_1=x_2`$ and $`x_1\ne x_3`$ on a computational string $`x`$. Exactly $`001`$ and $`110`$ satisfy both. They give identical reports, so the measurement retains their relative phase. Each has squared amplitude $`1/8`$, giving acceptance probability $`1/4`$.

Apply CNOTs from qubit 1 to qubits 2 and 3. The two accepted strings become $`001`$ and $`101`$, so the last two wires are fixed at $`01`$ and qubit 1 carries the logical relative phase. In the equivalent two-CNOT implementation the receiver applies the CNOTs first, then measures wires 2 and 3 in the computational basis and accepts $`01`$. If $`\phi_3=\phi_1+\phi_2`$, the relative phase is exactly $`\pi/4`$ for every allowed block. [Full circuit and its resource accounting](../science/three-input-protocol.md)

## From the example to a theorem

**Replace the cancellation identity by equality of charges.** If the delivered phase on qubit $`j`$ is $`\phi_j=a_j\cdot\theta`$, a string $`x`$ acquires unknown phase $`q(x)\cdot\theta`$ with $`q(x)=\sum_j x_ja_j`$. It also acquires nominal phase $`\pi|x|/4`$, where $`|x|`$ is its Hamming weight. Equal charges make the unknown factor global on the pair. An odd weight difference leaves an odd multiple of $`\pi/4`$, which powers of $`S`$ can put into the required form. The same signed Pauli measurement principle isolates any specified pair by reading the binary linear equations shared by both strings. [Source model](../science/model.md) · [General extraction circuit](../science/exact-extraction.md)

**Separate the noise modes in the converse.** For any fixed accepted branch, the coefficient along a state orthogonal to $`|T\rangle`$ must vanish for every value of the unknown parameters. Along a line separating the finitely many charges, these terms are distinct exponentials. Linear independence forces the orthogonal component to vanish in each charge sector separately. Thus every surviving sector must supply the exact target within the same branch.

**Use the arithmetic restriction of stabilizer processing.** In the computational basis, a fine stabilizer branch has entries in $`\mathbb Q(i)`$ up to a shared scalar. For instance, $`H`$ supplies a common factor $`1/\sqrt2`$, while $`S`$ supplies a factor of $`i`$ on its $`|1\rangle`$ component. Clifford generators, signed Pauli projectors and computational-basis contractions preserve this form under composition. In a charge sector containing only even weights, all powers of $`\zeta`$ are powers of $`i`$. In an odd-only sector there is one additional common factor $`\zeta`$. The ratio needed for the T state lies outside $`\mathbb Q(i)`$, forcing every branch that exactly succeeds to annihilate every same-parity sector. The anchor supplies the stabilizer operations. The project supplies this arithmetic argument for the delivered-state family and the proof of necessity and sufficiency. [Exact-extraction proof](../science/exact-extraction.md)

## Add a whole-bundle burst

A $`Z`$ fault on every member of a triple supplies opposite signs on the two accepted strings because their parities differ. Decoding still removes the unknown continuous phase and transfers that binary sign to the logical qubit. For five triples equipped with ties, a comparator keeps two strings with equal charge and even weight difference. After decoding its logical $`X`$ sign records a relative burst parity. Without cross-source ties, a charge sector is a product of singleton and two-string factors. The latter give at most five noisy logical T states and make the ordinary distillation lower bound applicable. [Burst converse](../science/burst-converse.md)

The [30 milestones](milestones.md) develop the source model and stabilizer operations first, then connect the extraction criterion, optimal three-input probability, larger-block bounds, and the distinction between phase cancellation and burst suppression.
