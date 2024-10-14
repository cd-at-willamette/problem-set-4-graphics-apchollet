########################################
# Name:
# Collaborators:
# Estimate time spent (hrs):
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():

    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        print("You clicked the window!") # Delete this once you start Part C

    def click_func(e):
        if

        x = e.get_x()
        y = e.get_y()
        gw.box.set_location(x - SQUARE_SIZE//2, y - SQUARE_SIZE//2)
    gw.box = GRect(GW_WIDTH//2 - SQUARE_SIZE//2, GW_HEIGHT//2 - SQUARE_SIZE//2, SQUARE_SIZE, SQUARE_SIZE)
    gw.box.set_filled(True)
    gw.box.set_color('pink')
    gw.add(gw.box)
    # I need to get the edge cords of the box and then use <= and >= to compare x and y to those point to see if
    # clicked in the box then move the box to a random place
    gw.add_event_listener("click", click_func)

    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function

gw = GWindow(GW_WIDTH, GW_HEIGHT)












if __name__ == '__main__':
    clicky_box()
