import random
import json
import pickle
import os

from pico2d import *
import game_framework
import game_world

import main_state


import world_build_state


name = "RankingState"

menu = None

def enter():
    global menu
    menu = load_image('ranking.png')
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    del menu

def pause():
    pass

def resume():
    pass




def load_saved_world():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)


def update():
    pass

def draw():
    clear_canvas()
    menu.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()






