def turn_right():
    repeat 3:
        turn_left()
        
def giro():
    repeat 2:
        turn_left()
        
        
def subir_esc():
    turn_left()
    move()
    turn_right()
    repeat 2:
        move()

def bajar_esc():
    repeat 2:
        move()
    turn_left()
    move()
    turn_right()


take()  
repeat 3:
    subir_esc()
put() 
giro()
repeat 3:
    bajar_esc()
