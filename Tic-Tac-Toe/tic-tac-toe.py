import tkinter as tk
from functions import create_game_field, write_symbol, get_clicked_position, game_over
from config import BLOCK_SIZE

class TicTacToe:
    def __init__(self):
        self.game_state = [[None, None, None],
                           [None, None, None],
                           [None, None, None]]
        self.player = 'O'
        self.canvas = tk.Canvas(width=BLOCK_SIZE * 3, height=BLOCK_SIZE * 3)
        self.canvas.pack()

    def click(self, data):
        horizontal, vertical = get_clicked_position(data.x, data.y)
        
        if self.game_state[vertical][horizontal] is None:
            if data.num == 1 and self.player == 'O':
                self.make_move('O', horizontal, vertical)
            elif data.num == 3 and self.player == 'X':
                self.make_move('X', horizontal, vertical)

    def make_move(self, symbol, horizontal, vertical):
        write_symbol(self.canvas, horizontal, vertical, symbol)
        self.game_state[vertical][horizontal] = symbol
        self.player = 'X' if symbol == 'O' else 'O'

        if game_over(self.game_state):
            print("Game Over!")
            self.canvas.quit()

    def run_game(self):
        create_game_field(self.canvas)
        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<Button-3>", self.click)
        self.canvas.mainloop()


game = TicTacToe()
game.run_game()
