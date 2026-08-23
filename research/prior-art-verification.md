# Prior-Art Verification Evidence

**Verification date:** 2026-08-22
**Scope:** Independent re-fetch of every arXiv, GitHub, and SSRN citation in `research/prior-art.md`.

This file supersedes the five-line summary in `research/prior-art-run.log`. That log
records only that "all search queries and source fetches succeeded" with no per-citation
evidence. The table below is the actual per-citation fetch record: identifier, claimed
value, fetched value, HTTP status, and verdict. Where `prior-art.md` disagreed with the
fetched metadata, the file was corrected (see "Prior-Art Fixes Applied" below); where a
URL was unresolvable or materially mismatched, it was deleted per the backlog rule of
deleting unresolvable entries rather than softening them.

## Commands used

```
curl -sL -o <id>.html https://arxiv.org/abs/<id>
grep -oE '<meta name="citation_title" content="[^"]*"' <id>.html
grep -oE '<meta name="citation_author" content="[^"]*"' <id>.html
grep -oE '<meta name="citation_date" content="[^"]*"' <id>.html

curl -sL -o <repo>.html https://github.com/<owner>/<repo>
curl -sL -o readme.md https://raw.githubusercontent.com/<owner>/<repo>/main/README.md

curl -sL https://doi.org/10.2139/ssrn.5189069
curl -sI https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5189069
```

A 4-second sleep was inserted between each arXiv request and a 2-second sleep between
each GitHub request, per arxiv.org's rate-limit behavior. The export.arxiv.org API was
not used (it returns 429 in this environment).

## arXiv citations

| arXiv ID | Claimed in prior-art.md | Fetched citation_title | Fetched date | HTTP | Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2311.07911 | "Instruction-Following Evaluation for Large Language Models" | Instruction-Following Evaluation for Large Language Models | 2023/11/14 | 200 | Match |
| 2507.02833 | "Generalizing Verifiable Instruction Following" | Generalizing Verifiable Instruction Following | 2025/07/03 | 200 | Match |
| 2510.07043 | "COMPASS: Benchmarking Constrained Optimization in LLM Agents" | COMPASS: Benchmarking Constrained Optimization in LLM Agents | 2025/10/08 | 200 | Match |
| 2503.16974 | "Assessing Consistency and Reproducibility in the Outputs of Large Language Models: Evidence Across Diverse Finance and Accounting Tasks"; authors J. Wang & V. X. Wang; March 2025 | Assessing Consistency and Reproducibility in the Outputs of Large Language Models: Evidence Across Diverse Finance and Accounting Tasks; Wang, Julian Junyan; Wang, Victor Xiaoqi | 2025/03/21 | 200 | Match |
| 2508.18427 | Title matched, but dated "Nov 2025" and authored "F. Dimino & K. B. Saxena" only | Tracing Positional Bias in Financial Decision-Making: Mechanistic Insights from Qwen2.5; Dimino, Fabrizio; Saxena, Krati; Sarmah, Bhaskarjit; Pasquali, Stefano | 2025/08/25 | 200 | **Mismatch (defect a): date was 3 months off, 2 co-authors (Sarmah, Pasquali) missing. Fixed in prior-art.md.** |
| 2601.15322 | "Replayable Financial Agents: A Determinism-Faithfulness Assurance Harness for Tool-Using LLM Agents"; R. Khatchadourian; Jan 2026 | Replayable Financial Agents: A Determinism-Faithfulness Assurance Harness for Tool-Using LLM Agents; Khatchadourian, Raffi | 2026/01/17 | 200 | Match |
| 2606.31522 | "FinPersona-Bench: Longitudinal Psychometric Stability of Autonomous Financial Agents" | FinPersona-Bench: A Benchmark for Longitudinal Psychometric Stability of Autonomous Financial Agents | 2026/06/30 | 200 | **Mismatch: title in prior-art.md dropped "A Benchmark for". Fixed in prior-art.md.** |
| 2608.09988 | "OpenPM: Auditable Point-in-Time Evaluation for LLM Portfolio-Management Agents" | OpenPM: Auditable Point-in-Time Evaluation for LLM Portfolio-Management Agents | 2026/08/06 | 200 | Match |
| 2605.16895 | "The Alpha Illusion: Reported Alpha from LLM Trading Agents Should Not Be Treated as Deployment Evidence"; Y. Ye et al.; May 2026 | The Alpha Illusion: Reported Alpha from LLM Trading Agents Should Not Be Treated as Deployment Evidence; Ye, Yuxuan (+9 co-authors) | 2026/05/16 | 200 | Match |
| 2603.00285 | "TraderBench: How Robust Are AI Agents in Adversarial Capital Markets?"; Feb 2026 | TraderBench: How Robust Are AI Agents in Adversarial Capital Markets?; Yuan, Xiaochuang et al. | 2026/02/27 | 200 | Match |
| 2608.00991 | "SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling"; Aug 2026 | SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling | 2026/08/02 | 200 | Match |
| 2604.18373 | "Dissecting AI Trading: Behavioral Finance and Market Bubbles"; S. Ouyang & P. Sui; April 2026 | Dissecting AI Trading: Behavioral Finance and Market Bubbles; Ouyang, Shumiao; Sui, Pengfei | 2026/04/20 | 200 | Match |
| 2607.11141 | "NextFund: A Unified Performance Tracking Platform for Agentic Portfolio Management"; July 2026 | NextFund: A Unified Performance Tracking Platform for Agentic Portfolio Management | 2026/07/13 | 200 | Match |

All 13 unique arXiv IDs cited in `prior-art.md` (2601.15322 and 2605.16895 are each cited
twice, once per table) return HTTP 200 and resolve to real papers. Two title/date/author
mismatches were found and fixed (2508.18427, 2606.31522); the rest matched exactly.

## GitHub repositories

| URL | HTTP | Verdict |
| :--- | :--- | :--- |
| github.com/ibm-client-engineering/output-drift-financial-llms | 200 | Resolves, kept as-is |
| github.com/usmansafdarktk/FinPersona-Bench | 200 | Resolves, kept as-is |
| github.com/aslcai/OpenPM-Bench | 200 | Resolves, kept as-is |
| github.com/sunnytqin/compass | 200 | Resolves, kept as-is |
| github.com/allenai/IFBench | 200 | Resolves, kept as-is |
| github.com/google-research/google-research | 200 | Resolves, kept as-is |
| github.com/hj1650782738/Trading | **404** | **Unresolvable (defect b): deleted from prior-art.md per the backlog rule. The arXiv:2605.16895 citation for the same paper is intact.** |
| github.com/yxc20089/TraderBench | 200 | **Resolves, but its README (fetched via raw.githubusercontent.com) describes an AgentBeats/A2A "Green Agent"/"Purple Agent" competition submission (2nd place, AgentBeats Competition, Feb 2026), not the paper's own benchmark framing used in prior-art.md's description (defect c). Dropped the repo URL and kept only the arXiv:2603.00285 citation, since correcting the description to match the repo would require describing a different artifact (a competition submission) than the row is actually about (the paper).** |

## SSRN

| Identifier | HTTP | Verdict |
| :--- | :--- | :--- |
| doi.org/10.2139/ssrn.5189069 | 403 | Cloudflare bot-block (`cf-ray` header present), reproduced with both a plain and a browser-spoofed User-Agent. This is SSRN's standard anti-scraping behavior, not evidence the paper/listing does not exist - the same paper's arXiv mirror (2503.16974) is independently verified above with matching title, authors, and date. Left as-is in prior-art.md; not treated as an unresolvable/dead link. |

## Prior-Art Fixes Applied

1. **arXiv:2508.18427** (Dimino & Saxena) - corrected date from "Nov 2025" to "Aug 2025"
   and added missing co-authors Sarmah and Pasquali (Category 3 table).
2. **arXiv:2605.16895 GitHub link** - removed the dead `github.com/hj1650782738/Trading`
   URL from the Category 1 table; the arXiv citation and paper-derived description remain.
   Row title changed from "Trading / The Alpha Illusion" to "The Alpha Illusion" and
   "Active (May 2026)" changed to "Published (May 2026)" since there is no longer a repo
   whose activity is being tracked.
3. **arXiv:2603.00285 GitHub link** - removed the `github.com/yxc20089/TraderBench` URL
   from the Category 1 table for the reason in the GitHub table above; same title/date
   wording change as (2).
4. **arXiv:2606.31522** - corrected title from "FinPersona-Bench: Longitudinal
   Psychometric Stability of Autonomous Financial Agents" to "FinPersona-Bench: A
   Benchmark for Longitudinal Psychometric Stability of Autonomous Financial Agents"
   (Category 3 table) to match the paper's actual title.

## Not changed, flagged for awareness

- Category 1's "Activity / Date" column for FinPersona-Bench reads "Active (July 2026)"
  while the paper's own citation_date is 2026/06/30 (June 2026). This column describes
  GitHub repository activity, not the paper's publication date, and no independent commit
  timestamp was fetched to confirm or refute "July 2026" - left as-is, consistent with
  `prior-art.md`'s own "Moderately Sourced / Inferred" confidence note on repo commit
  activity (Section 8).
