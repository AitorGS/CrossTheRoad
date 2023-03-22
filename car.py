from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self, color, row, level, window_width, window_height):
        super().__init__()
        self.color(color)
        self.pace = level * random.randint(1, 10)
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        self.window_width = window_width
        self.window_height = window_height
        self.row = row
        #Initial position differs from repositioning in that
        #initial cars should pop up on the main road
        #while reposioning happens always outisde the main road
        #otherwise there is a risk a reposition car pops up on top of the turtle
        #and hence ending the game
        initial_x = random.randint(self.window_width / -2, self.window_width /2)
        initial_y = self.window_height / -2 + 20 + (20 * self.row) - 10
        self.goto(initial_x, initial_y)

    def _position_car(self):
        initial_x = random.randint(self.window_width / 2, self.window_width + 1)
        initial_y = self.window_height / -2 + 20 + (20 * self.row) - 10
        self.goto(initial_x, initial_y)

    def __del__(self):
        print(f"Deleted car {self.color()[0]} at lane {self.row}")

    def move(self):
        self.goto(self.xcor() - self.pace, self.ycor())

    def has_left_screen(self):
        return self.xcor() < self.window_width / -2

    def reposition(self):
        self._position_car()


