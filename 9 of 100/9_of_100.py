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

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expection"
  elif score > 70:
    student_grades[student] = "Acceptable"
  elif score < 70:
    student_grades[student] = "Fail"

#for key, value in student_scores.items():
#  student_grades.append(value)
#print(student_grades)

# Nesting Lists and Dictionaries

capitals = {
  "France": "Paris",
  "Germany`": "Berlin",
  "Bulgaria": "Plovdiv",
  "Luxembourg": "Luxembourg",
}

#Nesting a List in a Dictionary
travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"], 
}

#Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 3}
}
#Nesting Dictionary in a List 
travel_log = [
  {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 3
    },
]

# Exercise - Dictionary in List

travel_log = [
  {
    "country": "France", 
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"],
    },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"],
    },
]

def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = country_visited
  new_country["visites"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)



add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


# The Secret Auction Program Instructions and Flow Chart