import game_framework
from pico2d import *
import main_state

name = "AdvancedPauseState"
image = None
emptyImage = None
twinkle_time = 0.0
#아니 rgba 조절 어떻게해 ㅠㅠ
none = False
pauseImage = None

temp = 1
def enter():
    global image
    global emptyImage
    global pauseImage
    pauseImage = load_image('pause2.png')
    emptyImage = load_image('pause3.png')
    image = pauseImage

def exit():
    global  image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type,event.key) ==(SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()

def draw():
    global none
    #clear_canvas()
    global image
    global emptyImage
    global pauseImage
    if(none):
        image = pauseImage
        image.draw(400,300,100 ,100)
    else:
        image = emptyImage
        image.draw(400,300,100,100)

    update_canvas()








def update():
    global twinkle_time
    global none
    if (twinkle_time > 0.5):
        twinkle_time = 0
        none = not none
    delay(0.01)
    twinkle_time += 0.01
    print(none)

def pause():
    pass


def resume():
    pass


