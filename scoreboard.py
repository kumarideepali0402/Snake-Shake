from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,210)
        self.score=0
        self.updateScore()
        
        
    def updateScore(self):
        self.clear()
        self.write(arg=f"Score is {self.score}",align='center', font=('Arial', 20, 'normal'))
        self.score=self.score+1
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game is over",align='center', font=('Arial', 20, 'normal'))
        
    

    def update_level(self, level):
        self.clear()
        self.write(f"Score: {self.score} | Level: {level}", align='center', font=('Arial', 20, 'normal'))
    
    
    def reset_score(self):
        self.score = 0
        self.updateScore()