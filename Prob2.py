########################################
# Name:Aly Chollet
# Collaborators:
# Estimated time spent (hrs):
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 6
#bricks width and height
w = 50 #brick width
h = 25 #brick height
BB = BRICKS_IN_BASE
x = 0
y = 0
b = 0
def draw_pyramid():

    gw = GWindow(WIDTH, HEIGHT)

    def n_bricks():
        global x #ACROSS
        global y #UP
        global b # to reduce BB

        for i in range(BB):
            r = GRect((WIDTH // 2) - w*BB//2 + x, (HEIGHT // 2), w, h)
            r.set_color('red')
            gw.add(r)
            x += w
        x = 0
        for i in range(BB -1):
            r = GRect((WIDTH // 2) - w * (BB-1) // 2 + x, (HEIGHT // 2) - h+y, w, h)
            r.set_color('red')
            gw.add(r)
            x += w
        x = 0
        for i in range(BB - 2):
            r = GRect((WIDTH // 2) - w * (BB - 2) // 2 + x, (HEIGHT // 2) - h*2 + y, w, h)
            r.set_color('red')
            gw.add(r)
            x += w

        r = GRect((WIDTH // 2) - (w // 2), (HEIGHT // 2), w, h)
        r.set_color('blue')
        gw.add(r)

    n_bricks()
if __name__ == '__main__':
    draw_pyramid()
