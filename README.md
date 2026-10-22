# Lab 5 — Static Code Analysis

## Objective
To improve Python code quality, security, and maintainability using Pylint, Bandit, and Flake8.

## Project
This repository contains a hotel booking system analyzed using three static analysis tools. The identified issues were corrected, and the tools were rerun to verify the changes.

## Tools Used
- **Pylint:** Code quality and maintainability analysis.
- **Bandit:** Security vulnerability analysis.
- **Flake8:** Python style and formatting checks.

## Results
- **Pylint:** Final score of 10.00/10.
- **Bandit:** No issues identified in the final scan.
- **Flake8:** No reported violations in the final scan.

## Deliverables
- `hotel_booking_system.py` — corrected Python program.
- `pylint_report_before.txt` and `pylint_report_after.txt`
- `bandit_report_before.txt` and `bandit_report_after.txt`
- `flake8_report_before.txt` and `flake8_report_after.txt`
- `issues.md` — issue log and fixes.
- `reflections.md` — lab reflection.

## Run the Program
```bash
python hotel_booking_system.py
```

## Run Static Analysis
```bash
python -m pylint hotel_booking_system.py --score=y
python -m bandit hotel_booking_system.py
python -m flake8 hotel_booking_system.py
```
