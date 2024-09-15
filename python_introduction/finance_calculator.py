#  This script will calculate the user’s monthly savings based on inputted monthly income and expenses. It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.

monthlyincome = input ("Enter your monthly income: ")
monthlyexpenses = input ("Enter your total monthly expenses:")
monthlysavings = int(monthlyincome) - int(monthlyexpenses)
print ("Your monthly savings are $"+ str(monthlysavings)+ ".")
projectedsavings = int(monthlysavings) * 12 + (int(monthlysavings) * 12 * int(0.05))
print ("Projected savings after one year, with interest, is: $" + str(projectedsavings) +".")