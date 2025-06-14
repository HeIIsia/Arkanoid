from turtle import Screen
from paddle import Paddle
from ball import Ball
from block import BlockManager
from GUI import GUI
import time

screen = Screen()
screen.setup(width=500, height=600)
screen.colormode(255)
screen.bgcolor(40, 40, 40)
screen.tracer(0)

paddle = Paddle()

STARTING_POSITIONS_yellow = [(-200, 180),(-150, 180), (-100, 180), (-50, 180), (0, 180), (50, 180), (100, 180), (150, 180), (200, 180)]
STARTING_POSITIONS_purple = [(-175, 150), (-125, 150), (-75, 150), (-25, 150), (25, 150), (75, 150), (125, 150), (175, 150)]
STARTING_POSITIONS_pink = [(-200, 120),(-150, 120), (-100, 120), (-50, 120), (0, 120), (50, 120), (100, 120), (150, 120), (200, 120)]

block_manager_yellow = BlockManager((177, 255, 0), STARTING_POSITIONS_yellow, 200)
block_manager_purple = BlockManager((249, 80, 200), STARTING_POSITIONS_purple, 100)
block_manager_pink = BlockManager((138, 80, 200), STARTING_POSITIONS_pink, 50)

all_block_managers = [block_manager_yellow, block_manager_purple, block_manager_pink]

total_block_count = block_manager_yellow.blocks_count + block_manager_purple.blocks_count + block_manager_pink.blocks_count

ball = Ball()
gui = GUI(0)

game_starting = True
game_on = False

# Launch the ball
def play():
    global game_starting
    global game_on
    game_starting = False
    game_on = True
    print("key s pressed, ball should move")

screen.listen()
screen.onkey(key="Left", fun=paddle.move_left)
screen.onkey(key="Right", fun=paddle.move_right)
screen.onkey(key="s", fun=play)

while game_starting: # Ball resting on paddle
    screen.update()
    ball.setx(paddle.xcor())
    ball.sety(paddle.ycor() + 20)

    while game_on: # Ball is launched
        time.sleep(0.05)
        screen.update()
        ball.move()

        # Bounce from the walls
        if ball.xcor() >= 230 or ball.xcor() <= -230:
            ball.bounce_x()

        # Bounce from the ceiling
        if ball.ycor() >= 230:
            ball.bounce_y()

        # Bounce from the paddle
        if ball.distance(paddle) < 30 and ball.ycor() <= -230:
            ball.bounce_y()
            ball.change_ball_speed()

        # Decrease lives if the ball is lost
        if ball.ycor() < -300:
            gui.decrease_lives()
            paddle.goto(0, -270)
            ball.goto(0, -250)
            if gui.lives > 0:
                ball.bounce_y()
                game_starting = True
                game_on = False
            else: # Out of lives, Game Over
                gui.game_over()
                game_on = False

        # Check collisions with any block type
        for block_manager in all_block_managers:
            for block in block_manager.all_blocks:
                if block.distance(ball) < 30: # If block is hit
                    total_block_count -= 1
                    block.goto(0, 400)
                    ball.bounce_y()
                    gui.increase_score(block_manager.score)
                    print(total_block_count)
                    if total_block_count <= 0: # All blocks are cleared, Stage Cleared
                        gui.stage_clear()
                        game_on = False

screen.exitonclick()