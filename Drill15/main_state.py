import random
import json
import pickle
import os
import json


from pico2d import *
import game_framework
import game_world

import world_build_state
import ranking_state

name = "MainState"






def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

boy = None
zombies = None
rankingList = []
def enter():
    # game world is prepared already in world_build_state
    global boy,zombies
    boy = world_build_state.get_boy()
    zombies = world_build_state.get_zombies()
    #RecordsInitialize()
    pass
def SaveBoysRecords():
    global boy,rankingList

    with open('ranking.json','r') as f:
        rankingList = json.load(f)

    for i in range(0,10):
        if rankingList[i]['#' + json.dumps(i + 1) + '. '] < boy.timeRecord:

            for j in range(1,10-i):

                rankingList[10   - j]['#' + json.dumps(10 - j + 1) + '. '] = rankingList[10 - j - 1]['#' + json.dumps(10 - j) + '. ']

            rankingList[i]['#' + json.dumps(i + 1) + '. '] = boy.timeRecord

            break


    with open('ranking.json','w') as f:
        json.dump(rankingList,f)

"""""
    for i in range(0,10):
        if rankingList[i]['#' + json.dumps(i + 1) + '. '] < boy.timeRecord:

            for j in range(i + 1,10):

                rankingList[10 - j]['#' + json.dumps(10 - j + 1) + '. '] = rankingList[10 - j - 1]['#' + json.dumps(10 - j) + '. ']
                print("와!신기록!")
            rankingList[i]['#' + json.dumps(i + 1) + '. '] = boy.timeRecord

            break
"""""




def RecordsInitialize():
    dic = []
    with open('ranking.json','w') as f:
        for i in range(0,10):
            s  = '#' + json.dumps(i + 1) + '. '
            t = 0
            dic.append({s:t})
        json.dump(dic,f)




def exit():
    print("꾸에엑")
    SaveBoysRecords()
    game_world.clear()

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
            game_framework.change_state(world_build_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_s:
            game_world.save()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    for zombie in zombies:
        if collide(boy,zombie):
            game_framework.change_state(ranking_state)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






