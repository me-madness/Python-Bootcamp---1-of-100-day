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
print(result)