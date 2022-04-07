# Loan Qualifier Application

This application allows the user to input basic financial information which outputs a lsting of qualified loans.

---

## Technologies

The application is coded via Python and uses fire and questionary databases.

---

## Installation Guide

pip install fire
pip install questionary
from pathlib import Path

---

## Usage

This is an example of how the loan qualifier application works.

? Enter a file path to a rate-sheet (.csv): data/daily_rate_sheet.csv
? What's your credit score? 750
? What's your current amount of monthly debt? 0
? What's your total monthly income? 10000
? What's your desired loan amount? 100000
? What's your home value? 300000
The monthly debt to income ratio is 0.00
The loan to value ratio is 0.33.
Found 15 qualifying loans
? Would you like to save the qualifying loans? Yes
? Enter a file path to save qualifying loans (.csv): data/qualifying_loans.csv

---

## Contributors

Application created by John Willis

---

## License

MIT
