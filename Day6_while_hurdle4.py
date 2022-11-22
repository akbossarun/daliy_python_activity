def roll():
    turn_left()
    turn_left()
    turn_left()
  
while not at_goal():
    if wall_in_front():
        if right_is_clear():
            roll()
            move()
        else:
            turn_left()
    if front_is_clear():
        if wall_on_right():
            move()
        elif right_is_clear():
            roll()
            move()
    
    
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
