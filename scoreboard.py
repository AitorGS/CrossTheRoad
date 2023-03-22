from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        self.next_level()

    def next_level(self):
        self.clear()
        self.level += 1
        self.goto(x=-300, y=280)
        self.write(f"Level {self.level}", font=FONT)

    def game_over(self):
        self.goto(x=-100, y=0)
        self.write("GAME OVER", font=FONT)
        self.stamp()
