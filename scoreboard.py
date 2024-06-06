from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("AntiqueWhite1")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER. Your score is {self.score}", align=ALIGNMENT, font=("Courier", 24, "normal"))
