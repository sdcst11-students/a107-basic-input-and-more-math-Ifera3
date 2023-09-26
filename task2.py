'''
##### Task 2 Compound Interest
Ask the user to enter the following:
* The principal (amount invested or borrowed)
* The annual interest rate (expressed as a percent)
* The number of compounding periods per year
* The length of time for the investment
Calculate the final amoutn as well as the amount of interest earned. Round your answer to 2 decimal places

```
https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
Enter the Princial: 2000
Enter the annual interest rate as a percent: 4
Enter the number of compounding periods: 4
How long is the investment period in years: 3
Your final amount is $2253.65
You earned $253.65 interest

Enter the Princial: 25000
Enter the annual interest rate as a percent: 7.5
Enter the number of compounding periods: 12
How long is the investment period in years: 6
Your final amount is $39152.94
You earned $14152.94 interest
```
'''

p = int(input("Enter the Princial: "))
r = float(input("Enter the annual interest rate as a percent: "))/100
n = int(input("Enter the number of compounding periods: "))
t = int(input("How long is the investment period in years: "))
a = round(p*((1+(r/n))**(n*t)), 2)
e = round(a-p, 2)
print(f"Your final amount is ${a}")
print(f"You earned ${e} interest")