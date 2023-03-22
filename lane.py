from turtle import Turtle

class Lane(Turtle):

    def __init__(self,  window_width, window_height, row, car):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.car = car
        self._draw_lane(window_width, window_height, row)

    def _draw_lane(self, window_width, window_height, row):
        self.penup()
        self.setx(window_width / 2)
        self.sety(window_height / -2 + (row * 20))
        self.pendown()
        self.setx(window_width / -2)
        print(f"Lane created at {self.ycor()}")







