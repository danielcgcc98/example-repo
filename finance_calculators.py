# finance_calculators.py

# Import the math module so we can use math.pow()
import math

# Display the available calculation options
print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond - to calculate the amount you'll have to pay on a home loan.")

# Ask the user which calculator they would like to use
choice = input("Enter your choice (Investment/Bond): ").lower()

# ---------------------------
# Investment Calculator
# ---------------------------
if choice == "investment":

    # Get investment information from the user
    principal = float(input("Enter the amount you are depositing: "))
    rate = float(input("Enter the interest rate (as a percentage): ")) / 100
    years = int(input("Enter the number of years you plan to invest: "))
    interest_type = input("Enter the type of interest (simple/compound): ").lower()

    # Calculate simple interest
    if interest_type == "simple":
        total_amount = principal * (1 + rate * years)
        print(f"The total amount after {years} years will be: {total_amount:.2f}")

    # Calculate compound interest
    elif interest_type == "compound":
        total_amount = principal * math.pow((1 + rate), years)
        print(f"The total amount after {years} years will be: {total_amount:.2f}")

    # Handle invalid interest type
    else:
        print("Invalid interest type. Please choose 'simple' or 'compound'.")

# ---------------------------
# Bond Calculator
# ---------------------------
elif choice == "bond":

    # Get bond information from the user
    house_value = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the annual interest rate (as a percentage): ")) / 100
    months = int(input("Enter the number of months you plan to take to repay the bond: "))

    # Convert annual interest rate to monthly interest rate
    i = interest_rate / 12

    # Calculate the monthly repayment using the bond formula
    repayment = (i * house_value) / (1 - math.pow((1 + i), -months))

    print(f"The monthly repayment amount will be: {repayment:.2f}")

# Handle invalid menu choice
else:
    print("Invalid choice. Please choose either 'Investment' or 'Bond'.")