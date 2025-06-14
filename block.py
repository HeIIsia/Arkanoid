from turtle import Turtle

class BlockManager(Turtle):
    def __init__(self, color, starting_pos, score):
        self.STARTING_POSITIONS = starting_pos
        self.score = score
        self.blocks_count = len(starting_pos)
        self.color = color
        self.all_blocks = []
        self.create_blocks()

    def add_blocks(self, position):
        new_block = Turtle("square")
        new_block.shapesize(stretch_wid=1, stretch_len=2.5)
        new_block.penup()
        new_block.pencolor("black")
        new_block.fillcolor(self.color)
        new_block.goto(position)
        self.all_blocks.append(new_block)

    def create_blocks(self):
        for position in self.STARTING_POSITIONS:
            self.add_blocks(position)

    def remove_block(self):
        self.goto(0, 400)

