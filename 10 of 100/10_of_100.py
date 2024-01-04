# Functions with Outputs

def my_function():
    return 3 * 2
output = my_function()

def my_function(something):
    print("Something is", something)
my_function("new")

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name}{formated_l_name}"  
print(format_name("John", "Angela"))

  
# Multiple Return

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Ressult: {formated_f_name}{formated_l_name}"  
print(format_name(input("What is your first name? "),
                  input("What is your last name? ")))



# Exercise - Days in Mount

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
        return True
  else:
    return False


def days_in_month(year, month):
  # if month > 121 or month < 1:
  #   return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) == 2:
      return 29
  return month_days[month -1]
 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# Docstring

#Storing output in a variable
formatted_name = format_name(input("Your first name: "),input("Your last name: "))
print(format_name)

#Or printing output directly
print(format_name(input("What is your first name? "),input("What is your last name? ")
))

#Already used functions with outputs.
lentgth = len(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
  """Take a first and last name and format it 
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"Ressult: {formated_f_name}{formated_l_name}"  

format_name()


# Calculator Part 1 - Combining Dictionaries and Functions

#Add
def add(a, b):
  a + b

#Substract
def substract(a, b):
  return a - b

#Multiply
def multiply(a, b):
  return a * b

#Divide
def divide(a, b):
  return a / b
  
#Operants
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

first_number = input("What's the first number?: ")
for symbol in operations:
  print(symbol)
second_number = input("What's the second number?: ")
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(first_number, second_number)


print(f"{first_number} {operation_symbol} {second_number} = {answer}")


# Print vs Return


#Add
def add(a, b):
  a + b

#Substract
def substract(a, b):
  return a - b

#Multiply
def multiply(a, b):
  return a * b

#Divide
def divide(a, b):
  return a / b
  
#Operants
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

first_number = input("What's the first number?: ")
for symbol in operations:
  print(symbol)
second_number = input("What's the second number?: ")
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
first_answer = calculation_function(first_number, second_number)


print(f"{first_number} {operation_symbol} {second_number} = {first_answer}")



operation_symbol = input("Pick an operation from the line above: ")
third_number = input("What's the next number?: ")
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(first_number, second_number), third_number)

print(f"{first_number} {operation_symbol} {second_number} = {second_answer}")


# While Looops, Flags and Recursion


#Add
def add(a, b):
  a + b

#Substract
def substract(a, b):
  return a - b

#Multiply
def multiply(a, b):
  return a * b

#Divide
def divide(a, b):
  return a / b
  
#Operants
operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}

first_number = input("What's the first number?: ")
for symbol in operations:
  print(symbol)
second_number = input("What's the second number?: ")
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
first_answer = calculation_function(first_number, second_number)


print(f"{first_number} {operation_symbol} {second_number} = {first_answer}")



operation_symbol = input("Pick an operation from the line above: ")
third_number = input("What's the next number?: ")
calculation_function = operations[operation_symbol]
second_answer = calculation_function(calculation_function(first_number, second_number), third_number)

print(f"{first_number} {operation_symbol} {second_number} = {second_answer}")
print("new commit")



# Calculator Finishing Touches and Bug Fixes
##10_of_100_calculator_project.py