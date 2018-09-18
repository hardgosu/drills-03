from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

#오늘은 진도 안나가고 이대현교수님의 특강 18 09 18

def move_from_center_to_right():
    global x,y

    while x < 800 - 25:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 2
        delay(0.01)


def move_up():
    global x,y

    while y < 600 - 50:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y += 2
        delay(0.01)


def move_left():
    global x,y


    while x > 0 + 25:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x -= 2
        delay(0.01)


def move_down():
    global x,y

    while y > 0 + 40:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y -= 2
        delay(0.01)

    pass
def move_left_to_center():
    global x,y

    while x < 400 + 25:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x += 2
        delay(0.01)
    pass


def make_rectangle():
    move_from_center_to_right()
    move_up()
    move_left()
    move_down()
    move_left_to_center()


    pass




def make_circle():
    pass


x,y = 800 // 2,90

while True:
    make_rectangle()
    #make_circle()
    #throw_rectangle()
    #throw_circle()


close_canvas()
