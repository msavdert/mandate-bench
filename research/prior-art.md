# Prior-Art Report: LLM Portfolio Agent Consistency and Mandate Compliance Benchmarking

**Date:** 2026-08-21  
**Target Scope:** Prior art evaluating Large Language Model (LLM) agents on (a) run-to-run decision consistency (allocation dispersion over $N$ repeated trials on identical prompt snapshots) and (b) mandate compliance (violation rates of hard numeric constraints: max position size, min cash, max turnover).

---

## 1. Executive Summary

Existing financial AI benchmarks focus overwhelmingly on either (1) financial knowledge QA/exam scores (e.g., CFA/FinBen), (2) backtested or live PnL/Sharpe trading performance (e.g., FinTrade, NextFund, OpenPM), or (3) multi-step tool-use execution.

A critical gap exists at the intersection of **continuous portfolio allocation, stochastic run-to-run variance, and deterministic numeric mandate compliance**:
1. **Consistency Evaluation:** While general LLM output drift and discrete financial classification consistency have been studied (e.g., IBM's DFAH, Wang & Wang 2025), no existing benchmark measures continuous allocation dispersion ($\text{Var}(w_i)$ across repeated runs on frozen portfolio snapshots).
2. **Mandate Compliance:** Most trading agents rely on deterministic external wrapper scripts or post-hoc portfolio optimizers to force constraint satisfaction rather than evaluating the LLM's intrinsic ability to follow continuous numerical allocation mandates.
3. **Leaderboards:** There is currently **zero** public recurring leaderboard tracking per-model compliance rates or decision consistency for portfolio-rebalancing agents.

---

## 2. Category 1: GitHub Projects Measuring Variance, Consistency, and Reproducibility in Financial Agents

| Project / Repository | Repository URL & Reference | Core Functionality | Activity / Date | Key Differences from Mandate-Bench Design |
| :--- | :--- | :--- | :--- | :--- |
| **DFAH (Determinism-Faithfulness Assurance Harness)** | [ibm-client-engineering/output-drift-financial-llms](https://github.com/ibm-client-engineering/output-drift-financial-llms)<br>Paper: [arXiv:2601.15322](https://arxiv.org/abs/2601.15322) | Evaluates trajectory determinism, decision determinism, and evidence-conditioned faithfulness across 74 configurations (12 models, 4 providers, 8–24 runs at $T=0.0$). | Active (Jan 2026) | Evaluates discrete classification choices (`approve`/`reject`/`modify`) on pre-proposed single trades via tool calls, rather than continuous asset weight generation ($\mathbf{w} \in \mathbb{R}^K$) and allocation variance across repeated prompts. |
| **FinPersona-Bench** | [usmansafdarktk/FinPersona-Bench](https://github.com/usmansafdarktk/FinPersona-Bench)<br>Paper: [arXiv:2606.31522](https://arxiv.org/abs/2606.31522) | Measures "Mandate Salience Decay" (MSD) across 18 LLMs over a 200-day sequential simulation across synthetic market regimes (bubble, crash, flat). | Active (July 2026) | Measures longitudinal degradation over cumulative conversational context (200 sequential trading days) rather than single-snapshot stochastic dispersion across $N$ independent runs. |
| **OpenPM-Bench** | [aslcai/OpenPM-Bench](https://github.com/aslcai/OpenPM-Bench)<br>Paper: [arXiv:2608.09988](https://arxiv.org/abs/2608.09988) | Auditable point-in-time portfolio evaluation framework managing a $1M long-only book over S&P 500 at 5-minute intervals. | Active (Aug 2026, commit `ed2e88c`) | Uses a deterministic programmatic critic to *enforce* feasibility before order execution and benchmarks cost-aware backtested returns rather than unconstrained raw LLM mandate violation rates. |
| **Trading / The Alpha Illusion** | [hj1650782738/Trading](https://github.com/hj1650782738/Trading)<br>Paper: [arXiv:2605.16895](https://arxiv.org/abs/2605.16895) | Reproduction harness auditing structural validity, friction modeling, and lookahead contamination in LLM trading agents. | Active (May 2026) | Focuses on backtest validity and cost-model auditing for trading agents, rather than benchmarking prompt-to-prompt allocation dispersion and constraint violation frequencies. |
| **TraderBench** | [yxc20089/TraderBench](https://github.com/yxc20089/TraderBench)<br>Paper: [arXiv:2603.00285](https://arxiv.org/abs/2603.00285) | Evaluates LLM trading agents in adversarial capital markets, options trading, and risk management scenarios. | Active (Feb 2026) | Focuses on multi-agent game-theoretic market dynamics and options pricing rather than static portfolio rebalancing under explicit numerical constraints. |

*Negative Result:* No open-source GitHub project was found whose primary benchmark metric is repeated-trial allocation vector dispersion ($\text{Var}(w_i)$ across $N$ identical prompt rollouts) on a fixed static portfolio snapshot.

---

## 3. Category 2: Constraint and Mandate Compliance Benchmarks (Finance & General)

| Benchmark / Repo | URL & Reference | Core Functionality | Activity / Date | Key Differences from Mandate-Bench Design |
| :--- | :--- | :--- | :--- | :--- |
| **COMPASS** | [sunnytqin/compass](https://github.com/sunnytqin/compass)<br>Paper: [arXiv:2510.07043](https://arxiv.org/abs/2510.07043) | Evaluates multi-turn planning agents on constrained optimization (budget limits, dates, occupancy) across 281 tasks and 18 APIs. | Active (Oct 2025) | Evaluates travel booking catalog selection under budget caps, not continuous fractional asset allocation or portfolio turnover/concentration constraints. |
| **SCHEDBench** | Paper: [arXiv:2608.00991](https://arxiv.org/abs/2608.00991) | Evaluates LLM constraint faithfulness in natural-language combinatorial scheduling problems. | Active (Aug 2026) | Evaluates discrete combinatorial job/slot assignment constraints rather than continuous numerical finance mandates. |
| **IFBench / IFEval** | [allenai/IFBench](https://github.com/allenai/IFBench) / [google-research/ifeval](https://github.com/google-research/google-research/tree/master/instruction_following_eval)<br>Papers: [arXiv:2507.02833](https://arxiv.org/abs/2507.02833), [arXiv:2311.07911](https://arxiv.org/abs/2311.07911) | Rule-based verifiable evaluation of instruction following (word counts, punctuation, JSON formatting, negative constraints). | Active (July 2025 / Nov 2023) | Focuses on structural and lexical text generation constraints rather than continuous numerical simplex balance ($\sum w_i = 1$) or financial boundary rules. |
| **DFAH Portfolio Benchmark** | [ibm-client-engineering/output-drift-financial-llms](https://github.com/ibm-client-engineering/output-drift-financial-llms)<br>Paper: [arXiv:2601.15322](https://arxiv.org/abs/2601.15322) | 50 test cases checking proposed trades against concentration limits (>5%), sector caps (>25%), liquidity, and cash reserve (>2%). | Active (Jan 2026) | Implemented as a binary classification / trade validation task against proposed external trades, rather than evaluating an LLM's own generated portfolio rebalancing allocations. |

*Negative Result:* No existing constraint benchmark evaluates portfolio-specific rebalancing mandates (e.g., simultaneous bounding of single-name weights $w_i \le c_{\max}$, portfolio cash reserve $w_{\text{cash}} \ge c_{\text{cash}}$, and two-way turnover $\sum |w_i - w_{i,0}| \le c_{\text{turnover}}$) on continuous allocation vectors.

---

## 4. Category 3: Academic Literature on Behavioral Metrics, Consistency & Reasoning-Action Gap (2024–2026)

| Paper Title | Authors & Date | Sourced Metrics & Key Findings | URL | Distinction from Mandate-Bench |
| :--- | :--- | :--- | :--- | :--- |
| **Assessing Consistency and Reproducibility in the Outputs of LLMs: Evidence Across Diverse Finance and Accounting Tasks** | J. Wang & V. X. Wang (March 2025) | Evaluates output consistency across classification, information extraction, and numerical accounting tasks over repeated runs. Finds near-perfect reproducibility for binary classification, but substantial variance on complex numerical extraction. | [SSRN:5189069](https://doi.org/10.2139/ssrn.5189069)<br>[arXiv:2503.16974](https://arxiv.org/abs/2503.16974) | Evaluates NLP extraction and accounting categorization tasks; does not evaluate portfolio rebalancing or numerical investment mandates. |
| **Replayable Financial Agents: A Determinism-Faithfulness Assurance Harness for Tool-Using LLM Agents** | R. Khatchadourian (Jan 2026) | 7–20B models achieved 100% determinism at $T=0.0$ on baselines, but 120B+ models required $3.7\times$ larger validation samples; reports positive correlation ($r=0.45, p<0.01, n=51$) between determinism and faithfulness. | [arXiv:2601.15322](https://arxiv.org/abs/2601.15322) | Formulates portfolio checks as tool-calling trade classification (`approve`/`reject`), not direct continuous allocation synthesis. |
| **FinPersona-Bench: Longitudinal Psychometric Stability of Autonomous Financial Agents** | M. U. Safder et al. (June 2026) | Evaluates 18 LLMs across 200 trading days. In crash scenarios, the behavioral gap between static agents and mandate-regrounded agents grows $4.4\times$ from Q1 to Q4. | [arXiv:2606.31522](https://arxiv.org/abs/2606.31522) | Evaluates longitudinal behavioral decay over multi-turn simulation history rather than single-turn prompt-to-prompt allocation dispersion. |
| **The Alpha Illusion: Reported Alpha from LLM Trading Agents Should Not Be Treated as Deployment Evidence** | Y. Ye et al. (May 2026) | Demonstrates that extended thinking helps retrieval but fails to improve numerical execution of P&L/Greeks; models exhibit severe "Parametric Prior Lock-in" where weights hide undisclosed factor exposures. | [arXiv:2605.16895](https://arxiv.org/abs/2605.16895) | Qualitative and structural critique of backtest claims rather than a standardized quantitative benchmark for mandate compliance. |
| **Dissecting AI Trading: Behavioral Finance and Market Bubbles** | S. Ouyang & P. Sui (April 2026) | Identifies human-like cognitive biases in LLM traders (disposition effect, recency-weighted extrapolation) using a 20-mechanism behavioral scoring framework in simulated auctions. | [arXiv:2604.18373](https://arxiv.org/abs/2604.18373) | Measures auction market dynamics and emergent bubble formation rather than individual portfolio constraint adherence. |
| **Tracing Positional Bias in Financial Decision-Making** | F. Dimino & K. B. Saxena (Nov 2025) | Demonstrates systematic sensitivity to irrelevant prompt context (ticker ordering and token sequence) in financial decision models. | [arXiv:2508.18427](https://arxiv.org/abs/2508.18427) | Analyzes input-order bias on discrete asset selection rather than continuous portfolio allocation variance and rule bounds. |

---

## 5. Category 4: Public Leaderboards and Recurring Reports

| Leaderboard / Report | Organization & URL | Metrics Tracked | Update Cadence | Key Differences from Mandate-Bench Design |
| :--- | :--- | :--- | :--- | :--- |
| **Open Financial LLM Leaderboard (FinBen)** | FinOS Foundation / Open-Finance-Lab<br>[Leaderboard Space](https://huggingface.co/spaces/finosfoundation/Open-Financial-LLM-Leaderboard)<br>[Docs](https://finllm-leaderboard.readthedocs.io/) | Evaluates ~30 LLMs across ~50 tasks covering CFA exam QA, SEC filing extraction, and FinTrade cumulative returns/Sharpe. | Periodic / Model Submissions | Tracks financial NLP and backtested trading Sharpe/returns; does **not** track run-to-run decision variance or numeric mandate violation rates. |
| **NextFund Arena** | Paradoox AI Research<br>[NextFund Demo](https://paradoox.cn/nextfund/)<br>Paper: [arXiv:2607.11141](https://arxiv.org/abs/2607.11141) | Live trading arena tracking equity curves, PnL, Sharpe, and intermediate multi-agent deliberation traces across HK, US, and China A-shares. | Live / Continuous | Ranks models by market PnL and displays qualitative justifications; does not evaluate single-snapshot repeated allocation consistency or mandate violation rates. |
| **Aider LLM Leaderboard** *(Adjacent)* | Aider.chat<br>[Aider Leaderboard](https://aider.chat/docs/leaderboards/) | Tracks instruction-following and code edit syntax compliance (diff application success) across model releases. | Updated per major LLM release | Code editing domain; measures code syntax adherence, not portfolio math or financial risk constraints. |
| **Open LLM Leaderboard v2** *(Adjacent)* | Hugging Face<br>[Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | IFEval (verifiable instruction following), BBH, MATH, GPQA, MuSR, MMLU-PRO. | Continuous | Tracks general text instruction formatting and academic reasoning; contains no financial mandate or allocation consistency metrics. |

*Negative Finding:* As of August 2026, there is **no** public leaderboard or recurring report tracking per-model mandate compliance or run-to-run decision consistency in financial or resource-allocation tasks.

---

## 6. Category 5: Adjacent General Benchmarks (Reusability Assessment)

| Candidate Benchmark | Repository / Source | Architectural Reusability | Domain Fit for Portfolio Rebalancing | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **IFEval / IFBench** | [allenai/IFBench](https://github.com/allenai/IFBench) | **High**: Clean rule-based evaluation harness with deterministic assertion checkers. | **Low**: Rule definitions are text-centric (word count, casing, regex, JSON syntax) and lack continuous numerical constraint logic. | **Adapt harness design only**: Write custom financial constraint evaluators ($\sum w_i = 1$, $w_i \le c_{\max}$, turnover, cash). |
| **COMPASS** | [sunnytqin/compass](https://github.com/sunnytqin/compass) | **Medium**: Multi-turn planning structure with hard constraint validation and soft preference scoring. | **Low**: Tailored to travel booking APIs (flights/hotels) rather than matrix/vector asset allocations. | **Do not reuse directly**: Domain mismatch is too large to adapt efficiently. |
| **DFAH (IBM)** | [ibm-client-engineering/output-drift-financial-llms](https://github.com/ibm-client-engineering/output-drift-financial-llms) | **High**: Python harness measuring run-to-run determinism across repeated trials ($N$ runs) at fixed temperature with code-based graders. | **Medium**: Already has a `Portfolio Constraint` benchmark module (50 test cases), but is structured for trade approval classification rather than allocation vector synthesis. | **Best foundational reference**: Extend DFAH's repeated-trial evaluation philosophy to continuous allocation vectors and mandate violation scoring. |

---

## 7. Comparative Feature Matrix

| Benchmark | Domain | Decision Output Type | Evaluates Run-to-Run Consistency ($N$ repeats)? | Evaluates Hard Numeric Mandate Compliance? | Pure LLM Decision (No Critic Enforcing Constraints)? |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **FinBen / FinTrade** | Finance | Trading actions / Returns | No | No | Yes |
| **OpenPM-Bench** | Finance | Portfolio weights / PnL | No | No *(critic enforces)* | No *(critic fixes violations)* |
| **NextFund** | Finance | Time-series trades / PnL | No | No | Yes |
| **FinPersona-Bench** | Finance | Target cash over 200 days | No *(measures longitudinal decay)* | Partially *(cash target drift)* | Yes |
| **DFAH (IBM)** | Finance | Trade Approve/Reject/Modify | **Yes** *(trajectory & decision determinism)* | Partially *(discrete trade limits)* | Yes |
| **COMPASS** | General | Travel itinerary / Bookings | No | **Yes** *(budget, occupancy)* | Yes |
| **IFEval / IFBench** | General NLP | Formatted text | No | **Yes** *(text formatting rules)* | Yes |
| **Mandate-Bench (Proposed)** | Finance | **Continuous Allocation Vector** ($\mathbf{w}$) | **Yes** *(variance across $N$ repeats on fixed snapshot)* | **Yes** *(max position, min cash, max turnover violation rates)* | **Yes** *(directly measures unassisted LLM compliance)* |

---

## 8. Confidence Assessment & Sourcing Audit

- **Well-Sourced Findings (High Confidence):**
  - Existence and exact metrics of IBM's DFAH (`arXiv:2601.15322`, Jan 2026), FinPersona-Bench (`arXiv:2606.31522`, July 2026), OpenPM-Bench (`arXiv:2608.09988`, Aug 2026), and The Alpha Illusion (`arXiv:2605.16895`, May 2026).
  - Absence of continuous portfolio allocation consistency metrics in the primary financial LLM leaderboards (Open Financial LLM Leaderboard / FinBen and NextFund).
  - General instruction-following benchmark mechanics (IFEval, IFBench, COMPASS).

- **Moderately Sourced / Inferred Findings (Medium Confidence):**
  - Exact commit activity on smaller GitHub repositories (`TraderBench`, `OpenPM-Bench` commit hashes) sourced from public index records as of August 2026.
  - Industry internal proprietary compliance testing practices (assumed non-public, as no open-source benchmark exists).

- **Negative Findings Confirmed (High Confidence):**
  - **No existing benchmark or public leaderboard** measures run-to-run allocation vector dispersion ($\text{Var}(w)$ over $N$ repeated prompt evaluations) combined with explicit numeric mandate violation rates (max position %, min cash %, max turnover %) on fixed market snapshots.
