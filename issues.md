# Lab 5 — Static Code Analysis Issue Log

| Issue | Type | Original line(s) | Description | Fix Approach |
|---|---|---|---|---|
| Mutable default argument | Bug | 15 | A list default could be shared between function calls. | Used `None` and initialized a new list inside the function. |
| Broad exception handling | Code quality | 24–27 | A bare exception and `pass` hid failures. | Removed the unnecessary exception handler and checked room existence. |
| Unsafe `eval()` | Security | 42 | Evaluated a string as Python code. | Replaced it with a numeric seasonal multiplier. |
| Weak MD5 hashing | Security | 47 | MD5 is unsuitable for security-sensitive hashing. | Replaced it with SHA-256 for a general-purpose digest. |
| Shell command execution | Security | 58–59 | Used `os.system()` to print a message. | Replaced shell execution with Python `print()`. |
| Hardcoded secret | Security | 62–70 | Embedded and printed a secret token in the program. | Removed the hardcoded secret and its output. |
| File handling | Code quality | 55–57 | File handling lacked a context manager and explicit encoding. | Used `with open(...)` and UTF-8 encoding. |
| Style and maintainability | Code quality | Multiple | Unused imports, naming, missing docstrings and formatting issues. | Improved naming, documentation and formatting. |

## Verification

- Pylint: 5.32/10 before; 10.00/10 after.
- Bandit: Findings before; no issues identified after.
- Flake8: Seven reported violations before; no output after.

