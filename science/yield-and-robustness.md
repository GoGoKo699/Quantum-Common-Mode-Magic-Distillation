# Yield and phase mismatch

## Pointwise yield bound

For sector $`q`$, let $`e_q`$ and $`o_q`$ be the squared norms in the even- and odd-weight strings. Each present basis string contributes $`2^{-n}`$. Every exact extraction protocol in the [source model](model.md) satisfies

```math
p_{\mathrm{succ}}(\theta)
\le \sum_{q:e_q+o_q>0}\frac{4e_qo_q}{e_q+o_q}
\qquad \text{for every allowed }\theta .
```

In particular, an imbalanced sector can contribute less than its total mass. A parity-homogeneous sector contributes zero.

To prove the bound, write $`v_q=E_q+\zeta O_q`$, with $`E_q,O_q`$ of even and odd support respectively. After removing a common real normalization, their entries are in $`\mathbb Q(i)`$. The field involution of $`\mathbb Q(i,\zeta)`$ that fixes $`i`$ and sends $`\zeta`$ to $`-\zeta`$ sends the sector to $`v_q^-=E_q-\zeta O_q`$ up to a common scalar. After rescaling a fine accepted Kraus operator $`K`$ to Gaussian-rational entries, apply the involution to its action on the sector. The [sector-wise exactness result](exact-extraction.md#converse-for-adaptive-circuits) gives $`K v_q`$ proportional to $`\lvert T\rangle`$. The involution gives $`K v_q^-`$ proportional to $`Z\lvert T\rangle`$. For this argument, use the unnormalized target with entries $`(1,\zeta)`$, so the scalar of proportionality lies in the field after normalization of the inputs and Kraus operator.

The combined map $`A\lvert\psi\rangle=(\langle T\rvert K\lvert\psi\rangle)_K`$ is a contraction because $`\sum_K K^\dagger K\le I`$. For a valid input $`\lvert\Psi(\theta)\rangle`$, its squared norm is the success probability. Since $`A v_q^-=0`$ for every sector, project the input onto the orthogonal complement of the span of the $`v_q^-`$ before applying the contraction. The comparison vectors on distinct sectors are orthogonal by their disjoint supports. In a single sector,

```math
\lVert v_q\rVert^2=e_q+o_q,\qquad
\langle v_q^-\mid v_q\rangle=e_q-o_q.
```

The squared norm of the projected vector there is

```math
e_q+o_q-\frac{(e_q-o_q)^2}{e_q+o_q}=\frac{4e_qo_q}{e_q+o_q}.
```

The unknown phase of each sector has unit modulus. Adding the contributions therefore gives the pointwise bound without averaging over the source.

If all $`n\ge 1`$ gain vectors are nonzero, any finite block has success at most $`1-2^{1-n}`$. Project the gains onto a generic real direction along which none vanish. The unique minimum and maximum projected charges occur at two distinct bit strings, each with mass $`2^{-n}`$. The bound excludes both masses. Thus exact deterministic extraction is impossible in a finite nonzero-gain block.

## Joint optimum for disjoint triples

Use $`L`$ triples, each consisting of the two-mode construction or another qualifying triple with nonzero gains. Assume that the charge of the combined block records each triple's charge separately. This holds if their phase parameters occupy disjoint coordinates in the linear source model. The partition into charge sectors then factors across triples.

In each triple the sole mixed-parity sector has balanced masses, with total mass $`1/4`$. Any product sector containing such a component has balanced aggregate even and odd masses. A product sector containing only homogeneous-parity components has one aggregate parity. As a result, the upper bound for the combined block is the total mass of the sectors in which at least one triple is mixed, or

```math
p_{\mathrm{succ}}(\theta)\le 1-\left(\frac34\right)^L .
```

Run the three-input receiver on each triple and return one accepted qubit whenever possible. Conditional on the unknown phases, the input state factors and each receiver succeeds with probability $`1/4`$. The resulting success probability attains the bound. The fixed attempt consumes $`3L`$ carriers, even if all tests fail. If one instead retains every accepted qubit, the output count has a binomial distribution with mean $`L/4`$.

The same separate receivers provide this achievable probability when the triples share nuisance coordinates. The proof of joint optimality above uses separate charge labels. In the shared-coordinate model, different tuples of per-triple charges can merge into the same charge sector, and a collective receiver can face a different optimization problem.

## Sensitivity to imperfect phase addition

For the three-input circuit, let $`\epsilon=\phi_1+\phi_2-\phi_3`$ be the residual phase. The accepted state has phase $`\pi/4+\epsilon`$, and its infidelity relative to $`\lvert T\rangle`$ is exactly

```math
1-F=\sin^2(\epsilon/2).
```

The parity acceptance remains $`1/4`$ because every equatorial product input has equal computational-basis probabilities. If $`\epsilon`$ fluctuates classically across attempts, the accepted ensemble therefore has the same residual-phase distribution as the incident ensemble. Its infidelity is $`(1-\operatorname{Re}\mathbb{E}e^{i\epsilon})/2\le \mathbb{E}[\epsilon^2]/4`$ when the second moment exists. The distributional condition concerns the residual phase itself. A small coefficient mismatch alone gives no small uniform error bound when the underlying unknown phase is unbounded. This analysis assumes equatorial inputs and ideal Clifford operations.
