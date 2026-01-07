
# Assistant Context

**Prohibition Notice:**
The use of `uv` for package management or installation is strictly prohibited in this repository. Always use `pip` for Python package management. Any PRs or scripts using `uv` will be rejected.

Use this manifest to refresh key repo context at the start of tasks.

## Pinned Files

- PROMPT.md
- README.md
- .gitignore
- git-helper.ps1
- setup.ps1
- scripts/task.ps1
- src/main.py
- tests/test_main.py
- TESTING.md

## Pinned Folders

- scripts/
- src/
- tests/


## Notes

- Make high-resolution git commits: commit frequently, with small and focused changes, to improve traceability and code review quality.

- Prefer `.venv\Scripts\python.exe` for Python runs.
- Use test-gated commits (`gctt`) when feasible.
- Do not commit secrets; use `.env` (ignored).
