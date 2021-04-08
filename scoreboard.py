from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")

        # add 21 newlines to argument to move scoreboard text to top of window
        self.write(f"Score: {self.score}" + "\n"*21, move=True, align="center", font=("Arial", 12, "normal"))
        self.hideturtle()
        self.penup()
