from turtle import Turtle
FONT=("Arial",15,"normal")
ALI="center"
class scorcard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_score()

    
    def update_score(self):
        self.clear
        self.write(f"score: {self.score}" ,align=ALI , font=FONT)
        
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_score()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER" ,align=ALI , font=FONT)
            
    
    def increase_score(self):
        self.score +=1
        self.update_score()
        
