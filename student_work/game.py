# Write your game here
import curses

game_data = {
    'width': 10,
    'height': 10,
    'player': {"x": 0, "y": 0, "score": 0},
    'MENS_SYMBOL': {'icon': "P "},
    'MONEY_BAG': {'icon': "$ ", 'x': 5, 'y': 5},
    'OBSTACLE': {'icon': "X ", 'x': 3, 'y': 3},
    'UP_TRIANGLE': {'icon': "^ ", 'x': 1, 'y': 1},
    'empty': ". ",
    'game_over': False
}

def draw_board(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(False)

    while not game_data['game_over']:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Score: {game_data['player']['score']} | WASD to move, Q to quit")

        for y in range(game_data['height']):
            for x in range(game_data['width']):
                char = game_data['empty']
                if x == game_data['player']['x'] and y == game_data['player']['y']:
                    char = game_data['MENS_SYMBOL']['icon']
                elif x == game_data['MONEY_BAG']['x'] and y == game_data['MONEY_BAG']['y']:
                    char = game_data['MONEY_BAG']['icon']
                elif x == game_data['OBSTACLE']['x'] and y == game_data['OBSTACLE']['y']:
                    char = game_data['OBSTACLE']['icon']
                elif x == game_data['UP_TRIANGLE']['x'] and y == game_data['UP_TRIANGLE']['y']:
                    char = game_data['UP_TRIANGLE']['icon']
                
                stdscr.addstr(y + 1, x * 2, char)

        stdscr.refresh()
        key = stdscr.getch()
        
        try:
            key_char = chr(key).lower()
        except:
            key_char = ""

        if key_char == 'q':
            break
        
        move_player(key_char)

def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']
    new_x, new_y = x, y

    if key == "w" and y > 0:
        new_y -= 1
    elif key == "s" and y < game_data['height'] - 1:
        new_y += 1
    elif key == "a" and x > 0:
        new_x -= 1
    elif key == "d" and x < game_data['width'] - 1:
        new_x += 1
    else:
        return  

    if new_x == game_data['OBSTACLE']['x'] and new_y == game_data['OBSTACLE']['y']:
        return

    if new_x == game_data['MONEY_BAG']['x'] and new_y == game_data['MONEY_BAG']['y']:
        game_data['player']['score'] += 10
        game_data['MONEY_BAG']['x'], game_data['MONEY_BAG']['y'] = -1, -1 

    game_data['player']['x'] = new_x
    game_data['player']['y'] = new_y

if __name__ == "__main__":
    curses.wrapper(draw_board)