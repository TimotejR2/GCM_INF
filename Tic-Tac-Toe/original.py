import tkinter as tk
from functions import create_game_field, write_symbol, get_clicked_position, game_over
from config import BLOCK_SIZE
import sys

game_state = [[None, None, None],
            [None, None, None],
            [None, None, None]]
player = 'O'

def click(data):
    global player, game_state
    horizontal, vertical = get_clicked_position(data.x, data.y)
    
    # If selected move is possible
    if game_state[vertical][horizontal] == None: 
        if data.num == 1:
            if player == 'O':
                write_symbol(canvas, horizontal, vertical, 'O')
                game_state[vertical][horizontal] = 'O'
                player = 'X'

        elif data.num == 3:
            if player == 'X':
                write_symbol(canvas, horizontal, vertical, 'X')
                game_state[vertical][horizontal] = 'X'
                player = 'O'
    if game_over(game_state):
        sys.exit()

canvas = tk.Canvas(width=BLOCK_SIZE * 3, height=BLOCK_SIZE * 3)
canvas.pack()

create_game_field(canvas)

canvas.bind("<Button-1>", click)
canvas.bind("<Button-3>", click)



canvas.mainloop()