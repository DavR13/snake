from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


snake = Snake()
food = Food()
score = Scoreboard()

screen = Screen()
screen.bgcolor('black')
screen.tracer(0)

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.listen()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collisions with food
    if food.distance(snake.head) <= 15:
        snake.add_segment()
        food.refresh()
        score.add_point()
        print("Score: " + str(score.score))

    # Detect collisions with wall
    if abs(snake.head.xcor()) >= screen.window_width()/2 or abs(snake.head.ycor()) >= screen.window_height()/2:
        break

    # Detect collisions with tail

score.game_over()
screen.exitonclick()
