from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280, 1024


class Boy():
    pass


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
            SetDestination(event.x, KPU_HEIGHT - 1 - event.y)
            # print(event.y)


open_canvas(KPU_WIDTH, KPU_HEIGHT)


def SetDestination(character, p1, p2):
    global x
    global y
    global frame
    global row
    global cursorY
    global cursorX

    for i in range(0, 100 + 1, 2):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        DrawCharacter(character)
        delay(0.02)


def MoveCurve(character, p1, p2, p3, parameterLimitStart, parameterLimitEnd):
    global x
    global y
    global frame
    global row
    global cursorY
    global cursorX

    for i in range(parameterLimitStart, parameterLimitEnd + 1, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * p1[0] + (-4 * t ** 2 + 4 * t) * p2[0] + (2 * t ** 2 - t) * p3[0]
        y = (2 * t ** 2 - 3 * t + 1) * p1[1] + (-4 * t ** 2 + 4 * t) * p2[1] + (2 * t ** 2 - t) * p3[1]
        DrawCharacter(character)
        delay(0.02)
    pass


def DrawBackground(background):
    pass


def RenderingPipeline():
    pass


# 하나의 인스턴스를 참조해야한다.
def DrawCharacter(character):
    global x
    global y
    global frame
    global row
    global points
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * row, 100, 100, x - (33 // 2), y + (77 / 2 - 10))
    cursor.draw(200, 200)
    cursor.draw(cursorX, cursorY)
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)

    pass


kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
cursor = load_image('hand_arrow.png')
noName = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2

destinationX = 0
destinationY = 0
characterMoveFlag = False

frame = 0
dir = 0
hide_cursor()
cursorX, cursorY = KPU_WIDTH // 2, KPU_HEIGHT // 2

row = 1

distanceX = 0
distanceY = 0
accumulatedX = 0
accumulatedY = 0

size = 10

points = [(random.randint(0, 800), random.randint(0, 600)) for i in range(size)]
# draw_line_basic(points[0],points[1])
# 잘라낸 캐릭터 크기 33 X 77
# 전체 캐릭텅 미지 크기 42X92
n = 0
stamp = 0

temp = [(200, 200), (500, 300)]
while running:

   for i in range(0, size):

     MoveCurve(character,points[i % size],points[(i + 1) % size],points[(i + 2) % size],0,50)


close_canvas()

