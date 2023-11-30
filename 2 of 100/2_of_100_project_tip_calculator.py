bill = input("What was the total bill? ")
tip = input("What percentage tip would you like to give? 10, 12, 0r 15? " )
people = input("How many people to split the bill? ")
result = (float(bill) + int(tip)) / people

print(f" YEach people should pay: {result:.2f}")