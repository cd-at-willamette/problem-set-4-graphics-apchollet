########################################
# Name:Aly Chollet
# Collaborators:Sophie
# Estimated time spent (hrs): 3
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 5
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
            for i in range(BB - b):
                r = GRect((WIDTH // 2) - (w*BB//2) + (x) + (w//2 *b), (HEIGHT // 2) + (h//2 * BB) // 2 - (h * b) , w, h)
                r.set_color('red')
                gw.add(r)
                x += w
            x = 0
            b += 1

    n_bricks()
if __name__ == '__main__':
    draw_pyramid()
