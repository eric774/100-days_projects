from turtle import Screen
from caterpillar import Caterpillar
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My caterpillar Game")
screen.tracer(0)

caterpillar = Caterpillar()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(caterpillar.up, "Up")
screen.onkey(caterpillar.down, "Down")
screen.onkey(caterpillar.left, "Left")
screen.onkey(caterpillar.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    caterpillar.move()

    #Detect collision with food.
    if caterpillar.head.distance(food) < 15:
        food.refresh()
        caterpillar.extend()
        scoreboard.increase_score()

    #Detect collision with wall.
    if caterpillar.head.xcor() > 280 or caterpillar.head.xcor() < -280 or caterpillar.head.ycor() > 280 or caterpillar.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for segment in caterpillar.segments:
        if segment == caterpillar.head:
            pass
        elif caterpillar.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()
