from turtle import Turtle

scr = Turtle()

with open("../../../Desktop/PycharmProjects/020_snake_project_new/data.txt", mode="r") as file:
    a = file.read()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(a)
        self.snake_score()

    def snake_score(self):
        self.clear()
        self.pencolor("white")
        self.penup()
        self.goto(-20, 270)
        self.pendown()
        self.hideturtle()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Arial", 14, "italic"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Arial", 14, "italic"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over !!", align="center", font=("Arial", 20, "italic"))

    def score_reset(self):
        if self.score > self.high_score:
            with open("../../../Desktop/PycharmProjects/020_snake_project_new/data.txt", mode="w") as file:
                file.write(str(self.score))
            self.high_score = self.score
        self.score = 0
