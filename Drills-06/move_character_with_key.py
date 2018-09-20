from pico2d import *


def handle_events():
    global running
    global x
    global dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                print(1)
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


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame = 0
dir = 0

row = 1

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100 * row, 100, 100, x, 90)
    update_canvas()

    handle_events()
    if dir >0 :
        row = 1
    elif dir < 0:
        row = 0

    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.05)

close_canvas()

