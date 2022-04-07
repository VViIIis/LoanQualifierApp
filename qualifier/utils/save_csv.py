import csv
import string

import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import load_csv

from qualifier.utils.calculators import (
    calculate_monthly_debt_ratio,
    calculate_loan_to_value_ratio,
)

from qualifier.filters.max_loan_size import filter_max_loan_size
from qualifier.filters.credit_score import filter_credit_score
from qualifier.filters.debt_to_income import filter_debt_to_income
from qualifier.filters.loan_to_value import filter_loan_to_value

def save_csv():
    """Saves qualifying data as csv file"""
    csvpath = Path('data/daily_rate_sheet.csv')
    qualifying_loans = []
    with open(csvpath, newline='') as csvfile:
        rows = csv.reader(csvfile)
        header = next(rows)
        for row in rows:
            lender = string(row[0])
            max_loan_amount = int(row[1])
            max_ltv = float(row[2])
            max_dti = float(row[3])
            min_credit_score = int(row[4])
            interest_rate = float(row[5])

            qualifying_loan = {
                "lender": lender,
                "max_loan_amount": max_loan_amount,
                "max_ltv": max_ltv,
                "max_dti": max_dti,
                "min_credit_score": min_credit_score,
                "interest_rate": interest_rate
            }
            qualifying_loans.append(qualifying_loan)
        return qualifying_loans
     