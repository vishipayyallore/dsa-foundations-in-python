# S.M.A.R.T. Prompt Framework for DSA Foundations in Python

Framework for creating high-quality coding agent instructions for this DSA learning repository.

---

## The S.M.A.R.T. Framework

- **S** – Specific Role (e.g. Python DSA implementer, interview-style problem solver)
- **M** – Mission-critical requirements (measurable outcomes: correctness, complexity, tests)
- **A** – Audience (learners, interview prep, engineers strengthening foundations)
- **R** – Response format (code structure, docstrings, complexity comments, tests)
- **T** – Task constraints (Python 3.12+, PEP 8, zero-copy, no external solution paste)

---

## DSA-Specific Alignment

When creating prompts for this repo:

- **Content type**: Data structure implementation, algorithm, or problem solution
- **Module**: One of 01_complexity_analysis … 07_hashing_and_problem_patterns
- **Requirements**: Type hints, docstrings, time/space complexity comments, edge cases, tests

## Problem Statement Template

```markdown
## ROLE

You are implementing [data structure / algorithm / problem] for the DSA Foundations in Python repository.

## MISSION

[Clear objective, e.g. implement X with O(n) time and O(1) space, with tests]

## CONSTRAINTS

- Python 3.12+, PEP 8, type hints, docstrings
- Zero-copy: original implementation only
- Include complexity analysis and edge-case handling

## SUCCESS CRITERIA

- Implementation in correct module folder
- Tests in tests/ with happy path and edge cases
- black, isort, flake8 pass
```

## Role Examples for This Repo

**Data structure implementation:**

- Implement core operations with complexity comments; add tests and usage example in docstring.

**Algorithm / problem solution:**

- Provide brute-force and optimized approach; document time/space complexity; add tests and edge cases.

**Critical constraints:**

- Use Python 3.12+ only. Do not copy solutions from external sites. Follow PEP 8 and repository file-naming conventions.

## PR Success (this repo)

- `pytest` passes (with `--cov=src` if applicable)
- `black .` and `isort .` applied
- `flake8` clean
- Zero-copy policy followed; complexity analysis included where applicable
