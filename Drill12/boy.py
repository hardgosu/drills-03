import game_framework
from pico2d import *
from ball import Ball

import game_world
import random
# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


# Boy Action Speed
# fill expressions correctly

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8



# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


# Boy States

class IdleState:

    timer = 0
    frameTime = 0



    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        IdleState.timer = get_time()





    @staticmethod
    def exit(boy, event):

        if event == SPACE:
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        IdleState.frameTime = get_time() - IdleState.timer

        IdleState.timer += IdleState.frameTime





    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(int(boy.frame) * 100, 200, 100, 100, boy.x, boy.y)


class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            boy.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            boy.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            boy.velocity += RUN_SPEED_PPS
        boy.dir = clamp(-1, boy.velocity, 1)

        pass

    @staticmethod
    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()

    @staticmethod
    def do(boy):
        #boy.frame = (boy.frame + 1) % 8
        # fill here
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        boy.x += boy.velocity * game_framework.frame_time
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(int(boy.frame) * 100, 100, 100, 100, boy.x, boy.y)


        else:
            boy.image.clip_draw(int(boy.frame) * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:


    step = 0
    degree = 30
    ghostVelocityX = 0
    ghostVelocityY = 0
    pixel_per_threeMeter = 333
    degree = -90

    currentTime = 0
    frameTime = 0
    timer = 0


    ghostVX = 0
    ghostVY = 0
    ghostPosX = 0
    ghostPosY = 0
    newDegree = 12

    @staticmethod
    def enter(boy, event):
        boy.frame = 0
        SleepState.currentTime = get_time()
        SleepState.frameTime = 0
        SleepState.timer = 0

        SleepState.ghostPosX = boy.x
        SleepState.ghostPosY = boy.y + SleepState.pixel_per_threeMeter

        radian = math.radians(SleepState.newDegree)

    @staticmethod
    def exit(boy, event):
        pass

#지름 곱하기 3.14....는 2091
#2091 * 2를 1초만에 움직여야..
#37.68m/s


    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8


        SleepState.frameTime = get_time() - SleepState.currentTime
        SleepState.currentTime += SleepState.frameTime
        SleepState.timer += SleepState.frameTime

        radian = math.radians(SleepState.degree)
        SleepState.ghostVelocityX = ( boy.x + SleepState.pixel_per_threeMeter * math.cos(radian))
        SleepState.ghostVelocityY = (boy.y + SleepState.pixel_per_threeMeter + SleepState.pixel_per_threeMeter * math.sin(radian))
        SleepState.degree += 720 / 60


        SleepState.ghostVX = (SleepState.pixel_per_threeMeter * math.cos(radian))
        SleepState.ghostVY = (SleepState.pixel_per_threeMeter * math.sin(radian))

        SleepState.ghostPosX += SleepState.ghostVX * 0.1
        SleepState.ghostPosY += SleepState.ghostVY * 0.1



    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.opacify(1)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
            boy.image.opacify(random.randint(0,10) / 10.0)

            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, SleepState.ghostVelocityX, SleepState.ghostVelocityY)

            boy.font.draw(boy.x - 60, boy.y + 100, '(Time: %3.2f)' % SleepState.timer, (122, 255, 0))
        else:
            boy.image.opacify(1)
            boy.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)
            boy.image.opacify(random.randint(0,10) / 10.0)

            boy.image.clip_draw(int(boy.frame) * 100, 300, 100, 100, SleepState.ghostPosX, SleepState.ghostPosY)





next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    SleepState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        # Boy is only once created, so instance image loading is fine
        self.image = load_image('animation_sheet.png')
        # fill here
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

        self.timer = 0

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir*3)
        game_world.add_object(ball, 1)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        # fill here

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

