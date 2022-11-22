def roll():
    turn_left()
    turn_left()
    turn_left()

def run():    
    move()
    turn_left()
    move()
    roll()
    move()
    roll()
    move()
    turn_left()
    
number_of_times = 6
while number_of_times > 0:
    run()
    number_of_times -= 1
    print(number_of_times)    