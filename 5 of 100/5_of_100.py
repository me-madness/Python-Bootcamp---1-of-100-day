# Using for lop in python lists

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits)    

## Exercise - Average Height  
# First way of Exercise Average Height

student_heights = input("Input a list of student heights ").split()
total_height = 0
numbers_of_students = 0
for n in range(len(student_heights)):
    total_height += n
    numbers_of_students += 1
    average = round(total_height / numbers_of_students)
print(student_heights)      
print(average)

# Second way of the exercise Average Height

student_heights = input("Input a list of student heights ").split()
total_height = sum(student_heights)
numbers_of_students = len(student_heights)
average = round(total_height / numbers_of_students)
print(average)

## Exercise - High Score
# First way of the task

student_scores = input("Input a list of student heights ").split()
for n in student_scores:
    if x < n:
        x = n
print(f"The Highest score in the class is {x}")
   

# Second way of the task

student_scores = input("Input a list of student heights ").split()
max_score = max(student_scores)
print(f"The Highest score in the class is {max_score}")

 
# For loop with range() function
    
for number in range(1, 11, 3):
    print(number) 

total = 0    
for number in range(1, 101):
    total += number
print(total)  

## Exercise - Adding Evens          
# First way

total_even = 0
for number in range(100):
    if number % 2 == 0:
        total += number
        
print(total)  

# Second way

total_even = 0
for number in range(2, 101, 2):
    total += number
print(total)

# Exercise - The Fizz Buzz

for number in range(100):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)            
 
 
# Project Password Generator 
# 5_of_100_project_password_generator.py