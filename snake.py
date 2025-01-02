from turtle import Turtle

INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.initial_snake()
        self.head = self.snake_segments[0]
        self.head.color("red")

    def initial_snake(self):
        for a in INITIAL_POSITION:
            self.add_segment(a)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        snake = Turtle("square")
        snake.penup()
        snake.color("green")
        snake.goto(position)
        self.snake_segments.append(snake)

    def extend_body(self):
        self.add_segment(self.snake_segments[-1].position())

    def snake_reset(self):
        for a in self.snake_segments:
            a.goto(1000, 1000)
        self.snake_segments.clear()
        self.initial_snake()
        self.head = self.snake_segments[0]
        self.head.color("red")

    def upward(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def downward(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
