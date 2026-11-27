# Unknown phase drift with source bursts

Five sources each supply three equatorial qubits $`A_i,B_i,C_i`$ with nominal phase $`\pi/4`$ and unknown offsets $`\theta_i,\phi_i,\theta_i+\phi_i`$. A hidden burst bit $`b_i`$ applies $`Z`$ to the whole bundle. For suppression orders the five bits are independent Bernoulli variables of rate $`p`$. The receiver has the 15 supplied qubits and the ideal stabilizer operations of the [delivered-state model](model.md). The offsets range over a nonempty relatively open subset of a fixed linear subspace, and the receiver must work throughout that set without a drift or burst record.

When appropriate phase ties hold, the [sister receiver](https://github.com/GoGoKo699/Quantum-Magic-Burst-Routing) achieves fifth-order conditional infidelity with positive limiting yield by measuring relative burst parities and retaining one phase-cancelled output. We prove that fifth order is impossible with fully independent offsets and that sixth order is impossible even with phase ties. With fully independent offsets the known quadratic distillation lower bound sharpens the conclusion to first order.

## Separate charges and burst parities

Let $`q(x)`$ be the weighted charge of a computational string $`x`$, restricted to the allowed phase subspace. Write $`r(x)\in\mathbb F_2^5`$ for the five parities of $`x`$ within the source bundles and $`\zeta=e^{i\pi/4}`$. Omitting the common factor $`2^{-15/2}`$ gives the sector and history vectors

```math
v_{q,r}=\sum_{x:q(x)=q,\;r(x)=r}\zeta^{|x|}|x\rangle,
\qquad
u_{q,b}=\sum_r(-1)^{b\cdot r}v_{q,r}.
```

At suppression order $`d`$, every history with weight below $`d`$ has zero accepted wrong mass for a fixed receiver. Its probability scales as $`p^{|b|}`$ and no other history can cancel its contribution to the error. By positivity of the accepted state, each fine Kraus branch $`K`$ sends the full input for that history into the line of $`|T\rangle`$. Distinct charge exponentials are independent on the allowed open region, by the [same separation argument](exact-extraction.md#converse-for-adaptive-circuits) as in the drift-only model. Thus every individual $`Ku_{q,b}`$ lies in the target line for those histories.

A fine $`K`$ has entries in $`\mathbb Q(i)`$ after a common rescaling. The involution $`\zeta\mapsto-\zeta`$ fixes those entries and flips the sign on each odd-weight basis string. Because the bundles partition the block, this replaces $`b`$ by $`b+\mathbf1`$ and exchanges the lines of $`|T\rangle`$ and $`Z|T\rangle`$. For fifth-order suppression, the partner of every history of weight 1 through 4 also has weight below five. Both line constraints apply and imply $`Ku_{q,b}=0`$ for those 30 histories. The two endpoint images lie in orthogonal lines. Fourier inversion on the five binary bits then gives

```math
Kv_{q,r}=2^{-5}\left(Ku_{q,0}+(-1)^{|r|}Ku_{q,\mathbf1}\right).
```

A charge sector with any missing parity label has $`v_{q,r}=0`$ at that label, so orthogonality forces both endpoint images to vanish. A branch with clean success therefore needs a sector containing all 32 parity labels. At sixth order, even the all-burst history must map to the target line. Its conjugate constraint from the clean history forces its image to vanish, and the same argument eliminates the clean image. No positive clean yield remains. The involution argument concerns hidden histories and requires no measurement of the full weighted charge.

## Fully independent offsets

When the ten phase coordinates are free, the charge in one bundle is $`(x_{A_i}+x_{C_i},x_{B_i}+x_{C_i})`$. Only charge $`(1,1)`$ contains both parities, from $`001`$ and $`110`$. All other charges fix a unique string. Thus the only sector containing all 32 parity labels is the product of the five two-string sectors.

The [three-input Clifford decoder](three-input-protocol.md#preparation-and-receiver) identifies that sector with five logical qubits. Write its inverse, including the fixed computational ancillas, as $`V`$. The sector vectors become, up to a common normalization, the 32 orthogonal products of $`|T\rangle`$ and $`Z|T\rangle`$. A clean-success branch restricted to this sector would make $`KV`$ vanish on the 30 intermediate products and send the endpoint products to orthogonal states. Both endpoint outputs are nonzero because the field involution takes one to the other after normalizing $`K`$ over $`\mathbb Q(i)`$. It follows that the support of $`(KV)^\dagger KV`$ would be the two-dimensional span of the endpoint products.

Applying a fine stabilizer branch, composed with $`V`$, to halves of Bell pairs gives a vector proportional to a pure stabilizer state. Its input marginal is proportional to a stabilizer projector because tracing out the output retains only the stabilizers supported on the input. Transposition gives $`(KV)^\dagger KV`$ and preserves the projector property. A rank-two stabilizer code on five qubits has a nonidentity Pauli fixing it. Each nonidentity Pauli on the product $`|T\rangle^{\otimes5}`$ has expectation of magnitude at most $`1/\sqrt2`$ by factorization. That product cannot belong to such a code, which rules out fifth order for any joint stabilizer receiver.

### Sharp order from the ordinary distillation bound

Every independent-phase sector is a Clifford embedding of a product of at most five $`T`$ states, with fixed computational states on the remaining carriers. The burst on each two-string factor acts as a logical $`Z`$ because its two strings have opposite parity. Bursts on singleton factors add only overall signs. For quadratic suppression, the sector separation already forces a clean-success branch to accept the fault-free logical product and to send each single logical fault to the target line or to zero. This would be an ordinary quadratic stabilizer distiller from at most five noisy equatorial $`T`$ states. [Balada Gaggioli and Mareček, Proposition 5](https://arxiv.org/html/2610.31115v1) exclude even eight inputs for this task. Thus first order is sharp with independent offsets. The one-bundle decoder attains it with acceptance $`1/4`$ and conditional infidelity $`p`$, charging all 15 supplied carriers in this model.

### Receivers chosen as a function of the burst rate

The impossibilities persist if the receiver depends on $`p`$ and its yield has positive limsup at a fixed allowed phase, with the stated suppression order holding pointwise throughout the allowed region. Each fine branch has a Choi operator proportional to one of a fixed finite set of normalized stabilizer projectors. Their nonnegative coefficients have bounded sum by the trace-nonincreasing constraint, so a sequence of accepted maps has a convergent subsequence within the same cone. Take the subsequence along which yield stays positive. For every lower-weight history and each allowed phase, the wrong mass tends to zero by dividing the total wrong mass bound by the history probability. By continuity the limiting map has zero wrong mass there, and by positivity each fine branch inherits that constraint. The nonzero histories have total probability $`O(p)`$, so the limiting map has a clean-success branch at the chosen phase. The fixed-map arguments exclude that branch.

## Relation to earlier work

The [charge-sector extraction proof](exact-extraction.md) separates the continuous phases and uses the Gaussian-rational restriction of stabilizer branches. [Beverland et al.](https://arxiv.org/abs/1904.01124) provide the number-field antecedent for exact conversion. [Balada Gaggioli and Mareček](https://arxiv.org/html/2610.31115v1) formulate branch reduction and fault-complement arguments for ordinary noisy $`T`$ inputs, and their quadratic lower bound is used above after the sector reduction. The combined charge and burst labels distinguish the untied delivered-state model from the [tied receivers](https://github.com/GoGoKo699/Quantum-Magic-Burst-Routing), where physically measured comparisons reveal relative burst parities.

[Scientific account](README.md) · [Finite checks](../verification/README.md)
