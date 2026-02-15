def turn_right():
    print("Turning right")

def turn_left():
    print("Turning left")

def move():
    print("Moving forward")

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# Simulating obstacle jumps
move()
jump()
move()
jump()
move()
