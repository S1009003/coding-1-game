# Write your game here
import curses
import time
import random
game_data = {
    'width': 20,
    'height': 20,
    'player': {"x": 0, "y": 0, "score": 0},
     #icons
    'MENS_SYMBOL': {'icon': "\U0001F6B9", 'x': 0, 'y': 0},
    'BLACK_MEDIUM_SQUARE': {'icon': "\U000025FC", 'x': 3, 'y': 3},
    'BLACK_UP-POINTING_DOUBLE_TRIANGLE' : {'icon': "\U000023EB", 'x': 1, 'y': 1},
    'MONEY_BAG' : {'icon': "\U0001F4B0", 'x': 2, 'y': 2}, #💰
    'empty' : "  "
    
    #store curses here
}
# Item to find is a bag of gold 
def draw_board(stdscr):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_WHITE, -1)

    stdscr.clear()
    for y in range(game_data['height']):
        row = ""
        for x in range(game_data['width']):
            # Player
            if x == game_data['player']['x'] and y == game_data['player']['y']:
                row += game_data['MENS_SYMBOL']['icon']
            # Triangle
            elif x == game_data['BLACK_UP-POINTING_DOUBLE_TRIANGLE']['x'] and y == game_data['BLACK_UP-POINTING_DOUBLE_TRIANGLE']['y']:
                 row += game_data['Black_up-pointing_double_triangle']['icon']
            # Obstacles
            elif x == game_data['BLACK_MEDIUM_SQUARE']['x'] and y == game_data['BLACK_MEDIUM_SQUARE']['y']:
                 row += game_data['BLACK_MEDIUM_SQUARE']['icon']
            #any(o['x'] == x and o['y'] == y for o in game_data['BLACK_MEDIUM_SQUARE']):
                 row += game_data['BLACK_MEDIUM_SQUARE']['icon']
            # Collectibles
            elif any(c['x'] == x and c['y'] == y and not c['collected'] for c in game_data['collectibles']):
                 row += game_data['MONEY_BAG']
            else:
                row += game_data['empty']
        stdscr.addstr(y, 0, row, curses.color_pair(1))

    stdscr.refresh()
    stdscr.getkey()  # pause so player can see board

curses.wrapper(draw_board)

    # Print the board and all game elements using curses

# Controls Here

def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()

    if key == "w" and y > game_data['height'] +1:
        new_y += 1
    elif key == "s" and y < game_data['height'] -1:
        new_y -= 1
    elif key == "a" and x > game_data['width'] -1:
        new_x += 1
    elif key == "d" and x < game_data['width'] +1:
        new_x -= 1
    else:
        return  

    if any(o['x'] == new_x and o['y'] == new_y for o in game_data['obstacles']):
        return
    
    