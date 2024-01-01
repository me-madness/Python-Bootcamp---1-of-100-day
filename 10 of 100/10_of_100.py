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
        print("Leap year.")
      else:
        print("Not leap year.")
    else:
      print("Leap year.")
  else:
    print("Not leap year.")

def days_in_month():
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



# Docstring





# Calculator Part 1 - Combining Dictionaries and Functions





# Print vs Return






# While Looops, Flags and Recursion





# Calculator Finishing Touches and Bug Fixes
##10_of_100_calculator_project.py