from turtle import Screen
from player_turtle import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(height= 600, width= 600)
screen.tracer(0)

player = Player()
car = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while(game_on):
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_car()

    
    for car_obj in car.all_cars:
        if car_obj.distance(player) < 20:
            game_on = False
            score.game_over()

    
    if player.ycor() > 280:
        player.goto_start()
        score.increase_level()
        car.increase_speed()


screen.exitonclick()


# Project by Shivani Verma
