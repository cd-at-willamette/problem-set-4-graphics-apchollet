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
def draw_pyramid():

    gw = GWindow(WIDTH, HEIGHT)

    def n_bricks():
        x = 0
        y = 0
        BB = BRICKS_IN_BASE
        if BRICKS_IN_BASE % 2 == 0: #even
            print(BB)
            y = -h
            for i in range(BB - 1):
                y += h
                x += -w // 2
                for i in range(BB//2):
                    #brick right
                    print('y=', y)
                    print('x=', x)
                    r = GRect((WIDTH // 2) + x, (HEIGHT // 2) - (h // 2) - y, w, h)
                    r.set_color('black')
                    gw.add(r)
                    x += w
                    # brick left
                    r = GRect((WIDTH // 2) - x, (HEIGHT // 2) - (h // 2) - y, w, h)
                    r.set_color('black')
                    gw.add(r)
                    print('y=', y)
                    print('x=', x)
                    BB += -1
            '''x = 0
            # brick middle
            r = GRect((WIDTH // 2) - (w // 2), (HEIGHT // 2) - (h // 2) - h, w, h)
            r.set_color('black')
            gw.add(r)
            for i in range((BRICKS_IN_BASE//2) - 1):
                y += h
                x += w
                print(y)
                # brick right
                r = GRect((WIDTH // 2) - (w // 2) + (x), (HEIGHT // 2) - (h // 2) - y, w, h)
                r.set_color('black')
                gw.add(r)
                # brick left
                r = GRect((WIDTH // 2) - (w // 2) - (x), (HEIGHT // 2) - (h // 2) - y, w, h)
                r.set_color('black')
                gw.add(r)
                print(y)'''
        else: # odd
            print(BRICKS_IN_BASE)
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
                # brick left
                r = GRect((WIDTH // 2) - (w // 2) - (x), (HEIGHT // 2) - (h // 2), w, h)
                r.set_color('black')
                gw.add(r)





        # brick guide
        r = GRect((WIDTH // 2) - (w // 2), (HEIGHT // 2) - (h // 2), w, h)
        r.set_color('yellow')
        gw.add(r)






    n_bricks()
if __name__ == '__main__':
    draw_pyramid()
