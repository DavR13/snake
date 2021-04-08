from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor('black')
screen.tracer(0)

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

while scoreboard.game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collisions with food
    if food.distance(snake.head) < 15:
        snake.extend()
        food.refresh()
        scoreboard.add_point()

    # Detect collisions with wall
    if abs(snake.head.xcor()) >= screen.window_width()/2 or abs(snake.head.ycor()) >= screen.window_height()/2:
        scoreboard.game_over()

    # Detect collisions with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 12:
            scoreboard.game_over()

scoreboard.game_over()
screen.exitonclick()
