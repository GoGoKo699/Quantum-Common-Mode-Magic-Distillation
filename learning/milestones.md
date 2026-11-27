# Project understanding map

The **12 background milestones** build the delivered-state model from single-qubit phases, parity measurements, stabilizer arithmetic and independent phase functions. The **18 research milestones** start with the three-input circuit, prove the general criterion and connect optimal yield to physical source conditions. The [educational bridge](anchor-and-bridge.md) identifies the sections of Daniel Gottesman's review used here.

| Route | Milestones |
|---|---|
| Source states and stabilizer measurements | [M01](#m01-a-qubit-with-an-unknown-phase)–[M08](#m08-the-stabilizer-arithmetic-field) |
| Charges and the receiver's task | [M09](#m09-weighted-charges-of-basis-strings)–[M12](#m12-the-delivered-state-task) |
| From the triple to the general circuit | [M13](#m13-the-additive-triple)–[M17](#m17-correcting-the-nominal-phase) |
| Converse and sharp minimal protocol | [M18](#m18-exactness-on-every-branch)–[M23](#m23-optimal-probability-for-three-inputs) |
| Operational consequences and scope | [M24](#m24-invisible-coherence-in-pair-marginals)–[M30](#m30-the-complete-scientific-story) |

## Background and preliminaries

### M01 A qubit with an unknown phase

**Central question.** Where does the error enter a delivered equatorial state?

**Understanding target.** Read the phase as a relative amplitude between the computational basis states and recognize the fixed T-state target.

**Prerequisites.** This is the starting point.

**Conceptual connection.** This makes the desired phase and the nuisance phase visible in the same expression.

**Sources.** [Delivered-state model](../science/model.md)

### M02 Sensitivity vectors

**Central question.** What does a shared phase error mean when different qubits respond differently?

**Understanding target.** Calculate each phase shift from its known sensitivity vector and the same unknown parameter vector.

**Prerequisites.** [M01](#m01-a-qubit-with-an-unknown-phase).

**Conceptual connection.** A source can respond to a shared drift with unequal gains or several common modes.

**Sources.** [Delivered-state model](../science/model.md)

### M03 Conditional products and averaged states

**Central question.** How can a product source acquire correlations after averaging?

**Understanding target.** Separate the tensor-product state at fixed nuisance parameters from its mixture when those parameters fluctuate.

**Prerequisites.** [M01](#m01-a-qubit-with-an-unknown-phase), [M02](#m02-sensitivity-vectors).

**Conceptual connection.** This distinction will explain how separable inputs can retain useful multiqubit coherence.

**Sources.** [Delivered-state model](../science/model.md)

### M04 Pauli parity as a measurement

**Central question.** Which property of a computational string is read by a product of Z operators?

**Understanding target.** Compute the sign of a Z parity on a basis string and group strings by their sign without resolving them individually.

**Prerequisites.** [M01](#m01-a-qubit-with-an-unknown-phase).

**Conceptual connection.** The measurement can preserve coherence between strings that give the same sign.

**Sources.** [Verified anchor sections](anchor-and-bridge.md#educational-anchor)

### M05 Signed joint eigenspaces

**Central question.** How can two checks leave a logical qubit in a larger block?

**Understanding target.** Use the product of commuting signed Pauli projectors to identify the accepted subspace and its dimension.

**Prerequisites.** [M04](#m04-pauli-parity-as-a-measurement).

**Conceptual connection.** The code space, the measurement syndrome and the retained logical state each play a different role.

**Sources.** [Verified anchor sections](anchor-and-bridge.md#educational-anchor) · [Three-input protocol](../science/three-input-protocol.md)

### M06 Clifford decoding of XOR constraints

**Central question.** How does a CNOT change a classical parity into a target-wire bit?

**Understanding target.** Track CNOT on basis labels and under conjugation of Pauli products, then move a joint syndrome to separate measured wires.

**Prerequisites.** [M04](#m04-pauli-parity-as-a-measurement), [M05](#m05-signed-joint-eigenspaces).

**Conceptual connection.** The parity-check description and the executable two-CNOT circuit become equivalent.

**Sources.** [Verified anchor sections](anchor-and-bridge.md#educational-anchor) · [Three-input protocol](../science/three-input-protocol.md)

### M07 Postselection and purity

**Central question.** What must an accepted instrument branch do to return an exact pure state?

**Understanding target.** Distinguish its unnormalized output, probability and conditional output. Use positivity to explain why each fine successful branch must be supported on the same target ray.

**Prerequisites.** [M03](#m03-conditional-products-and-averaged-states), [M05](#m05-signed-joint-eigenspaces).

**Conceptual connection.** This connects a single syndrome calculation to the arbitrary-instrument converse.

**Sources.** [Delivered-state model](../science/model.md) · [Exact extraction theorem](../science/exact-extraction.md)

### M08 The stabilizer arithmetic field

**Central question.** Why do ratios of computational amplitudes matter?

**Understanding target.** Describe a fine stabilizer branch as a Gaussian-rational matrix up to an overall factor. Identify the target amplitude ratio as outside that field.

**Prerequisites.** [M06](#m06-clifford-decoding-of-xor-constraints), [M07](#m07-postselection-and-purity).

**Conceptual connection.** The field constraint can rule out exact conversion even when an input might contain a different form of magic.

**Sources.** [Exact extraction theorem](../science/exact-extraction.md)

### M09 Weighted charges of basis strings

**Central question.** Which weighted sum labels the unknown phase of a basis string?

**Understanding target.** Expand a block in basis strings and assign each a charge and a Hamming weight. Identify which controls the unknown phase and which controls the nominal phase.

**Prerequisites.** [M01](#m01-a-qubit-with-an-unknown-phase), [M02](#m02-sensitivity-vectors), [M03](#m03-conditional-products-and-averaged-states).

**Conceptual connection.** This recasts drift cancellation as a property of relative phases within a sector.

**Sources.** [Delivered-state model](../science/model.md) · [Exact extraction theorem](../science/exact-extraction.md)

### M10 Even and odd Hamming weights

**Central question.** What does nominal phase contribute within a fixed charge?

**Understanding target.** Separate even and odd powers of the eighth root appearing in the raw amplitudes and identify their relationship to the fourth roots supplied by Cliffords.

**Prerequisites.** [M08](#m08-the-stabilizer-arithmetic-field), [M09](#m09-weighted-charges-of-basis-strings).

**Conceptual connection.** A sector containing weights of both parities can carry the phase needed for an exact T state.

**Sources.** [Exact extraction theorem](../science/exact-extraction.md)

### M11 Identifying independent phase functions

**Central question.** Why can different charges be considered separately when the model holds on an open set?

**Understanding target.** Restrict to a line with distinct projected frequencies and use independence of its exponential phase functions.

**Prerequisites.** [M09](#m09-weighted-charges-of-basis-strings).

**Conceptual connection.** An identity valid for every allowed nuisance parameter becomes one identity per charge.

**Sources.** [Exact extraction theorem](../science/exact-extraction.md)

### M12 The delivered-state task

**Central question.** What can the receiver control, and what guarantee counts as success?

**Understanding target.** State the receiver access, allowed operations, output condition and raw-qubit accounting together. Explain the roles of the calibrated Clifford frame and the absence of a nonstabilizer catalyst.

**Prerequisites.** [M02](#m02-sensitivity-vectors), [M03](#m03-conditional-products-and-averaged-states), [M06](#m06-clifford-decoding-of-xor-constraints), [M07](#m07-postselection-and-purity), [M09](#m09-weighted-charges-of-basis-strings), [M11](#m11-identifying-independent-phase-functions).

**Conceptual connection.** The model pins down where the constructive protocol and general obstruction both apply.

**Sources.** [Delivered-state model](../science/model.md)

## Narrative and innovation

### M13 The additive triple

**Central question.** Which two strings share an unknown phase when the third error equals the sum of the first two?

**Understanding target.** Compare the one-excitation string 001 with the two-excitation string 110, and derive their residual relative phase.

**Prerequisites.** [M09](#m09-weighted-charges-of-basis-strings), [M10](#m10-even-and-odd-hamming-weights), [M12](#m12-the-delivered-state-task).

**Conceptual connection.** A phase relation among the delivered inputs creates the simplest useful charge sector.

**Sources.** [Educational bridge](anchor-and-bridge.md) · [Three-input protocol](../science/three-input-protocol.md)

### M14 An accepted parity syndrome

**Central question.** Which reports isolate the additive triple's useful pair?

**Understanding target.** Translate equality of the first two bits and inequality of the first and third into the pair of signed Z-parity outcomes.

**Prerequisites.** [M04](#m04-pauli-parity-as-a-measurement), [M05](#m05-signed-joint-eigenspaces), [M13](#m13-the-additive-triple).

**Conceptual connection.** This identifies the branch that keeps exactly the two amplitudes selected by the phase relation.

**Sources.** [Educational bridge](anchor-and-bridge.md) · [Three-input protocol](../science/three-input-protocol.md)

### M15 Decode and count the successful attempts

**Central question.** How do the encoded amplitudes become a physical T state?

**Understanding target.** Track the two accepted strings under the two CNOTs and obtain a fixed helper result and a target on qubit 1. Compute the probability from the squared amplitudes.

**Prerequisites.** [M06](#m06-clifford-decoding-of-xor-constraints), [M07](#m07-postselection-and-purity), [M14](#m14-an-accepted-parity-syndrome).

**Conceptual connection.** The example connects a coherent sector to a physical output and a raw-input cost.

**Sources.** [Three-input protocol](../science/three-input-protocol.md)

### M16 An affine line for any collision

**Central question.** How do stabilizer measurements isolate a selected equal-charge pair in a larger block?

**Understanding target.** Use the binary difference between the strings to characterize the parity equations satisfied by both, and identify their joint solution space.

**Prerequisites.** [M05](#m05-signed-joint-eigenspaces), [M09](#m09-weighted-charges-of-basis-strings), [M15](#m15-decode-and-count-the-successful-attempts).

**Conceptual connection.** The three-input circuit becomes a general pair-isolation construction.

**Sources.** [Exact extraction theorem](../science/exact-extraction.md)

### M17 Correcting the nominal phase

**Central question.** Why does an odd weight difference give the target after a Clifford correction?

**Understanding target.** Track the relative eighth root through binary decoding and select a power of the phase gate to obtain the prescribed target phase.

**Prerequisites.** [M06](#m06-clifford-decoding-of-xor-constraints), [M10](#m10-even-and-odd-hamming-weights), [M16](#m16-an-affine-line-for-any-collision).

**Conceptual connection.** This completes the sufficient side of the exact extraction criterion.

**Sources.** [Exact extraction theorem](../science/exact-extraction.md)

### M18 Exactness on every branch

**Central question.** How does the requirement of a pure output constrain every allowed protocol?

**Understanding target.** Refine measurements, classical randomness and discarded wires into fine branches. Write the orthogonal component of a successful branch as a sum over charges.

**Prerequisites.** [M07](#m07-postselection-and-purity), [M09](#m09-weighted-charges-of-basis-strings), [M11](#m11-identifying-independent-phase-functions), [M12](#m12-the-delivered-state-task).

**Conceptual connection.** This removes dependence on the receiver using a parity-check circuit of the exhibited form.

**Sources.** [Exact extraction theorem](../science/exact-extraction.md)

### M19 Eliminating single-parity sectors

**Central question.** Why does a sector with only one weight parity contribute zero to exact success?

**Understanding target.** Combine the sectorwise pure-output constraint with preservation of the Gaussian-rational projective form to show the sector must be annihilated.

**Prerequisites.** [M08](#m08-the-stabilizer-arithmetic-field), [M10](#m10-even-and-odd-hamming-weights), [M18](#m18-exactness-on-every-branch).

**Conceptual connection.** The obstruction reaches every accepted branch of every allowed stabilizer protocol.

**Sources.** [Exact extraction theorem](../science/exact-extraction.md)

### M20 The exact extraction criterion

**Central question.** How do the pair circuit and the arithmetic obstruction meet?

**Understanding target.** Read both directions of the equal-charge, opposite-weight-parity criterion and identify the dependence on known sensitivities and nuisance parameters with an open domain.

**Prerequisites.** [M16](#m16-an-affine-line-for-any-collision), [M17](#m17-correcting-the-nominal-phase), [M19](#m19-eliminating-single-parity-sectors).

**Conceptual connection.** This gives a complete existence decision for each finite block.

**Sources.** [Exact extraction theorem](../science/exact-extraction.md)

### M21 One or two sensitive inputs

**Central question.** Why can no one- or two-input block work when all gains are nonzero?

**Understanding target.** Relate parity difference to odd Hamming distance and show that a distance-one collision forces one zero sensitivity.

**Prerequisites.** [M09](#m09-weighted-charges-of-basis-strings), [M20](#m20-the-exact-extraction-criterion).

**Conceptual connection.** The statement concerns exact conversion of a block. It also applies when an individual input may be nonstabilizer.

**Sources.** [Three-input protocol](../science/three-input-protocol.md) · [Exact extraction theorem](../science/exact-extraction.md)

### M22 Uniqueness of the useful triple sector

**Central question.** What can an odd-distance collision look like on three sensitive qubits?

**Understanding target.** Identify complementary strings and the corresponding signed sensitivity relation. Explain why two distinct relations of this kind would force a zero sensitivity.

**Prerequisites.** [M19](#m19-eliminating-single-parity-sectors), [M21](#m21-one-or-two-sensitive-inputs).

**Conceptual connection.** A qualifying triple has a unique sector with both parities and exactly two useful amplitudes.

**Sources.** [Three-input protocol](../science/three-input-protocol.md)

### M23 Optimal probability for three inputs

**Central question.** Why can a different stabilizer circuit never beat one quarter on such a triple?

**Understanding target.** Use the annihilation of every other sector and trace nonincrease of the success instrument to bound yield by the norm squared of the surviving sector.

**Prerequisites.** [M15](#m15-decode-and-count-the-successful-attempts), [M19](#m19-eliminating-single-parity-sectors), [M22](#m22-uniqueness-of-the-useful-triple-sector).

**Conceptual connection.** The circuit reaches an upper bound valid pointwise in the nuisance parameters.

**Sources.** [Three-input protocol](../science/three-input-protocol.md)

### M24 Invisible coherence in pair marginals

**Central question.** How can the triple work when no pair of qubits reveals its useful phase?

**Understanding target.** Average two independent uniform modes, identify which off-diagonal coherence remains and trace out any one qubit.

**Prerequisites.** [M03](#m03-conditional-products-and-averaged-states), [M13](#m13-the-additive-triple), [M23](#m23-optimal-probability-for-three-inputs).

**Conceptual connection.** The surviving three-body coherence is operationally useful despite the maximally mixed pair reductions.

**Sources.** [Three-input protocol](../science/three-input-protocol.md)

### M25 A projection bound for larger blocks

**Central question.** How can the weights of both parities constrain success across many sectors?

**Understanding target.** Read the field conjugation that maps the target to its orthogonal partner. Relate the resulting forbidden input directions to an upper bound in terms of even and odd sector masses.

**Prerequisites.** [M08](#m08-the-stabilizer-arithmetic-field), [M17](#m17-correcting-the-nominal-phase), [M19](#m19-eliminating-single-parity-sectors), [M23](#m23-optimal-probability-for-three-inputs).

**Conceptual connection.** The same arithmetic that decides feasibility also bounds the yield of a general block.

**Sources.** [Yield and robustness](../science/yield-and-robustness.md)

### M26 Comparing a filter with a yield bound

**Central question.** Which resource claim follows from one selected pair in a larger block?

**Understanding target.** Compare its explicitly attained probability with the bound for a general instrument and explain why a feasible circuit alone does not establish optimal yield.

**Prerequisites.** [M16](#m16-an-affine-line-for-any-collision), [M17](#m17-correcting-the-nominal-phase), [M25](#m25-a-projection-bound-for-larger-blocks).

**Conceptual connection.** Existence, success probability and optimality are distinct design questions for larger blocks.

**Sources.** [Exact extraction theorem](../science/exact-extraction.md) · [Yield and robustness](../science/yield-and-robustness.md)

### M27 Imperfect phase addition

**Central question.** Which residual phase error reaches the output after a successful triple?

**Understanding target.** Track the deviation from exact additivity through the accepted branch and relate it to conditional infidelity. Identify why the success rate is insensitive to phase-only deviations of equatorial product inputs.

**Prerequisites.** [M13](#m13-the-additive-triple), [M15](#m15-decode-and-count-the-successful-attempts), [M23](#m23-optimal-probability-for-three-inputs).

**Conceptual connection.** A correct syndrome heralds the chosen subspace, while output quality can still depend on phase alignment.

**Sources.** [Yield and robustness](../science/yield-and-robustness.md) · [Three-input protocol](../science/three-input-protocol.md)

### M28 Physical source and receiver roles

**Central question.** What would a hardware implementation have to supply?

**Understanding target.** Account for the sensitivities and nominal phases as source properties, distinguish them from the receiver's Clifford operations, and identify where source control or extra noise would change the model.

**Prerequisites.** [M12](#m12-the-delivered-state-task), [M23](#m23-optimal-probability-for-three-inputs), [M27](#m27-imperfect-phase-addition).

**Conceptual connection.** This makes the delivered-state result usable without attributing a hardware capability to the abstract circuit.

**Sources.** [Delivered-state model](../science/model.md) · [Yield and robustness](../science/yield-and-robustness.md)

### M29 Reading theorem evidence and attribution

**Central question.** What does the finite verification establish alongside the proofs?

**Understanding target.** Trace which source relationships use known stabilizer and phase facts, which claims follow from the theorem and which circuit or numerical checks test finite instances.

**Prerequisites.** [M20](#m20-the-exact-extraction-criterion), [M23](#m23-optimal-probability-for-three-inputs), [M24](#m24-invisible-coherence-in-pair-marginals), [M25](#m25-a-projection-bound-for-larger-blocks), [M27](#m27-imperfect-phase-addition).

**Conceptual connection.** The reader can assess exactness, physical scope and evidence separately when relating this work to existing concentration protocols.

**Sources.** [Educational bridge](anchor-and-bridge.md) · [Scientific reading route](../science/README.md)

### M30 The complete scientific story

**Central question.** When can common phase drift be removed while retaining a fixed non-Clifford phase?

**Understanding target.** Explain the full sequence from weighted charges to the parity filter, exact obstruction, sharp triple yield and the consequences of imperfect source alignment.

**Prerequisites.** [M20](#m20-the-exact-extraction-criterion), [M23](#m23-optimal-probability-for-three-inputs), [M24](#m24-invisible-coherence-in-pair-marginals), [M26](#m26-comparing-a-filter-with-a-yield-bound), [M27](#m27-imperfect-phase-addition), [M28](#m28-physical-source-and-receiver-roles), [M29](#m29-reading-theorem-evidence-and-attribution).

**Conceptual connection.** The same sector structure connects what the receiver can recover, how often it can succeed and which source assumptions matter.

**Sources.** [Scientific reading route](../science/README.md) · [Exact extraction theorem](../science/exact-extraction.md) · [Three-input protocol](../science/three-input-protocol.md) · [Yield and robustness](../science/yield-and-robustness.md)
