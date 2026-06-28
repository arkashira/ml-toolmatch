# breakeven.md  

## 1. Cost per Active User (USD / month)

| Resource | Assumption per active user | Unit cost | Monthly cost |
|----------|---------------------------|-----------|--------------|
| **Compute** (CPU‑seconds for recommendation engine) | 2 k CPU‑seconds ≈ 0.02 h @ $0.05 / h (spot) | $0.05 / h | **$0.01** |
| **Storage** (profile + match data) | 5 GB @ $0.02 / GB (standard SSD) | $0.02 / GB | **$0.10** |
| **Bandwidth** (API responses, UI assets) | 10 GB outbound @ $0.05 / GB | $0.05 / GB | **$0.50** |
| **Support / SaaS overhead** (ticket triage, monitoring) | flat allocation | – | **$0.20** |
| **Total variable cost / active user** | – | – | **$0.81** |

> *Variable cost excludes salaries, marketing, and other fixed overhead.*

---

## 2. Pricing Tiers  

| Tier | Monthly price (USD) | Core features | Typical user profile |
|------|---------------------|---------------|----------------------|
| **Starter** | **$29** | • Basic tool‑matching questionnaire  <br>• Up to 1 k recommendation API calls <br>• Community‑only support | Early‑stage (pre‑Series A) teams, < 5 engineers |
| **Growth** | **$79** | • All Starter features <br>• Advanced scoring & cost‑benefit analysis <br>• Up to 10 k API calls <br>• Email support with SLA 24 h | Series A‑B teams, 5‑15 engineers |
| **Enterprise** | **$199** | • All Growth features <br>• Unlimited API calls <br>• Dedicated account manager <br>• Custom integration scripts & on‑prem data residency <br>• 99.9 % SLA | Series B+ / later, >15 engineers, compliance needs |

---

## 3. Customer Acquisition Cost (CAC)

| Channel | CAC (USD) | Notes |
|---------|-----------|-------|
| Content + SEO (organic) | **$150‑$250** | Low‑touch, longer sales cycle |
| Paid LinkedIn / Google ads | **$250‑$500** | Targeted at ML leads, conversion ~2 % |
| Enterprise sales (direct outreach) | **$600‑$900** | Includes demo & negotiation time |

*We will target a blended CAC of **$300 ± $100** for the first 12 months.*

---

## 4. Lifetime Value (LTV)

Assumptions  

* Monthly churn = **5 %** (average across tiers) → average lifetime = 1 / 0.05 = **20 months**  
* Mix of paying customers (observed pilot): 60 % Starter, 30 % Growth, 10 % Enterprise  

**Weighted ARPU**  

\[
\text{ARPU} = 0.6 \times 29 + 0.3 \times 79 + 0.1 \times 199 = 61.0\ \text{USD/mo}
\]

**LTV**  

\[
\text{LTV} = \text{ARPU} \times \text{Lifetime} = 61.0 \times 20 = \mathbf{1{,}220\ USD}
\]

*Net LTV after CAC (mid‑range CAC $300) ≈ $920.*

---

## 5. Break‑Even Users Count  

### Fixed monthly overhead (estimated)

| Cost item | Monthly cost (USD) |
|-----------|-------------------|
| Engineering (2 senior devs) | 16,000 |
| Product / PM | 6,000 |
| Cloud infrastructure (reserved) | 2,000 |
| General & admin (legal, office, tools) | 6,000 |
| **Total Fixed** | **30,000** |

### Contribution margin per user  

\[
\text{Contribution} = \text{Weighted ARPU} - \text{Variable cost} = 61.0 - 0.81 = 60.19\ \text{USD}
\]

### Break‑Even Users  

\[
\frac{30{,}000}{60.19} \approx \mathbf{498\ users}
\]

*At ~500 paying users (mix as above) the business covers all fixed costs.*

---

## 6. Path to $10 K MRR  

| Tier | Users needed for $10 K MRR | Monthly revenue |
|------|----------------------------|-----------------|
| **Starter** ($29) | **345** | $29 × 345 = **$10,005** |
| **Growth** ($79) | **127** | $79 × 127 = **$10,033** |
| **Enterprise** ($199) | **51** | $199 × 51 = **$10,149** |
| **Mixed** (60 % S, 30 % G, 10 % E) | **~210** (126 S, 63 G, 21 E) | 126×29 + 63×79 + 21×199 = **$10,017** |

**Strategic focus:**  
* Acquire 150 Starter users + 40 Growth users + 10 Enterprise users within the first 3 months → $10.5 K MRR, surpassing the break‑even threshold with a comfortable safety margin.

---  

**Takeaway:** With a modest variable cost of $0.81 per active user, a blended CAC around $300, and a weighted ARPU of $61, the product needs roughly **500 paying customers** to become cash‑neutral. Reaching **$10 K MRR** can be achieved with a realistic mix of 200‑350 users across the three tiers, providing a clear early‑stage growth target.  