# Quantum Common-Mode Magic Distillation

**Can a receiver recover an exact T state from raw states with unknown phase errors?** Three inputs suffice when the third phase error is the sum of the first two. A fixed stabilizer circuit heralds an exact T state with probability 1/4, independent of both unknown phases. That yield is optimal for these three inputs, and three is the minimum when every input has nonzero phase sensitivity.

Each source aims for the equatorial state with relative phase π/4. Measure the two Z parities that select the basis strings `001` and `110`. Their unknown phases agree, while their nominal phases differ by π/4. Two CNOTs decode the surviving superposition to one qubit.

To run the [fused receiver](science/three-input-protocol.md#preparation-and-receiver), put the qubit with the summed phase error in position 3. Use qubit 1 as the control for a CNOT onto qubit 2 and then a CNOT onto qubit 3. Measure qubits 2 and 3 in the computational basis. Keep qubit 1 as the T-state output if their ordered bits are `01`. Otherwise discard the block and report rejection. Each attempt consumes three raw inputs.

With five sources that also suffer whole-bundle Z bursts, the [Quantum Magic Burst Routing](https://github.com/GoGoKo699/Quantum-Magic-Burst-Routing) sister project constructs a receiver that uses cross-source phase ties to obtain fifth-order infidelity at positive yield. Its checks distinguish complementary burst histories. The [converse here](science/burst-converse.md) shows why fully independent offsets limit the same 15 supplied carriers to first order, and why sixth order is impossible even with ties.

| Result | What it establishes |
| --- | --- |
| [Exact extraction criterion](science/exact-extraction.md) | For any finite input block with known phase sensitivities, success is possible exactly when two strings have the same total phase sensitivity and opposite Hamming-weight parity. |
| [Optimal three-input protocol](science/three-input-protocol.md) | The two-check circuit attains the pointwise bound of 1/4. When the first two phase errors are independent and uniform, every two-qubit marginal of the averaged input is maximally mixed. |
| [Yield and robustness](science/yield-and-robustness.md) | A pointwise upper bound applies to arbitrary gain lists. Independent three-input blocks attain a sharp combined yield. For the minimal circuit, residual output error depends only on the mismatch in the phase sum. |
| [Continuous drift with source bursts](science/burst-converse.md) | A successful fifth-order branch requires one charge sector containing all 32 source parity labels. The fully independent model reduces to at most five logical T inputs in each sector. |

## Read the science

The [science overview](science/README.md) connects the [input model](science/model.md), the exact protocol, and the converse. The [related work](references/RELATED_WORK.md) covers universal magic concentration, correlated-source distillation, and source-side composite pulse control.

## Learn the project

The educational anchor is Daniel Gottesman’s *An Introduction to Quantum Error Correction and Fault-Tolerant Quantum Computation* (2009). The [bridge](learning/anchor-and-bridge.md) uses its Pauli, Clifford, and stabilizer formalism to derive the two-check decoder and develop the charge-sector proof. The [30-milestone map](learning/milestones.md) follows the argument from the raw source model through exact extraction, yield bounds, and the burst converse. The [reading guide](llms.txt) points to the authoritative account for each result.

## Reproduce the checks

Run `python3 verification/check.py` from the repository root. The [verification guide](verification/README.md) describes the finite checks and their relationship to the proofs.

## Scope

The receiver receives prepared states and their known phase sensitivities. The results assume ideal stabilizer operations in a stable Clifford reference frame, with no nonstabilizer catalyst or control over the source pulses. Every raw input is charged, including rejected runs. The burst converse assumes each burst flips all carriers of its source and the burst rate sets the small parameter.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
