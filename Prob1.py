############################################################
# Name: Aly Chollet
# Name(s) of anyone worked with:
# Est time spent (hr): 1.3
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600


def draw_image():
    w = WIDTH
    h = HEIGHT

    def sun_and_water():
        # black frame
        r = GRect(0, 0, w, h)
        r.set_filled(True)
        r.set_fill_color("black")
        r.set_color('black')
        gw.add(r)

        # white fill
        r = GRect(50, 50, 500, 500)
        r.set_filled(True)
        r.set_fill_color("light blue")
        r.set_color('light blue')
        gw.add(r)

        #black oval line
        #(right, down, rs, ls)
        o = GOval(255,160, 90, 90)
        o.set_filled(True)
        o.set_fill_color("red")
        o.set_color('red')
        gw.add(o)

        # black oval fill
        # (right, down, rs, ls)
        o = GOval(255, 160, 85, 85)
        o.set_filled(True)
        o.set_fill_color("orange")
        o.set_color('orange')
        gw.add(o)

        # water
        r = GRect(50, 300, 500, 300)
        r.set_filled(True)
        r.set_fill_color("blue")
        r.set_color('blue')
        gw.add(r)
        # water glow
        r = GRect(50, 300, 500, 10)
        r.set_filled(True)
        r.set_fill_color("blue")
        r.set_color('blue')
        gw.add(r)

        # water glow
        r = GRect(0, 550, w, 50)
        r.set_filled(True)
        r.set_fill_color("black")
        r.set_color('black')
        gw.add(r)

        # text
        gw.add(GLabel("sun?", 100, 100))
        gw.add(GLabel("water?", 450, 500))
        gw.add(GLine(0,w//2,w,w//2))

    #call code here :3
    sun_and_water()




gw = GWindow(600, 600)

if __name__ == '__main__':
    draw_image()
