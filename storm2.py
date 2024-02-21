def turn_right():
    repeat 3:
        turn_left()
        

def recolectar():
    while front_is_clear():
        if object_here():
            while object_here():
                take()
        else:
            move()
            recolectar()
    if wall_in_front() and is_facing_north():
        if object_here():
            while object_here():
                take()
        turn_left()
        move()
        turn_left()
    elif wall_in_front() and not is_facing_north():
        if object_here():
            while object_here():
                take()
        turn_right()
        if wall_in_front():
            repeat 2:
                turn_left()
            move()
            turn_right()
            move()
            move()
            turn_right()
            move()
            turn_right()
            while carries_object():
                toss()
            done()    
          
        else:
            
            move()
            turn_right()  
     
   
                
        

            
repeat 5:
    move()
turn_left()
recolectar()