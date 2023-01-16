import os
#import requests
import urllib.parse

from flask import redirect, render_template, request, session
from functools import wraps

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def usd(value):
    """Format value as USD."""
    return f"${value:,.2f}"

def percent(part, whole):
    """Calculates percentage of number to whole as USD."""

    percent = (part / whole) * 100

    return f"{percent:,.2f}"


def calculate_budget(income_percent, housing_percent, food_percent, transportation_percent, saving_percent, other_percent, budget_item, value):
    """Calculates values of all budget aspects given the value of one and weight of each item"""

    # Calculate the index based on the value and percentage for the selected budget item
    index = value / eval(budget_item + '_percent')

    # Calculate the values for each budget item based on the index
    income = float(index * income_percent)
    housing = float(index * housing_percent)
    food = float(index * food_percent)
    transportation = float(index * transportation_percent)
    saving = float(index * saving_percent)
    other = float(index * other_percent)

    # Return the calculated values as a dictionary
    return {
        'income': income,
        'housing': housing,
        'food': food,
        'transportation': transportation,
        'saving': saving,
        'other': other
    }

def calculate_total_amount(debt_amount, interest_rate, years):
    # Calculate the total amount paid
    percent = interest_rate / 100

    total_amount = debt_amount * (1 + (percent * years))

    # Return the total amount
    return total_amount