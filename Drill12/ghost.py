import game_framework
from pico2d import *
from ball import Ball

import game_world
import random

import math

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed
# fill expressions correctly

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8






Degree = 0

W = 4 * math.pi



class Ghost:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        # fill here
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0


        self.timer = 0
        self.opacify = 0.5

        self.activate = False

        self.startPointX = 800
        self.startPointY = 400


        self.riseKeyFrame = 120
        self.currentFrame = 0
        self.riseAnimation = False

    def start(self,boy):
        self.startPointX = boy.x
        self.startPointY = boy.y
        self.currentFrame = 0
        self.riseAnimation = True


        pass

    def update(self):
        global Degree
        if(self.riseAnimation == True):
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
            self.image.opacify(self.opacify)
            self.currentFrame += 1
        else:


            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
            self.image.opacify(self.opacify)

            Degree = (Degree + math.degrees(W* game_framework.frame_time) ) % 720

            self.opacify = (random.randint(0,10) % 11) / 10.0

            self.velocity = 3 * PIXEL_PER_METER
            self.x = self.startPointX + self.velocity * math.cos(math.radians(Degree))
            self.y = self.startPointY + self.velocity * math.sin(math.radians(Degree))



        pass

    def draw(self):

        if self.riseAnimation == True:
            if(self.currentFrame < 40):
                self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, 3.141592 / 2, '', self.startPointX - 25, self.startPointY, 100, 100)
            elif(self.currentFrame < 80):
                self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, 3.141592 / 4, '',self.startPointX - 25, self.startPointY, 100, 100)
            elif(self.currentFrame < 120):
                self.image.clip_composite_draw(int(self.frame) * 100, 300, 100, 100, 0, '',self.startPointX - 25, self.startPointY, 100, 100)
            elif(self.currentFrame >= 120):
                self.riseAnimation = False

        else:


            if self.dir == 1:
                self.image.clip_draw(int(self.frame) * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(int(self.frame) * 100, 200, 100, 100, self.x, self.y)
