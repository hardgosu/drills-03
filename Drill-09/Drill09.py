from pico2d import *
import random
class SoccerBall:
    def __init__(self):
        self.x,self.y = random.randint(100,700),600
        self.speedY = random.randint(5,15)
        self.size = random.randint(0,1)
        self.directionY = -1
        self.positionLimitX = 0
        self.positionLimitY = 0
        if self.size == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')


#포지션 제한? 사각 영역,원 영역... 그러나 지금은 y = n 같은 직선.
    def update(self,limitX,limitY):
        self.positionLimitY = limitY
       #self.positionLimitX = limitX
        for i in range(self.speedY):
            self.y += 1 * self.directionY

        for i in range(self.speedY):
            if self.y < self.positionLimitY and self.positionLimitY != 0:
                self.y -= 1 * self.directionY


    def draw(self):
        self.image.draw(self.x,self.y)


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

soccerBalls = [SoccerBall() for i in range(20)]



grass = Grass()
running = True;

for boy in team:
    boy.frame = random.randint(0,7)
    boy.x = random.randint(100, 700)

# game main loop code

while running:
    handle_events()
    clear_canvas()
    for soccerBall in soccerBalls:
        if soccerBall.size == 0 :
            soccerBall.update(0,60)
        else:
            soccerBall.update(0,70)
        soccerBall.draw()
    #print(soccerBall.x)
    for boy in team:
        boy.update()
        boy.draw()
    grass.draw()
    update_canvas()
    delay(0.05)




# finalization code
close_canvas()

#end
