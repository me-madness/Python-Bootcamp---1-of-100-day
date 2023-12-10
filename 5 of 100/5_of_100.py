# Using for lop in python lists

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits)    

# Exercise - Average Height  
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

# Secon way of the exercise Average Height

student_heights = input("Input a list of student heights ").split()
total_height = sum(student_heights)
numbers_of_students = len(student_heights)
average = round(total_height / numbers_of_students)
print(average)

# 