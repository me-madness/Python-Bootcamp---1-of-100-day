# Conditional Statement
print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm?"))

if height > 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride.")    

# Odd and Even Exercise
number =  int(input("Which number do you want to check?"))

if number % 2 == 0:
    print(f"This is an even number")
else:
    print(f"This is an odd number")
 
# Nested if Statements and elif statement
print("Welcome to the rollercoaster!")
height = int(input("What is you height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")      
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride.") 

# Interactive Coding Exercise BMI        
height = float(input("Enter your height in m:"))
weight = float(input("Enter your weight in kg:"))
result = round(weight / (height ** 2))

if result < 18.5:
    print(f"Your bmi is {result}, they are underweight.")
elif result < 25:
    print(f"Your bmi is {result}, they have a normal weight.")    
elif result < 30:
    print(f"Your bmi is {result}, they are overweight.")    
elif result < 35:
    print(f"Your bmi is {result}, they are obese.")
else:
    print(f"Your bmi is {result}, they are clinically obese.")        
 
# Interactive Coding Exercise Leap Year Exercise
year = int(input("Which year do you want to check?"))
 
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")

# Multiple If statement in Succession 

# Interactive Coding Exercise Pizzle Quiz

# Logical Operators

# Interactive Coding Exercise Lo

# Day 3 Project Treasure Island 