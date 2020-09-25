# 3.21

price = int(input("enter item price in cents "))
change = 100 - price
quarters = change // 25
dimes = (change % 25) // 10
nickles = (change % 25 % 10) // 5
pennies = (change % 25 % 10 % 5)

print("Your change is: ")
print(quarters, "quarters")
print(dimes, "dimes")
print(nickles, "nickles")
print(pennies, "pennies")