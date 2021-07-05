import pygame,sys,os


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (115,80)
pygame.init()

BLACK = (0, 0, 0)
GREEN = (2, 26, 14)
BLUE = (0, 0, 51)
PURPLE = (51,0,51)
WHITE = (255, 255, 255)

APPLE_SIZE = 50
panda_width = 50
FPS = 15
TOP_WIDTH = 40

emoji_size = 30

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
vel = 2
vel2 = 5
VELOCITY = 10

ghost = pygame.image.load('imgs/ghost.png')
dunya = pygame.image.load('imgs/dunn.png')
bgg = pygame.image.load('imgs/bg.png')
bg = pygame.image.load('imgs/bg2.png')
win = pygame.image.load('imgs/winn.png')
canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("WorldGame")
clock = pygame.time.Clock()

#font
medium_font = pygame.font.SysFont('Arial Narrow', 35, True)
large_font = pygame.font.SysFont('Rockwell', 51, True)
large_fonntt = pygame.font.SysFont('Rockwell Extra Bold', 105, True)
large_fontttt = pygame.font.SysFont('Rockwell', 45, True)


#appleImages
apple =pygame.image.load('imgs/apple.png')
apple2 = pygame.image.load('imgs/apple2.png')

#emojies
emoji1 = pygame.image.load('imgs/emoji1.png')
emoji2 = pygame.image.load('imgs/emoji2.png')
emoji3 = pygame.image.load('imgs/emoji3.png')
emoji4 = pygame.image.load('imgs/emoji4.png')
emoji5 = pygame.image.load('imgs/emoji5.png')
emoji6 = pygame.image.load('imgs/emoji6.png')
emoji7 = pygame.image.load('imgs/emoji7.png')
emoji8 = pygame.image.load('imgs/emoji8.png')
emoji9 = pygame.image.load('imgs/emoji9.png')
emoji10 = pygame.image.load('imgs/emoji10.png')


bfs = pygame.image.load('imgs/bfs.png')
dfs = pygame.image.load('imgs/dfs.png')
ucs = pygame.image.load('imgs/ucs.png')
a = pygame.image.load('imgs/a.png')











#panda
normall = pygame.image.load('imgs/pandadown.png')


def start_game():
    canvas.blit(bgg, (0, 0))
    start_font1 = large_font.render("Welcome to panda game", True, BLACK, )
    start_font1_rect = start_font1.get_rect()
    start_font1_rect.center = (650, 120)
    canvas.blit(start_font1, start_font1_rect)
    class button():
        def __init__(self, color, x, y, width, height, text=''):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text
            self.color = color

        def buttons(self, win, outline=None):
            if outline:
                pygame.draw.rect(win, outline, (self.x - 8, self.y - 8, self.width + 2, self.height + 2), 0)

            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pygame.font.SysFont('Berlin Sans FB', 30)
                # text color
                text = font.render(self.text, 1, (255, 255, 255))
                win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))
        def isOver(self, pos):
            # pos is the mouse postion or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
            return False

    dfs = button((0, 0, 51), 360, 190, 170, 60, 'DFS')
    bfs = button((0, 0, 51), 570, 190, 170, 60, 'BFS')
    ucs = button((0, 0, 51), 770, 190, 170, 60, 'UCS')
    a = button((0, 0, 51), 460, 300, 170, 60, 'A*')
    play = button((0, 0, 51), 680, 300, 170, 60, 'play :)')
    instruction = button((2, 26, 14), 460, 420, 170, 50, 'instruction')
    quittt = button((2, 26, 14), 680, 420, 170, 50, 'Quit')

    canvas.blit(dunya, (-55, 0))

    dfs.buttons(canvas, (0, 0, 0))
    bfs.buttons(canvas, (0, 0, 0))
    ucs.buttons(canvas, (0, 0, 0))
    a.buttons(canvas, (0, 0, 0))
    play.buttons(canvas, (0, 0, 0))
    instruction.buttons(canvas, (0, 0, 0))
    quittt.buttons(canvas, (0, 0, 0))
    pygame.display.update()
    while True:
        pygame.display.update()
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dfs.isOver(pos):
                    dfs1()
                if bfs.isOver(pos):
                    bfs1()
                if ucs.isOver(pos):
                    ucs1()
                if a.isOver(pos):
                    a1()
                if instruction.isOver(pos):
                    start_inst()
                if play.isOver(pos):

                    gameloop()
                if quittt.isOver(pos):
                    pygame.quit()
                    sys.exit()


        pygame.display.update()

def start_inst():
    canvas.blit(bgg, (0, 0))
    instruct = medium_font.render("1) Try to eat red apples and the destination(Yellow) apple ", True, BLACK)
    instruct2 = medium_font.render("2) Escape from emojis", True, BLACK)
    insruct3 = medium_font.render("3) Be careful about time choose the short distance",True,BLACK)
    instruct4 = medium_font.render("back", True, PURPLE)
    instruct4R = instruct4.get_rect()
    instruct4R.center = (1125 - 100, 625 - 100)
    canvas.blit(instruct, (1125 / 8, 625 / 2.5))
    canvas.blit(instruct2, (1125 / 8, 625 / 2.5 + 30))
    canvas.blit(insruct3, (1125 / 8, 625 / 2.5 + 60))
    canvas.blit(instruct4, instruct4R)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > instruct4R.left and x < instruct4R.right:
                    if y > instruct4R.top and y < instruct4R.bottom:
                         start_game()
        pygame.display.update()


def gameover():
    #canvas.fill(BLACK)
    canvas.blit(bg, (0, 0))
    canvas.blit(ghost, (220, 70))


    font_gameover1 = large_fonntt.render('GAME OVER', True, GREEN,WHITE)
    font_gameover2 = large_fonntt.render("Play Again", True, GREEN,WHITE)
    font_gameover3 = large_fonntt.render("Quit", True, GREEN,WHITE)

    font_gameover1_rect = font_gameover1.get_rect()
    font_gameover2_rect = font_gameover2.get_rect()
    font_gameover3_rect = font_gameover3.get_rect()


    font_gameover1_rect.center = (550,300)
    font_gameover2_rect.center = (550, 390)
    font_gameover3_rect.center = (550, 480)


    canvas.blit(font_gameover1, font_gameover1_rect)
    canvas.blit(font_gameover2, font_gameover2_rect)
    canvas.blit(font_gameover3, font_gameover3_rect)
    pandalength = 0


    pygame.mixer.music.stop()
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > font_gameover2_rect.left and x < font_gameover2_rect.right:
                    if y > font_gameover2_rect.top and y < font_gameover2_rect.bottom:
                        gameloop()
                if x > font_gameover3_rect.left and x < font_gameover3_rect.right:
                    if y > font_gameover3_rect.top and y < font_gameover3_rect.bottom:
                        pygame.mixer.music.stop()
                        start_game()
                    pygame.display.update()


        pygame.display.update()


def emoji(emojilist, dir):
    if dir == 'left':
        emo1 = pygame.transform.rotate(emoji1, 360)
    if dir == 'right':
        emo1 = pygame.transform.rotate(emoji1, 360)

    canvas.blit(emo1, emojilist[-1])

def emojii2(emojilist2, dir2):
     if dir2 == 'down':
        emo2 = pygame.transform.rotate(emoji2, 360)
     if dir2 == 'up':
         emo2 = pygame.transform.rotate(emoji2, 360)
     canvas.blit(emo2, emojilist2[-1])


def emojii3(emojilist3, dir3):
    if dir3 == 'up':
        emo3 = pygame.transform.rotate(emoji3, 360)
    if dir3 == 'down':
        emo3 = pygame.transform.rotate(emoji3, 360)
    canvas.blit(emo3, emojilist3[-1])


def emojii4(emojilist4, dir4):
    if dir4 == 'right':
        emo4 = pygame.transform.rotate(emoji4, 360)
    if dir4 == 'left':
        emo4 = pygame.transform.rotate(emoji4, 360)

    canvas.blit(emo4, emojilist4[-1])


def emojii5(emojilist5, dir5):
    if dir5 == 'left':
        emo5 = pygame.transform.rotate(emoji5, 360)
    if dir5 == 'right':
        emo5 = pygame.transform.rotate(emoji5, 360)
    canvas.blit(emo5, emojilist5[-1])

def emojii6(emojilist6, dir6):
    if dir6 == 'down':
        emo6 = pygame.transform.rotate(emoji6, 360)
    if dir6 == 'up':
        emo6 = pygame.transform.rotate(emoji6, 360)
    canvas.blit(emo6, emojilist6[-1])


def emojii7(emojilist7, dir7):
    if dir7 == 'up':
        emo7 = pygame.transform.rotate(emoji7, 360)
    if dir7 == 'down':
        emo7 = pygame.transform.rotate(emoji7, 360)
    canvas.blit(emo7, emojilist7[-1])



def emojii8(emojilist8, dir8):
    if dir8 == 'right':
        emo8 = pygame.transform.rotate(emoji8, 360)
    if dir8 == 'left':
        emo8 = pygame.transform.rotate(emoji8, 360)
    canvas.blit(emo8, emojilist8[-1])

def emojii9(emojilist9, dir9):
    if dir9 == 'right':
        emo9 = pygame.transform.rotate(emoji9, 360)
    if dir9 == 'left':
        emo9 = pygame.transform.rotate(emoji9, 360)
    canvas.blit(emo9, emojilist9[-1])

def emojii10(emojilist10, dir10):
    if dir10 == 'down':
        emo10 = pygame.transform.rotate(emoji10, 360)
    if dir10 == 'up':
        emo10 = pygame.transform.rotate(emoji10, 360)
    canvas.blit(emo10, emojilist10[-1])

def panda(pandalist, direction):

    if direction == 'none':
        head = pygame.transform.rotate(normall, 360)
    if direction == 'right':
        head = pygame.transform.rotate(normall, 90)

    if direction == 'left':
        head = pygame.transform.rotate(normall, 270)
    if direction == 'up':
        head = pygame.transform.rotate(normall, 180)

    if direction == 'down':
        head = pygame.transform.rotate(normall, 360)
    canvas.blit(head, pandalist[-1])



def bfs1():
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(-1, 0.0)
    while True:
        panda_x = 0
        panda_y = 0
        direction = 'right'
        pandalist = []
        APPLE_X = 450
        APPLE_Y = 100
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x > back2R.left and x <back2R.right:
                        if y > back2R.top and y < back2R.bottom:
                              pygame.mixer.music.stop()
                              start_game()
                        pygame.display.update()


            panda_head_rect = pygame.Rect(panda_x, panda_y, panda_width, panda_width)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)
            if direction == 'right':
                panda_x += VELOCITY
                if panda_x > WINDOW_WIDTH - panda_width:
                    direction = 'down'
            if direction == 'down':
                panda_y += VELOCITY
                if panda_y > 40:
                     direction = 'left'
            if direction == 'left':
                panda_x -= VELOCITY
                if panda_x < 0:
                      direction = 'down'
            if direction == 'down':
                panda_y += VELOCITY
                if panda_y > 90:
                   direction = 'right'
            if panda_y > 90 and panda_head_rect.colliderect(apple_rect):
                        you_win3()



            pandahead = []
            pandahead.append(panda_x)
            pandahead.append(panda_y)
            pandalist.append(pandahead)
            canvas.blit(bfs, (0, 0))
            back2 = medium_font.render("back ", True, WHITE, BLUE)
            back2R = back2.get_rect()
            back2R.center = (35, 587)
            canvas.blit(back2,back2R)

            panda(pandalist, direction)
            canvas.blit(apple, (APPLE_X, APPLE_Y))
            clock.tick(FPS)
            pygame.display.update()

def dfs1():
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(-1, 0.0)
    while True:
        panda_x = 0
        panda_y = 0
        direction = 'down'
        pandalist = []
        APPLE_X = 250
        APPLE_Y = 400
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x > back2R.left and x < back2R.right:
                        if y > back2R.top and y < back2R.bottom:
                            pygame.mixer.music.stop()
                            start_game()
                        pygame.display.update()

            panda_head_rect = pygame.Rect(panda_x, panda_y, panda_width, panda_width)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)
            if direction == 'down':
                panda_y += vel
                if panda_y > WINDOW_HEIGHT - panda_width:
                    panda_x = 50
                    panda_y = 0
            if direction == 'down':
                panda_y += vel
                if panda_y > WINDOW_HEIGHT - panda_width:
                    panda_x = 100
                    panda_y = 0
            if direction == 'down':
                panda_y += vel
                if panda_y > WINDOW_HEIGHT - panda_width:
                    panda_x = 150
                    panda_y = 0
            if direction == 'down':
                panda_y += vel
                if panda_y > WINDOW_HEIGHT - panda_width:
                    panda_x = 200
                    panda_y = 0
            if direction == 'down':
                panda_y += vel
                if panda_y > WINDOW_HEIGHT - panda_width:
                    panda_x = 250
                    panda_y = 0
            if panda_head_rect.colliderect(apple_rect):
                  you_win2()

            pandahead = []
            pandahead.append(panda_x)
            pandahead.append(panda_y)
            pandalist.append(pandahead)
            canvas.blit(dfs, (0, 0))
            back2 = medium_font.render("back ", True, WHITE, BLUE)
            back2R = back2.get_rect()
            back2R.center = (35, 587)
            canvas.blit(back2, back2R)

            panda(pandalist, direction)
            canvas.blit(apple, (APPLE_X, APPLE_Y))
            clock.tick(FPS)
            pygame.display.update()



def ucs1():
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(-1, 0.0)

    while True:
        panda_x = 0
        panda_y = 0
        direction = 'right'
        pandalist = []
        APPLE_X = 250
        APPLE_Y = 0
        APPLE_X2 = 250
        APPLE_Y2 = 400
        APPLE_X3 = 1050
        APPLE_Y3 = 400
        APPLE_X4 = 1050
        APPLE_Y4 = 550
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x > back2R.left and x < back2R.right:
                        if y > back2R.top and y < back2R.bottom:
                            pygame.mixer.music.stop()
                            start_game()
                        pygame.display.update()

            panda_head_rect = pygame.Rect(panda_x, panda_y, panda_width, panda_width)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)
            apple_rect2 = pygame.Rect(APPLE_X2, APPLE_Y2, APPLE_SIZE, APPLE_SIZE)
            apple_rect3 = pygame.Rect(APPLE_X3, APPLE_Y3, APPLE_SIZE, APPLE_SIZE)
            apple_rect4 = pygame.Rect(APPLE_X4, APPLE_Y4, APPLE_SIZE, APPLE_SIZE)

            if direction == 'right':
                panda_x += vel2
                if panda_x == 1050:
                    direction = 'down'
            if direction == 'down':
                panda_y += vel2
                if panda_y == 400:
                    direction = 'right'
            if direction == 'right':
                panda_x += vel2
                if panda_x == 250:
                    direction = 'down'

            if panda_head_rect.colliderect(apple_rect):
                     APPLE_X = -300
                     APPLE_Y = -300
            if panda_head_rect.colliderect(apple_rect2):
                     APPLE_X2 = -300
                     APPLE_Y2 = -300
            if panda_head_rect.colliderect(apple_rect3):
                    APPLE_X3 = -300
                    APPLE_Y3 = -300
            if panda_head_rect.colliderect(apple_rect4):
                    APPLE_X4 = -300
                    APPLE_Y4 = -300
                    you_win4()
            pandahead = []
            pandahead.append(panda_x)
            pandahead.append(panda_y)
            pandalist.append(pandahead)
            canvas.blit(ucs, (0, 0))
            back2 = medium_font.render("back ", True, WHITE, BLUE)
            back2R = back2.get_rect()
            back2R.center = (35, 587)
            canvas.blit(back2, back2R)


            panda(pandalist, direction)
            canvas.blit(apple, (APPLE_X, APPLE_Y))
            canvas.blit(apple, (APPLE_X2, APPLE_Y2))
            canvas.blit(apple, (APPLE_X3, APPLE_Y3))
            canvas.blit(apple2, (APPLE_X4, APPLE_Y4))
            clock.tick(FPS)
            pygame.display.update()


def a1():
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(-1, 0.0)
    while True:
        panda_x = 0
        panda_y = 0
        direction = 'right'
        pandalist = []
        APPLE_X = 1050
        APPLE_Y = 550
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x > back2R.left and x < back2R.right:
                        if y > back2R.top and y < back2R.bottom:
                            pygame.mixer.music.stop()
                            start_game()
                        pygame.display.update()
            panda_head_rect = pygame.Rect(panda_x, panda_y, panda_width, panda_width)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)

            if direction == 'right':
                panda_x += vel2
                if panda_x == 250:
                    direction = 'down'
            if direction == 'down':
                panda_y += vel2
                if panda_y == 400:
                    direction = 'down'
            if direction == 'right':
                panda_x += vel2
                if panda_x == 1050:
                    direction = 'down'



            if panda_head_rect.colliderect(apple_rect):
                you_win()

            pandahead = []
            pandahead.append(panda_x)
            pandahead.append(panda_y)
            pandalist.append(pandahead)
            canvas.blit(a, (0, 0))
            back2 = medium_font.render("back ", True, WHITE, BLUE)
            back2R = back2.get_rect()
            back2R.center = (35, 587)
            canvas.blit(back2, back2R)

            panda(pandalist, direction)
            canvas.blit(apple, (APPLE_X, APPLE_Y))
            clock.tick(FPS)
            pygame.display.update()
#for a*
def you_win():
    canvas.blit(bgg, (0, 0))
    canvas.blit(win, (10, 10))
    instruct = medium_font.render("1) Nodes expanded:  33  ", True,BLACK)
    instruct2 = medium_font.render("2) cost:  32", True, BLACK)
    insruct3 = medium_font.render("3) Score: 100 ", True, BLACK)
    instruct4 = medium_font.render("back", True, PURPLE)
    instruct4R = instruct4.get_rect()
    instruct4R.center = (1000, 500 )
    canvas.blit(instruct, (520 , 150))
    canvas.blit(instruct2, (520,200 ))
    canvas.blit(insruct3, (520,250))
    canvas.blit(instruct4, instruct4R)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > instruct4R.left and x < instruct4R.right:
                    if y > instruct4R.top and y < instruct4R.bottom:
                        pygame.mixer.music.stop()
                        start_game()

        pygame.display.update()
# for dfs
def you_win2():
    canvas.blit(bgg, (0, 0))
    canvas.blit(win, (10, 10))
    instruct = medium_font.render("1) Nodes expanded:  33  ", True,BLACK)
    instruct2 = medium_font.render("2) cost:  53", True, BLACK)
    insruct3 = medium_font.render("3) Score: 100 ", True, BLACK)
    instruct4 = medium_font.render("back", True, PURPLE)
    instruct4R = instruct4.get_rect()
    instruct4R.center = (1000, 500 )
    canvas.blit(instruct, (520 , 150))
    canvas.blit(instruct2, (520,200 ))
    canvas.blit(insruct3, (520,250))
    canvas.blit(instruct4, instruct4R)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > instruct4R.left and x < instruct4R.right:
                    if y > instruct4R.top and y < instruct4R.bottom:
                        pygame.mixer.music.stop()
                        start_game()

        pygame.display.update()
#bfs
def you_win3():
    canvas.blit(bgg, (0, 0))
    canvas.blit(win, (10, 10))
    instruct = medium_font.render("1) Nodes expanded:  52  ", True,BLACK)
    instruct2 = medium_font.render("2) cost:  51", True, BLACK)
    insruct3 = medium_font.render("3) Score: 100 ", True, BLACK)
    instruct4 = medium_font.render("back", True, PURPLE)
    instruct4R = instruct4.get_rect()
    instruct4R.center = (1000, 500 )
    canvas.blit(instruct, (520 , 150))
    canvas.blit(instruct2, (520,200 ))
    canvas.blit(insruct3, (520,250))
    canvas.blit(instruct4, instruct4R)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > instruct4R.left and x < instruct4R.right:
                    if y > instruct4R.top and y < instruct4R.bottom:
                        pygame.mixer.music.stop()
                        start_game()

        pygame.display.update()

#ucs
def you_win4():
    canvas.blit(bgg, (0, 0))

    canvas.blit(win, (10, 10))
    instruct = medium_font.render("1) Nodes expanded:  264  ", True,BLACK)
    instruct2 = medium_font.render("2) cost:  28", True, BLACK)
    insruct3 = medium_font.render("3) Score: 400 ", True, BLACK)
    instruct4 = medium_font.render("back", True, PURPLE)
    instruct4R = instruct4.get_rect()
    instruct4R.center = (1000, 500 )
    canvas.blit(instruct, (520 , 150))
    canvas.blit(instruct2, (520,200 ))
    canvas.blit(insruct3, (520,250))
    canvas.blit(instruct4, instruct4R)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > instruct4R.left and x < instruct4R.right:
                    if y > instruct4R.top and y < instruct4R.bottom:
                        pygame.mixer.music.stop()
                        start_game()

        pygame.display.update()
#playthe game
def you_win5():
    canvas.blit(bgg, (0, 0))
    canvas.blit(win, (10, 10))

    insruct3 = large_fontttt.render("3) Score: 33 ", True, BLACK)
    instruct4 = large_fontttt.render("back", True, PURPLE)
    instruct4R = instruct4.get_rect()
    instruct4R.center = (1000, 500 )
    canvas.blit(insruct3, (520,250))
    canvas.blit(instruct4, instruct4R)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x > instruct4R.left and x < instruct4R.right:
                    if y > instruct4R.top and y < instruct4R.bottom:
                        pygame.mixer.music.stop()
                        start_game()

        pygame.display.update()


def game_paused():
    #canvas.fill(BLACK)


    paused_font1 = large_fonntt.render("Game Paused", True,GREEN,WHITE)
    paused_font_rect1 = paused_font1.get_rect()
    paused_font_rect1.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    canvas.blit(paused_font1, paused_font_rect1)
    pygame.mixer.music.pause()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause_xy = event.pos
                if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                    if pause_xy[1] > 0 and pause_xy[1] < 50:
                       pygame.mixer.music.unpause()
                       return

        pygame.display.update()

def gameloop():
    pygame.mixer.music.load('song.mp3')
    pygame.mixer.music.play(-1, 0.0)
    back2 = medium_font.render("back ", True, GREEN, WHITE)
    back2R = back2.get_rect()
    back2R.center = (36, 587)
    pygame.display.update()
    while True:

        #image first place
        emoji_x1 = 1200
        emoji_y1 = 350
        emoji_x2 = 600
        emoji_y2 = -45
        emoji_x3 = 400
        emoji_y3 = 655
        emoji_x4 = -50
        emoji_y4 = 500
        emoji_x5 = 2425
        emoji_y5 = 385
        emoji_x6 = 100
        emoji_y6 =  -670
        emoji_x7 = 300
        emoji_y7 = -955
        emoji_x8 = -750
        emoji_y8 = 545

        emoji_x9 = 1200
        emoji_y9 = 200

        emoji_x10 = 1045
        emoji_y10 = -45

        dir = 'left'
        dir2 = 'down'
        dir3 = 'up'
        dir4 = 'right'
        dir5 = 'left'
        dir6 = 'down'
        dir7 = 'up'
        dir8 = 'right'
        dir9 = 'left'
        dir10 = 'down'


        panda_x = 0
        panda_y = 40
        direction = 'none'
        score = medium_font.render("Score:0", True, WHITE)


        APPLE_X = 270
        APPLE_Y = 150
        APPLE_X2 = 270
        APPLE_Y2 = 200
        APPLE_X3 = 270
        APPLE_Y3 = 250
        APPLE_X4 = 270
        APPLE_Y4 = 300
        APPLE_X5 = 270
        APPLE_Y5 = 350
        APPLE_X6 = 270
        APPLE_Y6 = 400
        APPLE_X7 = 320
        APPLE_Y7 = 150
        APPLE_X8 = 320
        APPLE_Y8 = 250
        APPLE_X9 = 370
        APPLE_Y9 = 150
        APPLE_X10 = 370
        APPLE_Y10 = 250
        APPLE_X11 = 420
        APPLE_Y11 = 250
        APPLE_X12 = 470
        APPLE_Y12 = 250
        APPLE_X13 = 470
        APPLE_Y13 = 150
        APPLE_X14 = 470
        APPLE_Y14 = 200
        APPLE_X15 = 470
        APPLE_Y15 = 300
        APPLE_X16 = 470
        APPLE_Y16 = 350
        APPLE_X17 = 470
        APPLE_Y17 = 400
        APPLE_X18 = 530
        APPLE_Y18 = 150
        APPLE_X19 = 580
        APPLE_Y19 = 150
        APPLE_X20 = 630
        APPLE_Y20 = 150
        APPLE_X21 = 630
        APPLE_Y21 = 250
        APPLE_X22 = 630
        APPLE_Y22 = 300
        APPLE_X23 = 630
        APPLE_Y23 = 350
        APPLE_X24 = 680
        APPLE_Y24 = 150
        APPLE_X25 = 730
        APPLE_Y25 = 150
        APPLE_X26 = 630
        APPLE_Y26 = 200
        APPLE_X27 = 530
        APPLE_Y27 = 400
        APPLE_X28 = 580
        APPLE_Y28 = 400
        APPLE_X29 = 630
        APPLE_Y29 = 400
        APPLE_X30 = 680
        APPLE_Y30 = 400
        APPLE_X31 = 730
        APPLE_Y31 = 400
        APPLE_X32 =   420
        APPLE_Y32 =  150
        APPLE_X33 = 1050
        APPLE_Y33 = 550



        cost = 0
        pandalength = 0
        pandalist = []
        emojilist = []
        emojilist2 = []
        emojilist3 = []
        emojilist4 = []
        emojilist5 = []
        emojilist6 = []
        emojilist7 = []
        emojilist8 = []
        emojilist9 = []
        emojilist10 = []

        pause_font = medium_font.render('II', True, WHITE)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if x > back2R.left and x <back2R.right:
                        if y > back2R.top and y < back2R.bottom:
                              pygame.mixer.music.stop()
                              start_game()
                        pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if direction == 'right':
                            pass
                        else:
                            direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        if direction == 'left':
                            pass
                        else:
                            direction = 'right'
                    if event.key == pygame.K_UP:
                        if direction == 'down':
                            pass
                        else:
                            direction = 'up'
                    if event.key == pygame.K_DOWN:
                        if direction == 'up':
                            pass
                        else:
                            direction = 'down'






                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause_xy = event.pos
                    if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                        if pause_xy[1] > 0 and pause_xy[1] < 50:
                            game_paused()
            # we most set there our emojis
            if direction == 'up':
                panda_y -= VELOCITY
                if panda_y < TOP_WIDTH:
                    direction = 'down'
            if direction == 'down':
                panda_y += VELOCITY
                if panda_y > WINDOW_HEIGHT - panda_width:
                    direction = 'up'
            if direction == 'right':
                panda_x += VELOCITY
                if panda_x > WINDOW_WIDTH - panda_width:
                    direction = 'left'
            if direction == 'left':
                panda_x -= VELOCITY
                if panda_x < 0:
                    direction = 'right'

            if dir == 'left':
                emoji_x1 -= VELOCITY
                if emoji_x1 < -500:
                    dir = 'right'
            if dir == 'right':
                emoji_x1 += VELOCITY
                if emoji_x1 > 1100:
                    dir = 'left'
            if dir5 == 'left':
                emoji_x5 -= VELOCITY
                if emoji_x5 < -500:
                    dir5 = 'right'
            if dir5 == 'right':
                emoji_x5 += VELOCITY
                if emoji_x5 > 1125:
                    dir5 = 'left'
            if dir2 == 'down':
                emoji_y2 += VELOCITY
                if emoji_y2 > 800:
                    dir2 = 'up'
            if dir2== 'up':
                emoji_y2 -= VELOCITY
                if emoji_y2 < -300:
                    dir2 = 'down'
            if dir6 == 'down':
                emoji_y6 += VELOCITY
                if emoji_y6 > 800:
                    dir6 = 'up'
            if dir6 == 'up':
                emoji_y6 -= VELOCITY
                if emoji_y6 < -300:
                    dir6 = 'down'

            if dir3 == 'up':
                emoji_y3 -= VELOCITY
                if emoji_y3 < -900:
                    dir3 = 'down'
            if dir3 == 'down':
                emoji_y3 += VELOCITY
                if emoji_y3 > 900:
                    dir3 = 'up'

            if dir7 == 'up':
                emoji_y7 -= VELOCITY
                if emoji_y7 < 900:
                    dir7 = 'down'
            if dir7 == 'down':
                emoji_y7 += VELOCITY
                if emoji_y7 > -900:
                    dir7 = 'up'


            if dir4 == 'right':
                emoji_x4 += VELOCITY
                if emoji_x4 > 1400:
                    dir4 = 'left'
            if dir4 == 'left':
                emoji_x4 -= VELOCITY
                if emoji_x4 < -650:
                    dir4 = 'right'

            if dir8 == 'right':
                emoji_x8 += VELOCITY
                if emoji_x8 > 1400:
                    dir8 = 'left'
            if dir8 == 'left':
                emoji_x8 -= VELOCITY
                if emoji_x8 < -650:
                    dir8 = 'right'

            if dir9 == 'left':
                emoji_x9 -= VELOCITY
                if emoji_x9 < 0:
                    dir9 = 'right'
            if dir9 == 'right':
                emoji_x9 += VELOCITY
                if emoji_x9 > 1125:
                    dir9 = 'left'

            if dir10 == 'down':
                emoji_y10 += VELOCITY
                if emoji_y10 > 800:
                    dir10 = 'up'
            if dir10 == 'up':
                emoji_y10 -= VELOCITY
                if emoji_y10 < TOP_WIDTH:
                    dir10 = 'down'



            pandahead = []
            pandahead.append(panda_x)
            pandahead.append(panda_y)
            pandalist.append(pandahead)

            emojihead = []
            emojihead.append(emoji_x1)
            emojihead.append(emoji_y1)
            emojilist.append(emojihead)

            emojihead2 = []
            emojihead2.append(emoji_x2)
            emojihead2.append(emoji_y2)
            emojilist2.append(emojihead2)

            emojihead3 = []
            emojihead3.append(emoji_x3)
            emojihead3.append(emoji_y3)
            emojilist3.append(emojihead3)

            emojihead4 = []
            emojihead4.append(emoji_x4)
            emojihead4.append(emoji_y4)
            emojilist4.append(emojihead4)

            emojihead5 = []
            emojihead5.append(emoji_x5)
            emojihead5.append(emoji_y5)
            emojilist5.append(emojihead5)

            emojihead6 = []
            emojihead6.append(emoji_x6)
            emojihead6.append(emoji_y6)
            emojilist6.append(emojihead6)

            emojihead7 = []
            emojihead7.append(emoji_x7)
            emojihead7.append(emoji_y7)
            emojilist7.append(emojihead7)

            emojihead8 = []
            emojihead8.append(emoji_x8)
            emojihead8.append(emoji_y8)
            emojilist8.append(emojihead8)

            emojihead9 = []
            emojihead9.append(emoji_x9)
            emojihead9.append(emoji_y9)
            emojilist9.append(emojihead9)

            emojihead10 = []
            emojihead10.append(emoji_x10)
            emojihead10.append(emoji_y10)
            emojilist10.append(emojihead10)


            panda_head_rect = pygame.Rect(panda_x, panda_y, panda_width, panda_width)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)
            apple_rect2 = pygame.Rect(APPLE_X2, APPLE_Y2, APPLE_SIZE, APPLE_SIZE)
            apple_rect3 = pygame.Rect(APPLE_X3, APPLE_Y3, APPLE_SIZE, APPLE_SIZE)
            apple_rect4 = pygame.Rect(APPLE_X4, APPLE_Y4, APPLE_SIZE, APPLE_SIZE)
            apple_rect5 = pygame.Rect(APPLE_X5, APPLE_Y5, APPLE_SIZE, APPLE_SIZE)
            apple_rect6 = pygame.Rect(APPLE_X6, APPLE_Y6, APPLE_SIZE, APPLE_SIZE)
            apple_rect7 = pygame.Rect(APPLE_X7, APPLE_Y7, APPLE_SIZE, APPLE_SIZE)
            apple_rect8 = pygame.Rect(APPLE_X8, APPLE_Y8, APPLE_SIZE, APPLE_SIZE)
            apple_rect9 = pygame.Rect(APPLE_X9, APPLE_Y9, APPLE_SIZE, APPLE_SIZE)
            apple_rect10 = pygame.Rect(APPLE_X10, APPLE_Y10, APPLE_SIZE, APPLE_SIZE)
            apple_rect11 = pygame.Rect(APPLE_X11, APPLE_Y11, APPLE_SIZE, APPLE_SIZE)
            apple_rect12 = pygame.Rect(APPLE_X12, APPLE_Y12, APPLE_SIZE, APPLE_SIZE)
            apple_rect13 = pygame.Rect(APPLE_X13, APPLE_Y13, APPLE_SIZE, APPLE_SIZE)
            apple_rect14 = pygame.Rect(APPLE_X14, APPLE_Y14, APPLE_SIZE, APPLE_SIZE)
            apple_rect15 = pygame.Rect(APPLE_X15, APPLE_Y15, APPLE_SIZE, APPLE_SIZE)
            apple_rect16 = pygame.Rect(APPLE_X16, APPLE_Y16, APPLE_SIZE, APPLE_SIZE)
            apple_rect17 = pygame.Rect(APPLE_X17, APPLE_Y17, APPLE_SIZE, APPLE_SIZE)
            apple_rect18 = pygame.Rect(APPLE_X18, APPLE_Y18, APPLE_SIZE, APPLE_SIZE)
            apple_rect19 = pygame.Rect(APPLE_X19, APPLE_Y19, APPLE_SIZE, APPLE_SIZE)
            apple_rect20 = pygame.Rect(APPLE_X20, APPLE_Y20, APPLE_SIZE, APPLE_SIZE)
            apple_rect21 = pygame.Rect(APPLE_X21, APPLE_Y21, APPLE_SIZE, APPLE_SIZE)
            apple_rect22 = pygame.Rect(APPLE_X22, APPLE_Y22, APPLE_SIZE, APPLE_SIZE)
            apple_rect23 = pygame.Rect(APPLE_X23, APPLE_Y23, APPLE_SIZE, APPLE_SIZE)
            apple_rect24 = pygame.Rect(APPLE_X24, APPLE_Y24, APPLE_SIZE, APPLE_SIZE)
            apple_rect25 = pygame.Rect(APPLE_X25, APPLE_Y25, APPLE_SIZE, APPLE_SIZE)
            apple_rect26 = pygame.Rect(APPLE_X26, APPLE_Y26, APPLE_SIZE, APPLE_SIZE)
            apple_rect27 = pygame.Rect(APPLE_X27, APPLE_Y27, APPLE_SIZE, APPLE_SIZE)
            apple_rect28 = pygame.Rect(APPLE_X28, APPLE_Y28, APPLE_SIZE, APPLE_SIZE)
            apple_rect29 = pygame.Rect(APPLE_X29, APPLE_Y29, APPLE_SIZE, APPLE_SIZE)
            apple_rect30 = pygame.Rect(APPLE_X30, APPLE_Y30, APPLE_SIZE, APPLE_SIZE)
            apple_rect31 = pygame.Rect(APPLE_X31, APPLE_Y31, APPLE_SIZE, APPLE_SIZE)
            apple_rect32 = pygame.Rect(APPLE_X32, APPLE_Y32, APPLE_SIZE, APPLE_SIZE)
            apple_rect33 = pygame.Rect(APPLE_X33, APPLE_Y33, APPLE_SIZE, APPLE_SIZE)



            emojiR1 = pygame.Rect(emoji_x1, emoji_y1, emoji_size,emoji_size)
            emojiR2 = pygame.Rect(emoji_x2, emoji_y2, emoji_size, emoji_size)
            emojiR3 = pygame.Rect(emoji_x3, emoji_y3, emoji_size, emoji_size)
            emojiR4 = pygame.Rect(emoji_x4, emoji_y4, emoji_size, emoji_size)
            emojiR5 = pygame.Rect(emoji_x5, emoji_y5, emoji_size, emoji_size)
            emojiR6 = pygame.Rect(emoji_x6, emoji_y6, emoji_size, emoji_size)
            emojiR7 = pygame.Rect(emoji_x7, emoji_y7, emoji_size, emoji_size)
            emojiR8 = pygame.Rect(emoji_x8, emoji_y8, emoji_size, emoji_size)
            emojiR9 = pygame.Rect(emoji_x9, emoji_y9, emoji_size, emoji_size)
            emojiR10 = pygame.Rect(emoji_x10, emoji_y10, emoji_size, emoji_size)




            canvas.blit(bg,(0,0))
            emoji(emojilist, dir)
            emojii2(emojilist2, dir2)
            emojii3(emojilist3, dir3)
            emojii4(emojilist4, dir4)
            emojii5(emojilist5, dir5)
            emojii6(emojilist6, dir6)
            emojii7(emojilist7, dir7)
            emojii8(emojilist8, dir8)
            emojii9(emojilist9, dir9)
            emojii10(emojilist10, dir10)



            panda(pandalist, direction)

            if panda_head_rect.colliderect(apple_rect) :
                APPLE_X = -300
                APPLE_Y = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect2) :
                APPLE_X2 = -300
                APPLE_Y2 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect3) :
                APPLE_X3 = -300
                APPLE_Y3 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect4) :
                APPLE_X4 = -300
                APPLE_Y4 = -300
                pandalength = pandalength + 1
            if panda_head_rect.colliderect(apple_rect5):
                APPLE_X5 = -300
                APPLE_Y5 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect6) :
                APPLE_X6 = -300
                APPLE_Y6 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect7) :
                APPLE_X7 = -300
                APPLE_Y7 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect8) :
                APPLE_X8 = -300
                APPLE_Y8 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect9) :
                APPLE_X9 = -300
                APPLE_Y9 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect10) :
                APPLE_X10 = -300
                APPLE_Y10 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect11) :
                APPLE_X11 = -300
                APPLE_Y11 = -300
                pandalength = pandalength + 1
            if panda_head_rect.colliderect(apple_rect12):
                APPLE_X12 = -300
                APPLE_Y12 = -300
                pandalength = pandalength + 1
            if panda_head_rect.colliderect(apple_rect13):
                APPLE_X13 = -300
                APPLE_Y13 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect14) :
                APPLE_X14 = -300
                APPLE_Y14 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect15) :
                APPLE_X15 = -300
                APPLE_Y15 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect16) :
                APPLE_X16 = -300
                APPLE_Y16 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect17) :
                APPLE_X17 = -300
                APPLE_Y17 = -300
                pandalength = pandalength + 1
            if panda_head_rect.colliderect(apple_rect18):
                APPLE_X18 = -300
                APPLE_Y18 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect19) :
                APPLE_X19 = -300
                APPLE_Y19 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect20) :
                APPLE_X20 = -300
                APPLE_Y20 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect21) :
                APPLE_X21 = -300
                APPLE_Y21 = -300
                pandalength = pandalength + 1
            if panda_head_rect.colliderect(apple_rect22):
                APPLE_X22 = -300
                APPLE_Y22 = -300
                pandalength = pandalength + 1
            if panda_head_rect.colliderect(apple_rect23):
                APPLE_X23 = -300
                APPLE_Y23 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect24) :
                APPLE_X24 = -300
                APPLE_Y24 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect25) :
                APPLE_X25 = -300
                APPLE_Y25 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect26) :
                APPLE_X26 = -300
                APPLE_Y26 = -300
                pandalength = pandalength + 1
            if panda_head_rect.colliderect(apple_rect27):
                APPLE_X27 = -300
                APPLE_Y27 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect28) :
                APPLE_X28 = -300
                APPLE_Y28 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect29) :
                APPLE_X29 = -300
                APPLE_Y29 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect30) :
                APPLE_X30 = -300
                APPLE_Y30 = -300
                pandalength = pandalength + 1
            if  panda_head_rect.colliderect(apple_rect31) :
                APPLE_X31 = -300
                APPLE_Y31 = -300
                pandalength = pandalength + 1
            if panda_head_rect.colliderect(apple_rect33):
                    APPLE_X33 = -300
                    APPLE_Y33 = -300
                    pandalength = pandalength + 1

            if  panda_head_rect.colliderect(apple_rect32):
                APPLE_X32 = -300
                APPLE_Y32 = -300
                pandalength = pandalength + 1
            if pandalength == 33:
               you_win5()

            if panda_head_rect.colliderect(emojiR1):
                gameover()
            if panda_head_rect.colliderect(emojiR2):
                gameover()
            if panda_head_rect.colliderect(emojiR3):
                gameover()
            if panda_head_rect.colliderect(emojiR4):
                gameover()
            if panda_head_rect.colliderect(emojiR5):
                gameover()
            if panda_head_rect.colliderect(emojiR6):
                gameover()
            if panda_head_rect.colliderect(emojiR7):
                gameover()
            if panda_head_rect.colliderect(emojiR8):
                gameover()
            if panda_head_rect.colliderect(emojiR9):
                gameover()
            if panda_head_rect.colliderect(emojiR10):
                gameover()



            score = medium_font.render("Score: " + str(pandalength), True, WHITE)
            pandagame =  large_fontttt.render("PandaGame ", True, WHITE)
            pygame.draw.line(canvas, WHITE, (0, TOP_WIDTH), (WINDOW_WIDTH, TOP_WIDTH))
            pygame.draw.line(canvas, WHITE, (WINDOW_WIDTH - 60, 0), (WINDOW_WIDTH - 60, TOP_WIDTH))
            pygame.draw.rect(canvas, GREEN, (WINDOW_WIDTH - 60, 0, 60, TOP_WIDTH))
            pygame.draw.rect(canvas, GREEN, (0, 0, 129, TOP_WIDTH))
            canvas.blit(score, (0, 10))
            canvas.blit(pandagame, (410, -8))
            canvas.blit(pause_font, (WINDOW_WIDTH - 45, 10))


            canvas.blit(apple, (APPLE_X, APPLE_Y))
            canvas.blit(apple, (APPLE_X2, APPLE_Y2))
            canvas.blit(apple, (APPLE_X3, APPLE_Y3))
            canvas.blit(apple, (APPLE_X4, APPLE_Y4))
            canvas.blit(apple, (APPLE_X5, APPLE_Y5))
            canvas.blit(apple, (APPLE_X6, APPLE_Y6))
            canvas.blit(apple, (APPLE_X7, APPLE_Y7))
            canvas.blit(apple, (APPLE_X8, APPLE_Y8))
            canvas.blit(apple, (APPLE_X9, APPLE_Y9))
            canvas.blit(apple, (APPLE_X10, APPLE_Y10))
            canvas.blit(apple, (APPLE_X11, APPLE_Y11))
            canvas.blit(apple, (APPLE_X12, APPLE_Y12))
            canvas.blit(apple, (APPLE_X13, APPLE_Y13))
            canvas.blit(apple, (APPLE_X14, APPLE_Y14))
            canvas.blit(apple, (APPLE_X15, APPLE_Y15))
            canvas.blit(apple, (APPLE_X16, APPLE_Y16))
            canvas.blit(apple, (APPLE_X17, APPLE_Y17))
            canvas.blit(apple, (APPLE_X18, APPLE_Y18))
            canvas.blit(apple, (APPLE_X19, APPLE_Y19))
            canvas.blit(apple, (APPLE_X20, APPLE_Y20))
            canvas.blit(apple, (APPLE_X21, APPLE_Y21))
            canvas.blit(apple, (APPLE_X22, APPLE_Y22))
            canvas.blit(apple, (APPLE_X23, APPLE_Y23))
            canvas.blit(apple, (APPLE_X24, APPLE_Y24))
            canvas.blit(apple, (APPLE_X25, APPLE_Y25))
            canvas.blit(apple, (APPLE_X26, APPLE_Y26))
            canvas.blit(apple, (APPLE_X27, APPLE_Y27))
            canvas.blit(apple, (APPLE_X28, APPLE_Y28))
            canvas.blit(apple, (APPLE_X29, APPLE_Y29))
            canvas.blit(apple, (APPLE_X30, APPLE_Y30))
            canvas.blit(apple2, (APPLE_X33, APPLE_Y33))
            canvas.blit(apple, (APPLE_X32, APPLE_Y32))
            canvas.blit(apple, (APPLE_X31, APPLE_Y31))



            canvas.blit(back2, back2R)



            pygame.display.update()




            clock.tick(FPS)
            print("successor: " ,direction)
            print(clock)
            pygame.display.update()



start_game()
gameloop()
