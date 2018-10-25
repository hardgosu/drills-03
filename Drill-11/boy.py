from pico2d import *
from ball import Ball

import game_world

# Boy Event

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,SLEEP_TIMER,SPACE,LSHIFT,RSHIFT,LSHIFTUP,RSHIFTUP = range(10)


# fill here

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN,SDLK_SPACE) : SPACE,
    (SDL_KEYDOWN, SDLK_LSHIFT): LSHIFT,
    (SDL_KEYDOWN, SDLK_RSHIFT): RSHIFT,
    (SDL_KEYUP, SDLK_LSHIFT): LSHIFTUP,
    (SDL_KEYUP, SDLK_RSHIFT): RSHIFTUP

}

# Boy States

class IdleState:

    @staticmethod
    def enter(boy,event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.frame = 0
        boy.timer = 1000


    @staticmethod
    def exit(boy,event):
        if(event == SPACE):
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -=1
        if boy.timer == 0:
            boy.add_event(SLEEP_TIMER)

    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_draw(boy.frame * 100, 300, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)

class RunState:

    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity

    @staticmethod
    def exit(boy, event):

        if(event == SPACE):
            boy.fire_ball()
        pass

    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


class SleepState:
    @staticmethod
    def enter(boy,event):
        boy.frame = 0
    @staticmethod
    def exit(boy,event):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + 1) % 8
    @staticmethod
    def draw(boy):
        if boy.dir == 1:
            boy.image.clip_composite_draw(boy.frame * 100, 300, 100, 100,3.141592 / 2, '', boy.x - 25, boy.y - 25, 100, 100)
        else:
            boy.image.clip_composite_draw(boy.frame * 100, 200, 100, 100,-3.141592 / 2, '', boy.x + 25, boy.y - 25, 100, 100)



class DashState:

    test = 0
    @staticmethod
    def enter(boy, event):
        if event == RIGHT_DOWN:
            boy.velocity += 1
        elif event == LEFT_DOWN:
            boy.velocity -= 1
        elif event == RIGHT_UP:
            boy.velocity -= 1
        elif event == LEFT_UP:
            boy.velocity += 1
        boy.dir = boy.velocity
        DashState.test = 0
    @staticmethod
    def exit(boy, event):
        #boy.x -= boy.velocity * 10
        boy.cur_state = RunState
        boy.cur_state.enter(boy,None)

        pass

    @staticmethod
    def do(boy):
        DashState.test +=1
        print(DashState.test)
        if(DashState.test > 60):
            DashState.exit(boy,None)
            DashState.test = 0

        boy.frame = (boy.frame + 1) % 8
        boy.timer -= 1
        boy.x += boy.velocity * 10
        boy.x = clamp(25, boy.x, 1600 - 25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.image.clip_draw(boy.frame * 100, 100, 100, 100, boy.x, boy.y)
        else:
            boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)



next_state_table = {
# fill here
    IdleState: { RIGHT_UP : RunState, LEFT_UP : RunState, RIGHT_DOWN : RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState,
                 SPACE: IdleState},
    RunState: { RIGHT_UP : IdleState,LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN : IdleState,
                SPACE: RunState},

    SleepState:  { LEFT_DOWN: RunState, RIGHT_DOWN :RunState, LEFT_UP: RunState, RIGHT_UP: RunState,SPACE: IdleState},
    DashState: { LEFT_DOWN: IdleState, RIGHT_DOWN :IdleState, LEFT_UP: IdleState, RIGHT_UP: IdleState,LSHIFT : IdleState, RSHIFT : IdleState}

}

class Boy:

    def __init__(self):
        self.x, self.y = 1600 // 2, 90
        self.image = load_image('animation_sheet.png')
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)


    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir * 3)
        game_world.add_object(ball, 1)
        pass



    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        print(self.cur_state)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

