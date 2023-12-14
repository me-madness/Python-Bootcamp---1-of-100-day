# Functions, Code Blocks and While Loops


# Defining and calling python functions

def my_function():
    print("Hello")
    print("Bey")
    
    
my_function()    


# The hurdles loop challenge

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():    
    move()
    turn_left()
    move()
    turn_right()  
    move()
    turn_right()
    move()
    turn_left()  

for step in range(6):
    jump()


# Indentation in Python

def my_function():
    if sky == "clear":
        print("blue")
    elif sky == "cloudy": 
        print("grey")
    print("Hello")       
print("World")


# While Loops

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():    
    move()
    turn_left()
    move()
    turn_right()  
    move()
    turn_right()
    move()
    turn_left()  

for step in range(6):
    jump()
    
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump() 
    number_of_hurdles -= 1
    print(number_of_hurdles)

while not at_goal():
    jump()

# Hurdles Challenge using While loops





# Jumping over hurdles with variables heights

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while front_is_clesr():
        move()
    turn_left()
    
while not at_goal():
    if wall_in_front():
        jump()   
    else:
        move()             



# Project Escaping the Maze
# 6_of_100_project_escaping_the_maze