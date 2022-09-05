from turtle import Screen
from player import Player
from car import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard() 
player = Player()
car = CarManager()

screen.listen()
screen.onkeypress(fun=player.move_up,key="Up")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    
    car.create_car()
    car.move_cars()


    #Detect when player collides with a car
    for cars in car.all_cars:
        if cars.distance(player) < 30:
            is_game_on = False
            scoreboard.game_over()
            
    #Detect when the player reached the other side
    if player.ycor() > 300:
        player.goto((0,-280))
        scoreboard.increase_score()
        car.level_up()
        
        
    
        
        
    
    
    
    
screen.exitonclick()