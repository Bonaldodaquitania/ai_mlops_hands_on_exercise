# Ground Rules

## General rules

Your Git history is part of what instructors review, so commit often and tag each task when its timebox ends.

- **Timeboxes are real.** When time is up, commit, tag and stop, even if the work is unfinished;
- **Commit often (at least every 30 minutes)**, use short commit messages, try to follow [standards](https://www.conventionalcommits.org/en/v1.0.0/);
- **Tag the end of each task** as `task[task number]` and push the tag;
- **Part 1 ends with a pushed `task2` tag.** Improving your project between the parts or go back and explore other techniques is welcome but not required;
- **Ask for hints any time.** Hints are noted on your profile to show where you got stuck, not as a penalty.
- **Write in English**: code comments, reports, README and attachments.
- **Any language, framework or library is allowed**, as long as you meet the task goals. Setup guides are provided only for the core tools in this document.

## Using AI assistants

Use AI for lookups and repetitive boilerplate; design, analysis and core code are yours. There is no grade to protect, and in your presentation you must explain and justify every choice, so outsourcing the thinking gains you nothing.

| Area | Fine to use AI | Do it yourself |
| --- | --- | --- |
| Lookup | API and syntax questions ("pandas resample signature", "kubectl flag for X"), reading error messages | Asking how to solve the task |
| Boilerplate | Plot styling, YAML indentation fixes, argparse/CLI scaffolding, docstrings, `.gitignore`, Makefile targets | Whole Dockerfiles, Kubernetes manifests or Compose files |
| Task 1 | Formatting tables and figures, colour palettes, layout CSS | Choosing what to analyse, analysis code, insights, what to present and how |
| Task 2 | Explaining an error from `kubectl describe` or Docker, Dockerfile structure and unusual fields | Design, deployment, trade-off summary |
| Task 3 | Explaining a library error, turning a training log into a table, a toy front-end, formatting test questions | Model choice, training loop, feature engineering, evaluation, agent tools, prompt design |
| Task 4 | Formatting and grammar/spelling checks | README, design notes (ADRs) and presentation content |

**Log every use in `AI_LOG.md`**, one line each: time, purpose, what you kept. It tells instructors what you find tedious or hard, which shapes what is taught next.

```markdown
| Time  | Purpose                                   | Kept                         |
|-------|-------------------------------------------|------------------------------|
| 10:42 | Meaning of CrashLoopBackOff in my pod     | Fixed wrong CMD path myself  |
| 11:15 | Seaborn colour palette for 12 categories  | Used suggested palette       |
```
