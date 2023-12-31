from turtle import Turtle
UP = 90
DOWN = 270

class Pong:
    def __init__(self):
        self.creating_pong()   
        self.up()
        self.down()
        
    def creating_pong(self):
        self.paddle = Turtle()
        self.paddle .color("white")
        self.paddle .shape("square")
        self.paddle .shapesize(stretch_wid=0.4,stretch_len=3)
        self.paddle.right(90)
        self.paddle .penup()
       
    
    def up(self):
        new_y = self.paddle.ycor() + 30
        self.paddle.goto(self.paddle.xcor(),new_y)
    def down(self):
        new_y = self.paddle.ycor() - 30
        self.paddle.goto(self.paddle.xcor(),new_y)
