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
x = 0
y = 0

def draw_pyramid():

    gw = GWindow(WIDTH, HEIGHT)




    def n_bricks():
        x = 0
        y = h
        if BRICKS_IN_BASE % 2 == 0:
            print("even")
            # brick right
            r = GRect((WIDTH // 2), (HEIGHT // 2) - (h // 2), w, h)
            r.set_color('black')
            gw.add(r)
            # brick left
            r = GRect((WIDTH // 2) - w, (HEIGHT // 2) - (h // 2), w, h)
            r.set_color('black')
            gw.add(r)
            # brick middle
            r = GRect((WIDTH // 2) - (w // 2), (HEIGHT // 2) - (h // 2), w, h)
            r.set_color('yellow')
            gw.add(r)

            #_______________________
            # brick middle up
            r = GRect((WIDTH // 2) - (w // 2), (HEIGHT // 2) - (h // 2) - h, w, h)
            r.set_color('red')
            gw.add(r)
            y += h

            for i in range((BRICKS_IN_BASE - 2)//2):
                #brick
                x += w
                r = GRect((WIDTH // 2) + x, (HEIGHT // 2) - (h // 2), w, h)
                r.set_color('black')
                gw.add(r)
                x += w
                # brick
                r = GRect((WIDTH // 2) - x, (HEIGHT // 2) - (h // 2), w, h)
                r.set_color('black')
                gw.add(r)
                x -= w

        else:  # odd
            print("odd")
            # brick middle
            r = GRect((WIDTH // 2) - (w // 2), (HEIGHT // 2) - (h // 2), w, h)
            r.set_color('black')
            gw.add(r)
            for i in range(BRICKS_IN_BASE//2):
                #brick right
                x += w
                r = GRect((WIDTH//2) - (w//2) + (x), (HEIGHT//2) - (h//2), w, h)
                r.set_color('black')
                gw.add(r)
                print(x)
                # brick left
                r = GRect((WIDTH // 2) - (w // 2) - (x), (HEIGHT // 2) - (h // 2), w, h)
                r.set_color('black')
                gw.add(r)
                print(x)


    n_bricks()



if __name__ == '__main__':
    draw_pyramid()
