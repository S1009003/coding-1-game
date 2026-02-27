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
