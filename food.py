from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.fillcolor("#FF1493")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        random_x=random.randint(-380,380)
        random_y=random.randint(-240,180)
        self.goto(random_x,random_y)