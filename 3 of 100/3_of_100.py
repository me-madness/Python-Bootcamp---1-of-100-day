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
result = weight / (height ** 2)

if result < 18.5:
    print("They are underweight.")
elif result < 25:
    print("They have a normal weight.")    
elif result < 30:
    print("They are overweight.")    
elif result < 35:
    print("They are obese.")
else:
    print("They are clinically obese.")        
 
# Interactive Coding Exercise Lea

# Multiple If statement in Succession 

# Interactive Coding Exercise Pizzle Quiz

# Logical Operators

# Interactive Coding Exercise Lo

# Day 3 Project Treasure Island 