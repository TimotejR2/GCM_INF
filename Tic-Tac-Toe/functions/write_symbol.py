from config import SYMBOL_SIZE
from .utils import get_block_mid


def write_X(canvas, x, y):
    canvas.create_line(x - SYMBOL_SIZE, y - SYMBOL_SIZE, x + SYMBOL_SIZE, y + SYMBOL_SIZE)
    canvas.create_line(x + SYMBOL_SIZE, y - SYMBOL_SIZE, x - SYMBOL_SIZE, y + SYMBOL_SIZE)

def write_O(canvas, x, y):
    canvas.create_oval(x - SYMBOL_SIZE, y - SYMBOL_SIZE, x + SYMBOL_SIZE, y + SYMBOL_SIZE)

def write_symbol(canvas, horizontal, vertical, symbol): # napr. 0,0   2,2
    x_mid, y_mid = get_block_mid(horizontal, vertical)
    if symbol == 'O':
        write_O(canvas, x_mid, y_mid)
    elif symbol == 'X':
        write_X(canvas, x_mid, y_mid)