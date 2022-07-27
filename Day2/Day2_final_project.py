name = input("What is your name? ")
sales = input("What is your monthly sales? ")
sales = int(sales)
commission = round(sales*13 / 100, 2)
# commission = round(commission, 2)

print(f"Hello {name}, your commission this month is ${commission}")



