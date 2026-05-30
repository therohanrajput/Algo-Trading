#Python Mini Project 1 :
#Scenario: Stock Data Entry and Analysis Tool
#Objective: Create a Python script that will involve taking manual input for stock prices over a week and will calculate the average price. It should also demonstrate variable declaration, user input, and basic arithmetic using Python types.

#input stock prices for a week's total working days
stock_name = input("Enter the name of the stock: ")
day1= float(input("Enter the stock price for Day 1: "))
day2= float(input("Enter the stock price for Day 2: "))
day3= float(input("Enter the stock price for Day 3: "))
day4= float(input("Enter the stock price for Day 4: "))
day5= float(input("Enter the stock price for Day 5: "))

#calculate the average stock price for the week
average_price = (day1 + day2 + day3 + day4 + day5) / 5

#Generate a report
print(f"\n====Analysis Report====")
print(f"Stock Name: {stock_name}")
print(f"The average stock price for the week is: {average_price:.2f}")
print(f"====Report End====")
