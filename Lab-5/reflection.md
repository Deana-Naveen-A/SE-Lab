# Reflection

The handout PDF I was given does not list the four reflection questions. These are the usual ones. Replace the headings with the exact wording from your handout if it differs.

**1. Which issues were the easiest and hardest to fix?**
The easiest were the style and cleanup items (unused import, naming, blank lines, line length), since the tools say exactly what to change. The hardest was the SQL injection. The fix was small (`?` placeholders), but I had to understand why string concatenation is dangerous before I trusted it. The `shell=True` call was also a judgment call: I decided the notice only needed `print()`, so the subprocess could go entirely.

**2. Did the tools report any false positives or issues you disagreed with?**
Not really false positives, but some findings were low value. Bandit flagged the unused `CURATOR_PASSWORD` as a hardcoded password (correct, but harmless since it was unused). Pylint's missing-docstring warnings are about convention, not behavior. I fixed everything instead of suppressing with `# nosec` or `# pylint: disable`, because suppressing hides the problem rather than removing it.

**3. How would you integrate static analysis into a real workflow?**
Run Flake8 and Pylint as a pre-commit hook and in CI on every pull request, and run Bandit in CI with a fail-on-medium-or-higher rule. Teams can set a minimum Pylint score so quality does not drift down.

**4. What tangible improvements did you see in code quality, security and robustness?**
Pylint went from 4.85 to 10.00, Bandit from 5 findings to none, and Flake8 from 8 warnings to 0. Beyond the scores, the code is safer (no injection, no shell, no embedded secret) and more robust: `display_status` no longer crashes on a missing id, and a title containing an apostrophe is now stored correctly. Importing the module no longer runs the demo.
