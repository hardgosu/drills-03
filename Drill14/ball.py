import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None

    bg = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')



    def get_bb(self):
        return self.x - self.bg.window_left - 20, self.y - self.bg.window_bottom - 20, self.x - self.bg.window_left + 20, self.y - self.bg.window_bottom + 20

    def draw(self):
        self.image.draw(self.x - self.bg.window_left, self.y - self.bg.window_bottom)
        draw_rectangle(*self.get_bb())

    def update(self):
        pass
        #self.y -= self.fall_speed * game_framework.frame_time

    def set_background(self, bg):
        Ball.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2
        self.x, self.y = random.randint(0, self.bg.w - 1), random.randint(0,self.bg.h - 1)

