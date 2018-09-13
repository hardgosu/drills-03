from pico2d import *
open_canvas()

path = os.getcwd()

os.chdir(path)



frame = 0
grass = load_image('grass.png')
animation = load_image('character.png')
x = 0

frontDirection = True
backDirection = False

animation = load_image('animation_sheet.png')
row = 2




row = 1

while (x < 800):
    clear_canvas()
    grass.draw(400, 30)
    animation.clip_draw(frame * 100, 100 * row, 100, 100, x, 90)
    frame = (frame + 1) % 8
    x = x + 15

    update_canvas()
    delay(0.05)
    get_events()

row = 0
while (x > 0 ):
    clear_canvas()
    grass.draw(400, 30)
    animation.clip_draw(frame * 100, 100 * row, 100, 100, x, 90)
    frame = (frame + 1) % 8
    x = x - 15

    update_canvas()
    delay(0.05)
    get_events()


close_canvas()