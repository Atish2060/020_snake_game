from turtle import Screen, Turtle
import time as t
from snake import Snake
from food import Food
from score_board import Score
screen = Screen()
screen.title("Snake Game")
screen.setup(600, 600)
screen.bgcolor("black")
snake_segments = []
screen.tracer(0)

border = Turtle()
border.pencolor("white")
border.penup()
border.goto(-270, 270)
border.pendown()
border.goto(270, 270)
border.goto(270, -270)
border.goto(-270, -270)
border.goto(-270, 270)
border.hideturtle()

score = Score()
snake = Snake()
food = Food()
is_game_on = True

screen.listen()
screen.onkey(snake.upward, "Up")
screen.onkey(snake.downward, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

while is_game_on:
    screen.update()
    t.sleep(0.1)
    score.snake_score()
    snake.move()
    if snake.head.xcor() > 260 or snake.head.xcor() < -260 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        score.score_reset()
        snake.snake_reset()
    if snake.head.distance(food) < 15:
        snake.extend_body()
        food.rand_food()
        score.update_score()
    for tail in snake.snake_segments[1:]:
        if snake.head.distance(tail) < 10:
            score.score_reset()
            snake.snake_reset()


screen.exitonclick()