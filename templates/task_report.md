# Task [N] report: [task name]

> **Guidance.** Copy this file to `reports/task[N].md` at the end of each task and fill it in as you go.
>
> - Replace every [placeholder]; delete every Guidance block before you tag.
> - Keep it short: one to three pages. Prefer tables and figures to prose.
> - Write in English, in your own words. Explain *why*; do not paste code the reader can open in the repository.
> - Every section ends with an **Evidence** line: a notebook cell, file path, test, commit or screenshot. A claim with no evidence counts as not done.
>
> What to focus on in sections 3 and 4:
>
> | Task | Focus on |
> | --- | --- |
> | 1. Exploratory data analysis | Data quality checks and fixes; main findings, each with a number; what each finding means for later tasks |
> | 2. App deployment | Architecture; image and configuration choices; how the app gets its data; deployment trade-offs |
> | 3. AI agent | Evaluation protocol and baseline; model choice; agent tools and prompt rules; example dialogues including one failure; deployment |
> | 4. Presentation | Overall architecture; decision log across all tasks; what you would change for production |

| Field | Value |
| --- | --- |
| Student | [name] |
| Dataset | [name] |
| Task | [1 / 2 / 3 / 4] |
| Tag / commit | [task[N] / short hash] |
| How to run | [commands; for secrets, name the environment variable, never the value] |
| Timebox | [time used; finished / unfinished] |

## 1. Summary

> **Guidance.** Write this last, in at most 150 words: what you built, the main result with a number, and the most important limitation.

[Your summary.]

## 2. Goal and success criteria

> **Guidance.** State what the task asked for and how you decide whether you succeeded. Fix the criteria before you look at results.

**Goal.** [One paragraph.]

| Criterion | How it is measured | Target | Result |
| --- | --- | --- | --- |
| [ ] | [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] | [ ] |

**Evidence:** [ ]

## 3. Approach and key decisions

> **Guidance.** Write each decision as *finding → decision → where it lives in the code*, and name the alternative you rejected. Add a diagram if the task has an architecture or a pipeline.

| # | Finding | Decision | Alternative considered | Where in the code |
| --- | --- | --- | --- | --- |
| D1 | [ ] | [ ] | [ ] | [file or module] |
| D2 | [ ] | [ ] | [ ] | [ ] |
| D3 | [ ] | [ ] | [ ] | [ ] |

[Optional diagram, with a one-sentence caption.]

**Evidence:** [ ]

## 4. Results

> **Guidance.** Every figure needs a one-sentence caption that states what it shows, with a number. Compare with a baseline or reference wherever one exists.

| Result | Value | Baseline or reference |
| --- | --- | --- |
| [ ] | [ ] | [ ] |
| [ ] | [ ] | [ ] |

[Figure, with a one-sentence caption.]

**Evidence:** [ ]

## 5. Problems and how you handled them

| Problem | Cause | What you did | Status |
| --- | --- | --- | --- |
| [ ] | [ ] | [ ] | [solved / workaround / open] |

**Evidence:** [ ]

## 6. Limitations and trade-offs

> **Guidance.** Be specific. "The model may be wrong" says nothing; "all errors were of one kind, with confidence below X" does.

| Area | Limitation or trade-off | Impact | Mitigation or next step |
| --- | --- | --- | --- |
| [data / model / app / agent / operations] | [ ] | [ ] | [ ] |

**Evidence:** [ ]

## 7. Next steps

| Priority | Next step | Why | Effort |
| --- | --- | --- | --- |
| 1 | [ ] | [ ] | [S / M / L] |
| 2 | [ ] | [ ] | [ ] |

## 8. Use of AI assistants

> **Guidance.** Summarise your `AI_LOG.md` for this task. You must be able to explain any code or text you submit, whoever or whatever drafted it.

| Tool | What you used it for | Where (files or sections) | How you checked the output |
| --- | --- | --- | --- |
| [ ] | [ ] | [ ] | [tests, review, manual check] |

[One or two sentences: where did an assistant mislead you, and how did you notice?]

## Checklist

- [ ] Task tag pushed and named in the table at the top
- [ ] Runs from a fresh clone with the commands above
- [ ] No secrets, API keys or large data files committed
- [ ] Every section has an Evidence line
- [ ] Every figure has a caption with a number
- [ ] Guidance blocks and placeholders removed
- [ ] `AI_LOG.md` up to date
