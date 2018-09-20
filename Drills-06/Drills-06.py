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


# 잘라낸 캐릭터 크기 33 X 77
# 전체 캐릭텅 미지 크기 42X92
while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * row, 100, 100, x-(33//2), y + (77/2 - 10))
    cursor.draw(cursorX,cursorY)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)
    handle_events()
    print(distanceY)
    if characterMoveFlag == True:
        if destinationX < x:
            x -= 5
            accumulatedX += 5
            row = 0
        elif destinationX >= x:
            x += 5
            accumulatedX += 5
            row = 1
        if destinationY >= y:
            y += 5
            accumulatedY += 5

        elif destinationY < y:
            y -= 5
            accumulatedY += 5
        if accumulatedX >= distanceX and accumulatedY >= distanceY:
            characterMoveFlag = False



close_canvas()

