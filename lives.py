from turtle import Turtle

POSITIONS = [(370, 230), (340, 230), (310, 230)]

class Lifeline:
    def __init__(self):
        self.currLives = []
        self.create_lives()
        
    def create_lives(self):
        for position in POSITIONS:
            self.add_life(position)
        
    def add_life(self, position):
        new_segment = Turtle(shape="circle")
        new_segment.fillcolor("red")
        new_segment.penup()
        new_segment.goto(position)
        self.currLives.append(new_segment)
        
    def reduceLife(self):
        if self.currLives:
            life = self.currLives.pop()
            life.hideturtle()
        return self.numberOfLives() > 0
        
    def numberOfLives(self):
        return len(self.currLives)
    
    def reset_lives(self):
        for life in self.currLives:
            life.hideturtle()
        self.currLives.clear()
        self.create_lives()