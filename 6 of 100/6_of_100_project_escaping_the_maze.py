# Escaping The Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    

while no at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()            