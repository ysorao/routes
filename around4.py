def turn_right():
    repeat 3:
        turn_left()


put()

while not front_is_clear():
    turn_left()
move()


while not object_here():
    if right_is_clear():  # keep to the right
        turn_right()
        move()
    elif front_is_clear():    # move ... following the right wall
        move()
    else:
        turn_left() 