import random
import os
from pico2d import *

from PathData import InitializeData

class Boy:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 8

#추후에 클래스,구조체 등으로 모듈화

    rightIdle = None
    rightIdleIntervalX = 36
    rightIdleIntervalY = 46
    rightIdleFrames = 73


    leftIdle = None
    leftIdleIntervalX = 36
    leftIdleIntervalY = 46
    leftIdleFrames = 73


    startWalkingRight = None
    startWalkingRightIntervalX = 50
    startWalkingRightIntervalY = 47
    startWalkingRightFrames = 3


    startWalkingLeft = None
    startWalkingLeftIntervalX = 50
    startWalkingLeftIntervalY = 47
    startWalkingLeftFrames = 3


    walkingRight = None
    walkingRightIntervalX = 71
    walkingRightIntervalY = 47
    walkingRightFrames = 14


    walkingLeft = None
    walkingLeftIntervalX = 71
    walkingLeftIntervalY = 47
    walkingLeftFrames = 14










    START_RIGHT_RUN, START_LEFT_RUN , LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, RIGHT_DASH, LEFT_DASH, RIGHT_FALLING, LEFT_FALLING = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9



    def __init__(self):

        self.fuck = 0

        self.x, self.y = 0, 90
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0
        self.state = self.RIGHT_STAND
        if Boy.rightIdle == None:

            Boy.rightIdle = load_image('X_Idle2.png')
        if Boy.leftIdle == None:

            Boy.leftIdle = load_image('X_idle2_left.png')

        if Boy.startWalkingRight == None:

            Boy.startWalkingRight = load_image('X_Start_Right_Walking.png')
        if Boy.startWalkingLeft == None:

            Boy.startWalkingLeft = load_image('X_Start_Left_Walking.png')

        if Boy.walkingRight == None:

            Boy.walkingRight = load_image('X_Right_Walking.png')

        if Boy.walkingLeft == None:

            Boy.walkingLeft = load_image('X_Left_Walking.png')




    def update(self, frame_time):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        self.life_time += frame_time
        distance = Boy.RUN_SPEED_PPS * frame_time
        self.total_frames += Boy.FRAMES_PER_ACTION * Boy.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 8
        self.x += (self.dir * distance)

        self.x = clamp(0, self.x, 800)


    def draw(self):

        #똥손으로 인한 미세조정 필요
        if self.state == self.RIGHT_RUN:
            self.walkingRight.clip_draw(Boy.walkingRightIntervalX * self.fuck ,0,Boy.walkingRightIntervalX  ,Boy.walkingRightIntervalY,self.x,self.y)
            self.fuck = (self.fuck + 1) % (Boy.walkingRightFrames )
        elif self.state == self.LEFT_RUN:
            self.walkingLeft.clip_draw(Boy.walkingLeftIntervalX * self.fuck  ,0,Boy.walkingLeftIntervalX   ,Boy.walkingLeftIntervalY,self.x,self.y)
            self.fuck = (self.fuck + 1) % (Boy.walkingLeftFrames )
        elif self.state == self.RIGHT_STAND:
            self.rightIdle.clip_draw(Boy.rightIdleIntervalX * self.fuck  ,0,Boy.rightIdleIntervalX   ,Boy.rightIdleIntervalY,self.x,self.y)
            self.fuck = (self.fuck + 1) % (Boy.rightIdleFrames )
        elif self.state == self.LEFT_STAND:
            self.leftIdle.clip_draw(Boy.leftIdleIntervalX * self.fuck  ,0,Boy.leftIdleIntervalX   ,Boy.leftIdleIntervalY,self.x,self.y)
            self.fuck = (self.fuck + 1) % (Boy.leftIdleFrames )


        delay(0.03)
        #self.image.clip_draw(36 * self.fuck,0,36,46,self.x,self.y)
        #self.fuck = (self.fuck + 1) % 72

        pass



    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 18, self.y - 23, self.x + 18, self.y + 23

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN):
                self.state = self.LEFT_RUN
                self.dir = -1
                self.fuck = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN):
                self.state = self.RIGHT_RUN
                self.dir = 1
                self.fuck = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
                self.dir = 0
                self.fuck = 0
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
                self.dir = 0
                self.fuck = 0




