from turtle import Turtle,Screen
from pong import Pong
from ball import balls
from score_board import Scores
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("THE_PONG_GAME")
screen.tracer(0)
r_paddle = Pong()
r_paddle.paddle.goto(350,0)
l_paddle = Pong()
l_paddle.paddle.goto(-350,0)
scoresboard = Scores()



Ball =  balls()



screen.listen()
screen.onkey(l_paddle.up,"w")
screen.onkey(r_paddle.up,"i")
screen.onkey(l_paddle.down,"s")
screen.onkey(r_paddle.down,"k")


game_is_on = True

while game_is_on:
    time.sleep(Ball.move_speed)
    screen.update()
    Ball.move()

    if Ball.ycor() > 290 or Ball.ycor() < -290:
        Ball.bounce_y()

    if Ball.distance(r_paddle.paddle) < 50 and Ball.xcor() > 340 or Ball.distance(l_paddle.paddle) < 50 and Ball.xcor() < -340:
        Ball.bounce_x()

    if Ball.xcor() > 380:
        Ball.ball_miss()
        scoresboard.l_point()
        scoresboard.self_update()
    if Ball.xcor() < -380:
        Ball.ball_miss()
        scoresboard.r_point()
        scoresboard.self_update()

screen.exitonclick() 