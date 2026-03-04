# Write your game here
import curses
game_data = {
     'width': 5,
    'height': 5,
    'player': {"x": 0, "y": 0, "score": 0}
     #icons
    'MENS_SYMBOL': "/1F6B9"
    'BLACK_MEDIUM_SQUARE' : "/25FC"
    'BLACK_UP-POINTING_DOUBLE_TRIANGLE' : "/23EB"
    
    #store curses here
}
# Item to find is a rflx relic 
def draw_board(screen):
    # Print the board and all game elements using curses

# Controls Here

def move_player(key):
    x = game_data['player']['x']
    y = game_data['player']['y']

    new_x, new_y = x, y
    key = key.lower()

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

    if any(o['x'] == new_x and o['y'] == new_y for o in game_data['obstacles']):
        return