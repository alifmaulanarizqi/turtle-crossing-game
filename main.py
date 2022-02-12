import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.move)

counter = 1
game_is_on = True
while game_is_on:
    time.sleep(0.07)
    screen.update()

    # Create car every 6 loops
    if counter % 6 == 0:
        car.create_car()
    car.move()

    # Player collides with a car
    for c in car.list_cars:
        if c.distance(player) < 21:
            game_is_on = False
            scoreboard.game_over()

    # Player when reach the finish area
    if player.ycor() > player.finish_line:
        scoreboard.increment_level()
        player.reset()
        car.level_up()

    counter += 1

screen.exitonclick()
