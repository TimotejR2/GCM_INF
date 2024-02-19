import tkinter as tk
import random

root = tk.Tk()
game_canvas = tk.Canvas(root)
game_canvas.pack()

player_score = 0

# Create game environment
for i in range(0, 500, 30):
    game_canvas.create_line(0, i, 500, i)
    game_canvas.create_line(i, 0, i, 500)

game_canvas.create_rectangle(0, 0, 30, 30, fill="blue", tag="correct")
correct_rect_x = 0
correct_rect_y = 0

game_canvas.create_rectangle(0, 0, 30, 30, fill="red", tag="incorrect")
incorrect_rect_x = 0
incorrect_rect_y = 0

def move_rectangles():
    global correct_rect_x, correct_rect_y, incorrect_rect_x, incorrect_rect_y
    correct_rect_x = random.randrange(0, 360, 30)
    correct_rect_y = random.randrange(0, 270, 30)

    incorrect_rect_x = random.randrange(0, 360, 30)
    incorrect_rect_y = random.randrange(0, 270, 30)
    
    game_canvas.coords("correct", correct_rect_x, correct_rect_y, correct_rect_x + 30, correct_rect_y + 30)

    game_canvas.coords("incorrect", incorrect_rect_x, incorrect_rect_y, incorrect_rect_x + 30, incorrect_rect_y + 30)

    game_canvas.update()

    game_canvas.after(1000 - player_score * 50, move_rectangles)

move_rectangles()

def handle_click(event):
    global correct_rect_x, correct_rect_y, incorrect_rect_x, incorrect_rect_y, player_score
    mid_x, mid_y = calculate_mid_point(event.x, event.y)

    if is_collision(mid_x, mid_y, incorrect_rect_x, incorrect_rect_y):
        game_canvas.quit()
    elif is_collision(mid_x, mid_y, correct_rect_x, correct_rect_y):
        player_score += 1
    else:
        player_score -= 1
    print("Score:", player_score)

def calculate_mid_point(x, y):
    return x // 30 * 30, y // 30 * 30

def is_collision(x1, y1, x2, y2):
    return x1 == x2 and y1 == y2


game_canvas.bind("<Button-1>", handle_click)
root.mainloop()