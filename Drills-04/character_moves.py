from pico2d import *

open_canvas()

path = os.getcwd()

os.chdir(path)


grass = load_image('grass.png')
character = load_image('character.png')

# 여기를 채우세요.
x = 0
while (x < 800):
    clear_canvas()
    grass.draw(400,30)
    character.draw(x,90)
    x = x + 2
    update_canvas()
    delay(0.01)
    get_events()


close_canvas()

