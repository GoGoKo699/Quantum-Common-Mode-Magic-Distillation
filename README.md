# Quantum Common-Mode Magic Distillation

**Can a receiver recover an exact T state from raw states with unknown phase errors?** Three inputs suffice when the third phase error is the sum of the first two. A fixed stabilizer circuit heralds an exact T state with probability 1/4, independent of both unknown phases. That yield is optimal for these three inputs, and three is the minimum when every input has nonzero phase sensitivity.

Each source aims for the equatorial state with relative phase π/4. Measure the two Z parities that select the basis strings `001` and `110`. Their unknown phases agree, while their nominal phases differ by π/4. Two CNOTs decode the surviving superposition to one qubit. Equivalently, apply those CNOTs first, measure the other two qubits, and accept the outcome `01`.

| Result | What it establishes |
| --- | --- |
| [Exact extraction criterion](science/exact-extraction.md) | For any finite input block with known phase sensitivities, success is possible exactly when two strings have the same total phase sensitivity and opposite Hamming-weight parity. |
| [Optimal three-input protocol](science/three-input-protocol.md) | The two-check circuit attains the pointwise bound of 1/4. When the first two phase errors are independent and uniform, every two-qubit marginal of the averaged input is maximally mixed. |
| [Yield and robustness](science/yield-and-robustness.md) | A pointwise upper bound applies to arbitrary gain lists. Independent three-input blocks attain a sharp combined yield. For the minimal circuit, residual output error depends only on the mismatch in the phase sum. |

## Read the science

The [science overview](science/README.md) connects the [input model](science/model.md), the exact protocol, and the converse. The [related work](references/RELATED_WORK.md) covers universal magic concentration, correlated-source distillation, and source-side composite pulse control.

## Learn the project

The educational anchor is Daniel Gottesman’s *The Heisenberg Representation of Quantum Computers* (1998). The [bridge](learning/anchor-and-bridge.md) uses its Pauli, Clifford, and stabilizer formalism to derive the two-check decoder, then develops the weighted phase sectors and the converse. The [30-milestone map](learning/milestones.md) follows the argument from the raw source model to the yield bounds. The [reading guide](llms.txt) points to the authoritative account for each result.

## Reproduce the checks

Run `python3 verification/check.py` from the repository root. The [verification guide](verification/README.md) describes the finite checks and their relationship to the proofs.

## Scope

The receiver receives prepared states and their known phase sensitivities. The exact results assume ideal stabilizer operations in a stable Clifford reference frame, with no nonstabilizer catalyst or control over the source pulses. Every raw input is charged, including rejected runs. Independent phase errors, faulty processing, and the cost of realizing the source affect the physical implementation.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
