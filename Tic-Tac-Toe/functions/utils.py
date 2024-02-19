from config import BLOCK_SIZE

def get_clicked_position(x, y):
    horizontal = x // BLOCK_SIZE
    vertical = y // BLOCK_SIZE
    return horizontal, vertical

def get_block_mid(horizontal, vertical):
    
    x_mid = (horizontal*BLOCK_SIZE) + (BLOCK_SIZE/2)
    y_mid = (vertical*BLOCK_SIZE) + (BLOCK_SIZE/2)
    return x_mid, y_mid

def game_over(game_state):
    for row in game_state:
        if row[0] == row[1] and row[1] == row[2] and row[0] != None:
            print('Player ' + row[0] + ' won')
            return True
    for i in range(3):
        if game_state[0][i] == game_state[1][i] and  game_state[1][i] ==  game_state[2][i] and  game_state[1][i] != None:
            print('Player ' + game_state[0][i] + ' won')
            return True

    if game_state[0][0] == game_state[1][1] and  game_state[1][1] ==  game_state[2][2] and  game_state[1][1] != None:
        print('Player ' +  game_state[1][1] + ' won')
        return True

    if game_state[0][2] == game_state[1][1] and  game_state[1][1] ==  game_state[2][0] and  game_state[1][1] != None:
        print('Player ' +  game_state[1][1] + ' won')
        return True      

    if not any(None in sublist for sublist in game_state):
        print('Tie')
        return True

    return False
