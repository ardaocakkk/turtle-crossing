from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score() 
        self.update_score()
        
        
    def update_score(self):
        self.goto(-120,280)
        self.write(f"Your score is: {self.score}",align="center", font={"Arial",50,"normal"})
        
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align="center", font={"Arial",100,"normal"} )