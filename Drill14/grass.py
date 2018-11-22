from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        # fill here

        self.bgm = load_music('football.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)


    def get_bb(self):
        return 0, 0, 1600-1, 50
