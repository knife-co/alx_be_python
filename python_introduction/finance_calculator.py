# You will create a script named finance_calculator.py. 
# This script will calculate the user’s monthly savings based on inputted monthly income and expenses. 
# It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

# Instructions:

# User Input for Financial Details:

# Prompt the user for their monthly income: “Enter your monthly income: ”.
# Ask for their total monthly expenses: “Enter your total monthly expenses: ”.
# Calculate Monthly Savings:

# Calculate the monthly savings by subtracting monthly expenses from the monthly income.
# Project Annual Savings:

# Assume a simple annual interest rate of 5%.
# Calculate the projected savings after one year, incorporating the interest. Use the simplified formula for annual savings projection: 
# (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05)).
# Output Results:

# Display the user’s monthly savings.
# Display the projected annual savings after including interest.

# Enter your monthly income: 5000
# Enter your total monthly expenses: 4000
# Your monthly savings are $1000.
# Projected savings after one year, with interest, is: $12600.

monthly_income = int(input("Enter your monthly income:"))
monthly_expense = int(input("Enter your total monthly expenses:"))

monthly_savings = monthly_income - monthly_expense
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")
