from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.turtlesize(stretch_len=2, stretch_wid=2)
        self.goto(0,270)
        self.color("white")
        self.score = 0
        self.display()

    def display(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.display()
