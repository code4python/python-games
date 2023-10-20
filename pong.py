import turtle 

window = turtle.Screen()
window.title("Pong-Pong-Game | code4python")
window.setup(width=800, height=600)
window.tracer()
window.bgcolor(.1,.1,.1)

#ball
ball = turtle.Turtle()
ball.speed(0)#set max speed
ball.shape("square")
ball.color("white")
#scale facter defullt size(20px ,20px)
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.goto(x=0, y=0)
ball.penup()

ball_dx, ball_dy = 1, 1
ball_speed = 5


#center line 
center_line = turtle.Turtle()
center_line.speed(0)
center_line.color("white")
center_line.shape("square")

#set center line size 500px > 20px*25px
center_line.shapesize(stretch_len=.3, stretch_wid=25)
center_line.penup()
center_line.goto(0, 0)

#plyer 1
plyer_1 = turtle.Turtle()
plyer_1.speed(0)
plyer_1.shape("square")
plyer_1.shapesize(stretch_len=1, stretch_wid=5)
plyer_1.color("blue")
plyer_1.penup()
plyer_1.goto(x=-350, y=0)

#plyer 2
plyer_2 = turtle.Turtle()
plyer_2.speed(0)
plyer_2.shape("square")
plyer_2.shapesize(stretch_len=1, stretch_wid=5)
plyer_2.color("red")
plyer_2.penup()
plyer_2.goto(x=350, y=0)

#score text
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(x=0, y=260)
score.write("Player1 0 Player2 0", align="center", font=("courier",14,"normal"))
score.hideturtle() # hide drefult text in turtul 

p1_score , p2_score = 0, 0

#player moving

# mive player 1
player_speed = 20
def p1_move_up():
    plyer_1.sety(plyer_1.ycor() + player_speed)
def p1_move_down():
    plyer_1.sety(plyer_1.ycor() - player_speed)

# mive player 2
def p2_move_up():
    plyer_2.sety(plyer_2.ycor() + player_speed)
def p2_move_down():
    plyer_2.sety(plyer_2.ycor() - player_speed)
       
# key press
window.listen()
window.onkeypress(p1_move_up, "w")
window.onkeypress(p1_move_down, "s")
window.onkeypress(p2_move_up, "Up")
window.onkeypress(p2_move_down, "Down")

#

while True:
    window.update()

    # moving ball
    ball.setx(ball.xcor() + (ball_dx * ball_speed))               
    ball.sety(ball.ycor()+ (ball_dy * ball_speed))   

    # ball & borders
    if (ball.ycor() > 290): # 290 => 300(top border) - 10(half ball size)
        ball.sety(290)
        ball_dy *= -1       

    if (ball.ycor() < -290): # 290 => 300(top border) - 10(half ball size)
        ball.sety(-290)
        ball_dy *= -1   

    # down boll in playyer
    if (ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() > (plyer_1.ycor()-60) and ball.ycor() < (plyer_1.ycor()+60)):
        ball.setx(-340)
        ball_dx *= -1
    
    if (ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() > (plyer_2.ycor() -60) and ball.ycor() < (plyer_2.ycor()+60)):
        ball.setx(340)
        ball_dx *= -1


   # Crore Moving 
    if (ball.xcor() > 390):
        ball.goto(0,0)
        ball_dx *= -1
        score.clear()
        p1_score += 1
        score.write(f"Player1 {p1_score} Player2 {p2_score}", align="center", font=("courier",14,"normal"))

    if (ball.xcor() < -390):
        ball.goto(0,0)
        ball_dx *= -1
        score.clear()
        p2_score += 1
        score.write(f"Player1 {p1_score} Player2 {p2_score}", align="center", font=("courier",14,"normal"))

