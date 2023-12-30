# Day 9 Task
# Dictionary, Nesting


# The Python Dictionary Deep Dive 

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected", 
    "Function": "a piece of code that you can easily call over and over again."
}

#Retrieving items from dictionary.
print(programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# Exercise - Grading Program

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key, value in student_scores.items():
  student_grades.append(value)

print(student_grades)


# Nesting Lists and Dictionaries




# Exercise - Dictionary in List




# The Secret Auction Program Instructions and Flow Chart