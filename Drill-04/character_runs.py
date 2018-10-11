from pico2d import *
open_canvas()

path = os.getcwd()

os.chdir(path)


grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 0


frame = 0

while ( x <  800):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 100,0,100,100,x,90)
    update_canvas()
    frame = (frame + 1 )%8
    x = x + 5
    delay(0.05)
    get_events()

# 여기를 채우세요.


close_canvas()

