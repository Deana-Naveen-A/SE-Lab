# Issues found in museum_catalog.py

Line numbers refer to the ORIGINAL file.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| SQL injection (Bandit B608, Medium) | Security | 11 | `addArtifact` builds the INSERT by concatenating `title` and `era`. A title like `O'Brien's Vase` breaks the query, and crafted input could alter it. | Use a parameterized query with `?` placeholders and pass a tuple. |
| `shell=True` subprocess (B602, B607, B404) | Security | 3, 37 | `subprocess.call("echo ...", shell=True)` starts a shell with a partial executable path, which is risky if the string ever contains input. | The "backup notice" only prints text, so replace it with `print()` and remove the `subprocess` import. |
| Hardcoded password (B105) | Security | 7 | `CURATOR_PASSWORD = "m4seum!"` is a secret committed to source, and it is never used. | Delete it. If needed later, read it from an environment variable. |
| Crash on unknown id | Bug | 15-19 | `displayStatus` does `row[0]` on `fetchone()`, which is `None` for a missing id, so it raises `TypeError`. | Check `row is None` and return `"not found"`. |
| Unused import (F401, W0611) | Quality | 2 | `datetime` is imported but never used. | Remove the import. |
| Unused argument (W0613) | Quality | 15 | `curator` is passed to `displayStatus` but never used. | Remove the parameter and update the caller. |
| Naming (C0103) | Style | 10, 15, 24, 31, 36 | camelCase function names violate snake_case. | Rename to `add_artifact`, `display_status`, `total_value`, `move_to_display`, `backup_note`. |
| Unnecessary else after return (R1705) | Quality | 17-19 | `else` after a `return` adds nesting for no reason. | De-indent the final `return`. |
| Missing docstrings (C0114, C0116) | Quality | 1, 10, 15, 24, 31, 36, 40 | No module or function docstrings. | Add short docstrings. |
| Line too long (E501, C0301) | Style | 6, 11, 16, 26, 32 | Lines exceed 79 characters. | Wrap the SQL strings and calls across lines. |
| Blank lines / spacing (E303, E225) | Style | 24, 25 | Three blank lines before a function, and `total=0` lacks spaces around `=`. | Use two blank lines and `total = 0`. |
| Module runs on import | Quality | 46 | `main()` is called unconditionally, so importing the file runs the demo. | Wrap in `if __name__ == "__main__":`. |

## Results

| Tool | Before | After |
|------|--------|-------|
| Pylint | 4.85/10 | 10.00/10 |
| Bandit | 1 Medium, 4 Low | No issues |
| Flake8 | 8 warnings | 0 warnings |
