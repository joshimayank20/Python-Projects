from turtle import Screen, Turtle
import time
import random

# ---------------------------- SCREEN SETUP ------------------------------- #
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# ---------------------------- CREATE SNAKE ------------------------------- #
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    segments.append(segment)

head = segments[0]

# ---------------------------- MOVE SNAKE ------------------------------- #
def move():
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    head.forward(20)

# ---------------------------- DIRECTION CONTROLS ------------------------------- #
def up():
    if head.heading() != 270:
        head.setheading(90)

def down():
    if head.heading() != 90:
        head.setheading(270)

def left():
    if head.heading() != 0:
        head.setheading(180)

def right():
    if head.heading() != 180:
        head.setheading(0)

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# ---------------------------- FOOD ------------------------------- #
food = Turtle("circle")
food.color("red")
food.penup()
food.shapesize(stretch_len=0.5, stretch_wid=0.5)
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# ---------------------------- SCORE ------------------------------- #
score = 0

scoreboard = Turtle()
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0, 260)

def update_score():
    scoreboard.clear()
    scoreboard.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

update_score()

# ---------------------------- GAME LOOP ------------------------------- #
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    move()

    # Detect collision with food
    if head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        # Add new segment
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)

        score += 1
        update_score()

    # Detect wall collision
    if (
        head.xcor() > 280
        or head.xcor() < -280
        or head.ycor() > 280
        or head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.goto(0, 0)
        scoreboard.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    # Detect tail collision
    for segment in segments[1:]:
        if head.distance(segment) < 10:
            game_is_on = False
            scoreboard.goto(0, 0)
            scoreboard.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()
