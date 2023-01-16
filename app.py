import os

from flask import Flask, flash, redirect, render_template, request
from helpers import apology, usd, percent, calculate_budget, calculate_total_amount

# Configure application
app = Flask(__name__)

# Ensure tecdmplates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=['GET', 'POST'])
def home():
    """Calculates percentages of all aspects of given budget"""

    if request.method == "POST":

        # Stores income value and ensures it is a number
        try:
            income = float(request.form.get("income"))
        except ValueError:
            return apology("Invalid input for income", 400)

        # Stores housing value and ensures it is a number
        try:
            housing = float(request.form.get("housing"))
        except ValueError:
            return apology("Invalid input for housing", 400)

        # Stores food value and ensures it is a number
        try:
            food = float(request.form.get("food"))
        except ValueError:
            return apology("Invalid input for food", 400)

        # Stores transportation value and ensures it is a number
        try:
            transportation = float(request.form.get("transportation"))
        except ValueError:
            return apology("Invalid input for transportation", 400)

        # Stores saving value and ensures it is a number
        try:
            saving = float(request.form.get("saving"))
        except ValueError:
            return apology("Invalid input for saving", 400)

        # Stores debt value and ensures it is a number
        try:
            debt_payments = float(request.form.get("debt_payments"))
        except ValueError:
            return apology("Invalid input for debt payments", 400)

        # Stores other value and ensures it is a number
        try:
            other = float(request.form.get("other"))
        except ValueError:
            return apology("Invalid input for other", 400)

        # Uses percent function to calculate percentage of that item compared to income and stores it
        housing_percent = percent(housing, income)
        food_percent = percent(food, income)
        transportation_percent = percent(transportation, income)
        saving_percent = percent(saving, income)
        debt_payments_percent = percent(debt_payments, income)
        other_percent = percent(other, income)

        # Returns view.html where relevent info is displayed
        return render_template("view.html", income=income, housing_percent=housing_percent, food_percent=food_percent, transportation_percent=transportation_percent, saving_percent=saving_percent, debt_payments_percent=debt_payments_percent, other_percent=other_percent,
        housing=housing, food=food, transportation=transportation, saving=saving, debt_payments=debt_payments, other=other)


    else:

        # Bring user to home page, where they can input budget info
        return render_template("home.html")

@app.route("/builder", methods=['GET', 'POST'])
def builder():
    """Calculates the dollar values of all budget items given the value of one item"""

    if request.method == "POST":

        # Stores selected option from dropdown
        budget_item = request.form.get("builder_select")

        # If user selected "Select Budget Item" from dropdown
        if budget_item == ("1"):
            return apology("Invalid budget item", 400)

        # Stores value of whatever budget item is selected and ensures it is a number
        value = request.form.get("builder_value")
        if value is None:
            return apology("Missing value of item", 400)
        try:
            value = float(value)
        except ValueError:
            return apology("Invalid value of item", 400)

        # Percentages of each budget item
        income_percent = 100
        housing_percent = 25
        food_percent = 12
        transportation_percent = 13
        saving_percent = 20
        other_percent = 30

        # If user selected "Income" from dropdown, calculates the values of all other budget aspects given income value and percentages for all other values
        if budget_item == "2":
            budget_values = calculate_budget(income_percent, housing_percent, food_percent, transportation_percent,
            saving_percent, other_percent, 'income', value)

        # If user selected "Housing" from dropdown, calculates the values of all other budget aspects given housing value and percentages for all other values
        elif budget_item == "3":
            budget_values = calculate_budget(income_percent, housing_percent, food_percent, transportation_percent,
            saving_percent, other_percent, 'housing', value)

        # If user selected "Food" from dropdown, calculates the values of all other budget aspects given food value and percentages for all other values
        elif budget_item == "4":
            budget_values = calculate_budget(income_percent, housing_percent, food_percent, transportation_percent,
            saving_percent, other_percent, 'food', value)

        # If user selected "Transportation" from dropdown, calculates the values of all other budget aspects given transportation value and percentages for all other values
        elif budget_item == "5":
            budget_values = calculate_budget(income_percent, housing_percent, food_percent, transportation_percent,
            saving_percent, other_percent, 'transportation', value)

        # If user selected "Saving/Debt Payments" from dropdown, calculates the values of all other budget aspects given saving and debt value and percentages for all other values
        elif budget_item == "6":
            budget_values = calculate_budget(income_percent, housing_percent, food_percent, transportation_percent,
            saving_percent, other_percent, 'saving', value)

        # If user selected "Other" from dropdown, calculates the values of all other budget aspects given other value and percentages for all other values
        elif budget_item == "7":
            budget_values = calculate_budget(income_percent, housing_percent, food_percent, transportation_percent,
            saving_percent, other_percent, 'other', value)

        # Retreives values from the returned dictionary and stores them in variables
        income = budget_values['income']
        housing = budget_values['housing']
        food = budget_values['food']
        transportation = budget_values['transportation']
        saving = budget_values['saving']
        other = budget_values['other']

        # Returns built.html, which displays relevent information
        return render_template("built.html", income=income, housing=housing, food=food, transportation=transportation, saving=saving, other=other,
        income_percent=income_percent, housing_percent=housing_percent, food_percent=food_percent, transportation_percent=transportation_percent,
        saving_percent=saving_percent, other_percent=other_percent)

    else:

        # Bring user to Budget Builder page to make selection and enter info
        return render_template("builder.html")

@app.route("/debt", methods=['GET', 'POST'])
def debt():
    """Calculates monthly payment given debt amount, interest rate, and time frame goal"""

    if request.method == "POST":
            
        # Stores debt value and ensures it is a number
        try:
            debt_amount = float(request.form.get("debt_amount"))
        except ValueError:
            return apology("Invalid input for debt amount", 400)

        # Stores interest rate value and ensures it is a number
        try:
            interest_rate = float(request.form.get("interest_rate"))
        except ValueError:
            return apology("Invalid input for interest rate", 400)
        
        # Stores debt value and ensures it is a number
        try:
            debt_amount = float(request.form.get("debt_amount"))
        except ValueError:
            return apology("Invalid input for debt amount", 400)

        # Stores interest type value and ensures one type is selected
        time_unit = request.form.getlist('time_unit')

        if not time_unit:
            # Handle the case where no option is selected
            return apology("Invalid input for time unit", 400)
        else:
            # Store the selected option in a variable
            selected_time_unit = time_unit[0]
        
        # Stores months value and ensures it is a number
        try:
            time = int(request.form.get("time"))
        except ValueError:
            return apology("Invalid input for time", 400)

        # Defaults to yearly interest rate. Converts months to year equivialant and stores value of months
        if selected_time_unit == "months":
            years = (time / 12)
            months = time

        # Stores year and month equivilant
        elif selected_time_unit == "years":
            years = time
            months = (time * 12)

        # Uses calculate_total_amount function from helpers.py to find amount that will eventually be paid including interest
        total_amount = calculate_total_amount(debt_amount, interest_rate, years)

        # Calculates monthly payment by dividing by total amount of months in goal
        monthly_payment = total_amount / months

        # Initializes iteration dictionary with values prior to loop
        iteration = [{'counter': 0, 'balance': total_amount, 'paid_to_date': 0},]

        # Initializes variables
        counter = 0
        balance = total_amount
        paid_to_date = 0

        # If goal unit is in months
        if selected_time_unit == "months":
            
            # Variables used in debt_view.html
            display_unit = "Month"
            head_unit = "months"

            # Loop that calculates values for each row of table on debt_view.html
            for num in range(int(time)):

                # Month counter
                counter = counter + 1

                # Values for table
                paid_to_date = (paid_to_date + monthly_payment)
                balance = (balance - monthly_payment)
                if (balance) < 0:
                    balance = 0

                # Makes entry to iteration dictionary for each loop. Each loop/entry is a row in the table
                iteration.append({"counter": counter, "balance": balance, "paid_to_date": paid_to_date})
        
        # If goal unit is in years
        if selected_time_unit == "years":

            # Variables used in debt_view.html
            display_unit = "Year"
            head_unit = "years"

            # Loop that calculates values for each row of table on debt_view.html
            for num in range(int(time)):

                # Year counter
                counter = counter + 1

                # Values for table
                paid_to_date = (paid_to_date + (monthly_payment * 12))
                balance = (balance - (monthly_payment * 12))
                if (balance) < 0:
                    balance = 0

                 # Makes entry to iteration dictionary for each loop. Each loop/entry is a row in the table
                iteration.append({"counter": counter, "balance": balance, "paid_to_date": paid_to_date})

        # Stores length of iteration dictionary (useful for line chart)
        length = len(iteration)

        # Returns debt_view.html with useful information to fill in
        return render_template("debt_view.html", total_amount=total_amount, monthly_payment=monthly_payment, display_unit=display_unit, iteration=iteration, head_unit=head_unit, time=time, length=length)


    else:
            # Returns debt.html when user first arrives to page
            return render_template("debt.html")


@app.route("/about")
def about():
    """Displays about page to user"""

    # Returns about page
    return render_template("about.html")

