from turtle import Turtle

TURTLE_PACE = 20


class MainPlayer(Turtle):

    def __init__(self, window_width, window_height):
        super().__init__()
        self.color("green")
        self.shape("turtle")
        self.shapesize(0.65,0.65)
        self.penup()
        self.reposition()

    def reposition(self):
        self.setx(0)
        self.sety(-290)
        self.setheading(90)

    def move_up(self):
        self.forward(TURTLE_PACE)

    def move_down(self):
        self.forward(TURTLE_PACE * -1)

    def has_crashed(self, cars):
        for car in cars:
            if self.xcor() >= car.xcor() - 30 and self.distance(car) < 20:
                print(f"Hit by car {car.row} and color {car.color()[0]}")
                return True

        return False

    def has_win_level(self):
        if self.ycor() > 220:
            return True
