#  This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

monthly_income = input ("Enter your monthly income: ")
monthly_expenses = input ("Enter your total monthly expenses: ")

monthly_savings = float(monthly_income) - float(monthly_expenses)
print ("Your monthly savings are $"+ str(int(monthly_savings))+ ".")

interest_rate = 0.05
projected_savings = int(monthly_savings) * 12 + int(monthly_savings) * 12 * int(0.05)
print ("Projected savings after one year, with interest, is: $" + str(projected_savings) +".")
