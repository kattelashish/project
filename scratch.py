import turtle
import random

win = turtle.Screen()
win.title("make the geme")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


scorevalue = 0
# making snake

snake = turtle.Turtle()
snake.shape("square")
snake.color("white")
snake.penup()
snake.speed(0)

#score
score = turtle.Turtle()
score.color("white")
score.penup()
score.speed(0)
score.goto(-350,260)
score.color("blue")
score.hideturtle()
score.write("Score=",align="left",font=("Arial",24,"normal"))

#food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.speed(0)
food.goto(0,100)
#x=random.randint(200,-200)
#y=random.randint(100,-100)
#food.goto(x,y)

segment = []

def snake_movementright():

    x = snake.xcor()

    x = x+20
    if( x> 390):
        x= 390

    snake.setx(x)




def snake_movementleft():

    x1 = snake.xcor()
    x1 = x1-22
    if( x1< -390):
        x1= -390

    snake.setx(x1)


def snake_movementup():

    y = snake.ycor()
    y = y+22
    if(y>300):
        y = 290
    snake.sety(y)



def snake_movementdown():

    y1 = snake.ycor()
    y1 = y1-22
    if( y1< -300):
        y1= -290

    snake.sety(y1)


win.listen()
win.onkeypress(snake_movementleft, "Left")
win.onkeypress(snake_movementup, "Up")
win.onkeypress(snake_movementright, "Right")
win.onkeypress(snake_movementdown, "Down")

while True:

    win.update()
    if snake.distance(food)<20:

        score.clear()
        food.goto(random.randint(-290, 290), random.randint(-220, 220))
        scorevalue = scorevalue + 1
        score.write("Score = {}".format(scorevalue), align="left", font=("Arial", 24, "normal"))
        snakebody = turtle.Turtle()
        snakebody.shape("square")
        snakebody.color("Gray")
        snakebody.penup()
        snakebody.speed(0)
        segment.append(snakebody)

    for item in range(len(segment)-1, 0, -1):
        x = segment[item-1].xcor()
        y = segment[item-1].ycor()
        segment[item].goto(x, y)

        if len(segment) > 0:
            x = snake.xcor()
            y = snake.ycor()
            segment[0].goto(x,y)












