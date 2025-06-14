from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 15, "bold")

class GUI(Turtle):
    def __init__(self, amount):
        super().__init__()
        self.amount = amount
        self.score = 0
        self.lives = 3
        self.draw_walls()
        self.update_score()
        self.update_lives()
        self.hideturtle()

    def draw_walls(self):
        walls = Turtle()
        walls.penup()
        walls.pencolor("white")
        walls.pensize(5)
        walls.goto(-245, -295)
        walls.pendown()
        walls.left(90)
        walls.forward(550)
        walls.right(90)
        walls.forward(485)
        walls.right(90)
        walls.forward(550)
        walls.hideturtle()

    def update_score(self):
        self.penup()
        self.goto(75, 265)
        self.pencolor("red")
        self.write("SCORE", align=ALIGNMENT, font=FONT)
        self.goto(165, 265)
        self.pencolor("white")
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self, amount):
        self.score += amount
        self.clear()
        self.update_score()
        self.update_lives()

    def decrease_lives(self):
        self.lives -= 1
        self.clear()
        self.update_score()
        self.update_lives()

    def stage_clear(self):
        self.penup()
        self.goto(0, -30)
        self.pencolor("white")
        self.write("STAGE CLEAR!", align=ALIGNMENT, font=("Arial", 30, "bold"))

    def update_lives(self):

        self.penup()
        self.goto(-175, 265)
        self.pencolor("red")
        self.write("1-UP", align=ALIGNMENT, font=FONT)
        self.goto(-100, 265)
        self.pencolor("white")
        self.write(f"{self.lives}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.penup()
        self.goto(0, -30)
        self.pencolor("white")
        self.write("GAME OVER", align=ALIGNMENT, font=("Arial", 30, "bold"))

