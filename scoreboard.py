from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.game_is_on = True
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,380)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=("Arial", 22, "normal"))
        self.game_is_on = False
