import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import advanced_pause_state

name = "MainState"

boy = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global  boy, grass
    boy = Boy()
    grass = Grass()



def exit():
    global  boy, grass
    del(boy)
    del(grass)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
            #game_framework.push_state(luxury_pause_state)
            game_framework.push_state(advanced_pause_state)
def update():
    boy.update()



def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()






