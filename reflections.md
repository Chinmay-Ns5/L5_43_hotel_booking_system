# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it important?

Static code analysis is the process of examining source code without executing the program to identify potential bugs, security vulnerabilities, and coding standard violations. It is important because it helps developers detect problems early, improve code quality, enhance security, and make software easier to maintain.

## 2. What is the difference between Pylint, Bandit, and Flake8?

- **Pylint:** Checks code quality, naming conventions, unused variables, missing docstrings, and potential programming errors.
- **Bandit:** Identifies potential security vulnerabilities and unsafe coding practices in Python programs.
- **Flake8:** Checks Python code for style violations, formatting issues, unused imports, and other linting errors.

Using all three tools provides broader coverage of code quality, security, and maintainability.

## 3. What issues were identified and how were they fixed?

The original hotel booking program contained several issues, including a mutable default argument, broad exception handling, unsafe use of `eval()`, weak MD5 hashing, shell command execution using `os.system()`, a hardcoded secret, and improper file handling. These were addressed by using a `None` default, removing unnecessary exception handling, using a numeric multiplier instead of `eval()`, replacing MD5 with SHA-256, removing shell execution and the hardcoded secret, and using a file context manager with UTF-8 encoding.

## 4. How did static analysis improve the program?

Static analysis helped identify and correct issues that could affect security, reliability, readability, and maintainability. After the corrections, the Pylint score improved from 5.32/10 to 10.00/10. Bandit reported no issues, and Flake8 produced no error output. The program also executed successfully after the changes.

## Conclusion

This lab demonstrated how static analysis tools can improve Python code quality and security without executing the code during analysis. Using Pylint, Bandit, and Flake8 together helped identify different categories of issues and verify that the corrections improved the program.
