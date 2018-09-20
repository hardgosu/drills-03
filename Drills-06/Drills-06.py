from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global cursorX, cursorY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            cursorX, cursorY = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            SetDestination(event.x,KPU_HEIGHT  - 1 - event.y)
            #print(event.y)
open_canvas(KPU_WIDTH, KPU_HEIGHT)


def SetDestination(newX,newY):
    global  destinationX
    global  destinationY
    global characterMoveFlag
    global  distanceX
    global  distanceY
    global  x
    global  y
    global accumulatedX
    global accumulatedY

    accumulatedX = 0
    accumulatedY = 0
    distanceX = abs(newX - x)
    distanceY = abs(newY - y)

    characterMoveFlag = True
    destinationX = newX
    destinationY = newY





# fill here
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')



running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

destinationX = 0
destinationY = 0
characterMoveFlag = False


frame = 0
dir = 0
hide_cursor()
cursorX,cursorY = KPU_WIDTH // 2, KPU_HEIGHT // 2

row = 1

distanceX = 0
distanceY = 0
accumulatedX = 0
accumulatedY = 0





close_canvas()

