import os

# Initialize the game board
game_board = [
    ['P', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', 'K', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-'],
    ['D', '-', '-', '-', '-', '-', '-'],
    ['-', '-', '-', '-', '-', '-', '-']
]

# Player position
player_pos = [0, 0]
# Key position
key_pos = [1, 4]
# Door position
door_pos = [3, 0]

# Game state
has_key = False

def print_board():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal screen
    for row in game_board:
        print(' '.join(row))
    print("\n== THE ESCAPE GAME ==")
    print("Use W A S D to move (P)layer.")
    print("Find (K)ey first then exit through the (D)oor.")

def move_player(direction):
    global player_pos, key_pos, has_key  # Use global keyword to reference global variables
    x, y = player_pos
    if direction == 'W' and x > 0:
        x -= 1
    elif direction == 'S' and x < len(game_board) - 1:
        x += 1
    elif direction == 'A' and y > 0:
        y -= 1
    elif direction == 'D' and y < len(game_board[0]) - 1:
        y += 1

    # Update game board
    game_board[player_pos[0]][player_pos[1]] = '-'
    player_pos = [x, y]
    
    # Check for key
    if player_pos == key_pos:
        has_key = True
        key_pos = []
    
    game_board[player_pos[0]][player_pos[1]] = 'P'
    
    # Check for door
    if player_pos == door_pos:
        if has_key:
            print_board()
            print("Congratulations! You've escaped the game.")
            return True
        else:
            print_board()
            print("You need the key first!")
            return False
    return None

# Main game loop
def main():
    print_board()
    while True:
        move = input("Enter your move (W/A/S/D): ").upper()
        if move in ['W', 'A', 'S', 'D']:
            game_over = move_player(move)
            print_board()
            if game_over is not None:
                break

if __name__ == "__main__":
    main()
