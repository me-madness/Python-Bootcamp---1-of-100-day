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
height = int(input("What is you height in cm?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 12
        print("youth tickets are $7")      
    else:
        bill = 12
        print("Adult tickets are $12")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
        
    print(f"Your final bill is ${bill}")
            
else:
    print("Sorry, you have to grow taller before you can ride.") 

# Interactive Coding Exercise Pizzle Order Exercise
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L ")
add_pepperoni = input("Do you want extra cheese? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
    
if extra_cheese == "Y":
    bill += 1        

print(f"Your final bill is: ${bill}")

# Logical Operators

# Interactive Coding Exercise Lo

# Day 3 Project Treasure Island 