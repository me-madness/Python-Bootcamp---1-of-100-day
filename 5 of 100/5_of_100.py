# Using for lop in python lists

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + "Pie")
print(fruits)    

# Exercise - Average Height  

student_heights = input("Input a list of student heights ").split()
for n in range(len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)      