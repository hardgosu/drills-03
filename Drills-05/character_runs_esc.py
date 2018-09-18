from pico2d import *


def handle_events():
    global running
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                 dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1


def GotoSomeCoordinate(x,y,curX,curY):
    global dirX
    global dirY
    if curX < x:
        dirX += 1
    elif curX > x:
        dirX -= 1
    if curY < y:
        dirY += 1
    elif curY >y:
        dirY -= 1


def GotoSomeCoordinateUntilEnd(newX,newY):

        global dirX
        global dirY
        global frame
        global row
        global grass
        global character
        global running
        global x
        global y


        while running:
            dirX,dirY = 0,0

            clear_canvas()
            grass.draw(400, 30)
            GotoSomeCoordinate(newX, newY, x, y)
            # handle_events()
            frame = (frame + 1) % 8
            x += dirX
            y += dirY
            if dirX >= 0:
                row = 1
            elif dirX < 0:
                row = 0

            character.clip_draw(frame * 100, 100 * row, 100, 100, x, y)
            delay(0.005)
            update_canvas()
            if dirX == 0 and dirY == 0:
                break


open_canvas()
grass = load_image('KPU_GROUND_FULL.png')
character = load_image('animation_sheet.png')

dirX = 0
dirY = 0
running = True
x = 800 // 2
frame = 0
dir = 0
y = 90
row = 0
while True:
    GotoSomeCoordinateUntilEnd(203, 535)
    GotoSomeCoordinateUntilEnd(132, 243)
    GotoSomeCoordinateUntilEnd(535, 470)
    GotoSomeCoordinateUntilEnd(477, 203)
    GotoSomeCoordinateUntilEnd(715, 136)
    GotoSomeCoordinateUntilEnd(316, 225)
    GotoSomeCoordinateUntilEnd(510, 92)
    GotoSomeCoordinateUntilEnd(692, 518)
    GotoSomeCoordinateUntilEnd(682, 336)
    GotoSomeCoordinateUntilEnd(712, 349)

    GotoSomeCoordinateUntilEnd(800//2, 90)




close_canvas()
