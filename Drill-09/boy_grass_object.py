from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x,self.y = 0,90
        self.frame = 0
        self.image = load_image('run_animation.png')


    def update(self):
        self.frame = (self.frame + 1) %  8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

open_canvas()
team = [Boy() for i in range(11)]



grass = Grass()
running = True;

for boy in team:
    boy.frame = random.randint(0,7)
    boy.x = random.randint(100, 700)

# game main loop code

while running:
    handle_events()
    for boy in team:
        boy.update()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()
    delay(0.05)




# finalization code
close_canvas()
