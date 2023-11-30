# Primitive date type
print("Hello"[4])


# Type Error, Type Checking and Type Conversion
num_char = len(input("What is your name?"))
print(type(num_char))

new_num_char = str(num_char)
print("Your name has " + new_num_char + " character.")

# Interactive coding Exercise- Data types
two_digit_number = input("Type a two digit number: ")
a = int(two_digit_number[0])
b = int(two_digit_number[1])
print(a + b)

# Mathematical Operations in Python
3 + 5
3 - 5
3 * 5
3 / 5
3 ** 5
3 // 5

PEMDAS
()
**
*/
+
-

# Interactive Coding Exercise - BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#First way
result = int(weight) / (float(height) ** 2)

# Second way
result = int(weight) / (float(height) * float(height))
print(int(result))
print(f"{result:.2f}")

# Number Manipulation and f-string in Python
score = 0
height = 1.8
isWinning = True

print("Your score is " + str(score))
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# Interactive Coding Exercise - Life in weeks
age = input("What is your current age?")
years = 90 - int(age)

days_left = years * 365
weeks_left = days_left // 7
months_left = years / 12
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

# Welcome to the tip calculator
# 2_of_100_project_tip_calculator.py