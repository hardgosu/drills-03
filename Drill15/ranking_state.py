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
font = None
rankingList = []

def enter():
    global menu,font
    menu = load_image('ranking.png')
    font = load_font('ENCR10B.TTF', 20) # None
    hide_cursor()
    hide_lattice()

def exit():
    global menu
    del menu

def pause():
    pass

def resume():
    pass


def DispalyRecords():
    global rankingList


    with open('ranking.json','r') as f:
        rankingList = json.load(f)



    for i in range(0,10):
        font.draw(get_canvas_width() // 2 - 200, get_canvas_height() // 2 + 250 -60 * i , '%s'% '#' + json.dumps(i + 1) + '. ' , (255, 255, 0))
        font.draw(get_canvas_width() // 2 - 100, get_canvas_height() // 2 + 250 -60 * i , '%3.2f'%  rankingList[i]['#' + json.dumps(i + 1) + '. '] , (255, 255, 30))
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
    test = 'ad'
    clear_canvas()
    menu.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    DispalyRecords()

    update_canvas()






