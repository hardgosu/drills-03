from pico2d import *
import math




open_canvas()


path = os.getcwd()

os.chdir(path)


grass = load_image('grass.png')
character = load_image('character.png')

#stack = 0

#test = x+(y * y)

#print(math.sqrt(test))
#print(abs(3))
    


while(True):

    x = 0
    y = 90



    while ( x < 400):
        clear_canvas_now()
        grass.draw_now(400, 30)

        character.draw_now(x, y)
        x = x + 2
        delay(0.01)


    degree = 360
    i = 0

    while( i <= degree):
        clear_canvas_now()
        grass.draw_now(400,30)

        character.draw_now(x,y)
        x = 400 -200 * math.sin(math.radians(i))
        y = 285  -200* math.cos(math.radians(i))
        i = i + 1
        delay(0.01)
        

    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400, 30)

        character.draw_now(x, y)
        x = x + 2
        delay(0.01)



    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)


    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)

        character.draw_now(x, y)
        x = x - 2
        delay(0.01)

    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01)


close_canvas()
