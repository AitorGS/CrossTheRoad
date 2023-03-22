import time
from turtle import Screen
from main_player import MainPlayer
from car_manager import CarManager
from scoreboard import Scoreboard
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

screen = Screen()
screen.setup(width=WINDOW_WIDTH + 20, height=WINDOW_HEIGHT + 50)
screen.tracer(0)

scoreboard = Scoreboard()
main_player = MainPlayer(WINDOW_WIDTH, WINDOW_HEIGHT)

car_manager = CarManager(WINDOW_WIDTH, WINDOW_HEIGHT)


screen.onkeypress(main_player.move_up, "Up")
screen.onkeypress(main_player.move_down, "Down")

screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.move_cars()
    if main_player.has_crashed(car_manager.cars):
        scoreboard.game_over()
        game_is_on = False
    if main_player.has_win_level():
        car_manager.next_level()
        main_player.reposition()
        scoreboard.next_level()
    screen.update()


screen.exitonclick()
