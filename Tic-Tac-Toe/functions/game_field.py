from config import BLOCK_SIZE

def create_game_field(canvas):
    for i in range(0, BLOCK_SIZE * 3, BLOCK_SIZE):
        canvas.create_line(0, i, BLOCK_SIZE * 3, i)
        canvas.create_line(i, 0, i, BLOCK_SIZE * 3)