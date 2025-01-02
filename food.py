from turtle import Turtle
import random
from snake import Snake


class Food(Turtle, Snake):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.speed("fastest")
        self.rand_food()

    def rand_food(self):
        random_x = random.randint(-240, 240)
        random_y = random.randint(-240, 240)
        self.goto(random_x, random_y)


