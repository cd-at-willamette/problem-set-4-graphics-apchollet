########################################
# Name: Aly
# Collaborators: Sophie
# Estimate time spent (hrs): 4
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 20                       # Distance from left of window to origin
SCORE_DY = 20                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score
c = random.randint(60, 440)
d = random.randint(60, 440)
score = 0
def clicky_box():
    message = GLabel(str(score), SCORE_DX, GW_HEIGHT - SCORE_DY)
    message.set_font(SCORE_FONT)
    gw.message = message
    gw.add(gw.message)
    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        print("You clicked the window!") # Delete this once you start Part C

    def click_func(e): # compare x to c and d if x is in the range
        global c
        global d
        global score
        x = e.get_x()
        y = e.get_y()
        print('x,y =', x,y)
        if c <= x <= (c+ SQUARE_SIZE) and d <= y <= (d + SQUARE_SIZE):
            c = random.randint(60, 450)
            d = random.randint(60, 450)
            gw.box.set_location(c, d)
            print(True)
            #set score +1
            r = GRect(SCORE_DX, GW_HEIGHT - SCORE_DY -50, 60, 60)
            r.set_filled(True)
            r.set_fill_color("white")
            r.set_color('white')
            gw.add(r)
            score += 1
            score_str = str(score)
            message = GLabel(str(score), SCORE_DX, GW_HEIGHT - SCORE_DY)
            message.set_font(SCORE_FONT)
            gw.message = message
            gw.add(gw.message)
            print(score)
        else:
            r = GRect(SCORE_DX, GW_HEIGHT - SCORE_DY - 50, 60, 60)
            r.set_filled(True)
            r.set_fill_color("white")
            r.set_color('white')
            gw.add(r)
            print(False)
            score = 0
            print(score)
            score_str = str(score)
            message = GLabel(str(score), SCORE_DX, GW_HEIGHT - SCORE_DY)
            message.set_font(SCORE_FONT)
            gw.message = message
            gw.add(gw.message)
            # set score 0
    gw.box = GRect(c , d, SQUARE_SIZE, SQUARE_SIZE)
    gw.box.set_filled(True)
    gw.box.set_color('pink')
    gw.add(gw.box)
    gw.add_event_listener("click", click_func)
gw = GWindow(GW_WIDTH, GW_HEIGHT)


if __name__ == '__main__':
    clicky_box()
