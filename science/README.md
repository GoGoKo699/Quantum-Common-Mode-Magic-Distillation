# Scientific account

When raw magic states share a phase error, a receiver can sometimes cancel the error without learning its value. The receiver needs a pair of computational-basis strings that accumulate the same unknown phase while retaining a non-Clifford relative phase. Two parity checks select such a pair for a three-input source with additive phase errors.

| Question | Result | Source |
| --- | --- | --- |
| What information and controls does the receiver have? | It receives a block of equatorial states and knows their sensitivity vectors. Its subsequent operations are stabilizer operations in a fixed frame. | [Source and receiver model](model.md) |
| Which sources permit exact extraction? | At least one weighted charge sector contains bit strings of opposite Hamming-weight parity. A parity projection attains extraction whenever the condition holds. | [Exact extraction criterion](exact-extraction.md) |
| What is the smallest block? | With nonzero sensitivities, three inputs are necessary. A triple with additive phase errors yields one exact $`T`$ state with optimal probability $`1/4`$ at every allowed phase. | [Three-input protocol](three-input-protocol.md) |
| How does yield change with a larger block? | A pointwise upper bound follows from the even and odd sector masses. Repeated triples attain the bound if their nuisance coordinates are disjoint. | [Yield and phase mismatch](yield-and-robustness.md) |
| What changes when each source can suffer a whole-bundle Z burst? | Fifth-order suppression requires a charge sector containing all 32 source parity labels. With fully independent offsets only first order is possible, while phase-tied receivers attain fifth order. | [Burst converse](burst-converse.md) |

The two-mode construction can deliver usable coherence even when two-input tomography finds a maximally mixed state for every pair. The full averaged state is a mixture of product states, and the protocol reads the coherence between two basis strings that differ on all three inputs. The [related-work account](../references/RELATED_WORK.md) credits prior results on exact magic concentration, number-field obstructions and magic in separable correlations.
