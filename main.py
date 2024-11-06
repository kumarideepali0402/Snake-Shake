from turtle import Screen,Turtle
from snake import Snake
import time
from food import Food
from scoreboard import ScoreBoard
from lives import Lifeline



screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("#001F3F")
screen.title("Snake & Shake")
screen.tracer(0)


#Snake which is getting displayed on start Screen
dummy= Snake()
screen.update()

##Start text which is visible on start Screen
start=Turtle()
start.hideturtle()

start.penup()
start.goto(-180,-20)
start.color("white")
start.write("Press S ", align='left', font=('Arial', 28, 'normal'))

##Start text which is visible on start Screen
start2=Turtle()
start2.hideturtle()

start2.penup()
start2.goto(10,-20)
start2.color("white")
start2.write(" Start Game", align='left', font=('Arial', 28, 'normal'))
game_is_on = False






snake = Snake()
food = Food()
sb = ScoreBoard()
life = Lifeline()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

def reset_game():
    snake.reset_position()
    food.refresh()
    
def turnOnGame():
    dummy.disAppear()
    game_is_on = True
    start.clear()
    start2.clear()
    
    while game_is_on:
        screen.update()
        time.sleep(0.1)  
        snake.move() 
       
        if snake.head.distance(food) < 15:
            sb.updateScore()
            food.refresh()
            snake.extend()
            
       
        if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 240 or snake.head.ycor() < -240:
            if life.reduceLife():
                reset_game()
            else:
                game_is_on = False
                sb.game_over()

       
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                if life.reduceLife():
                    reset_game()
                else:
                    game_is_on = False
                    sb.game_over()
                break 
    
screen.onkey(turnOnGame,"S")



screen.exitonclick()