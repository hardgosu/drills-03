import sys
import os
import types
import ctypes
import math
import json

#try:
from .sdl2 import *
from .sdl2.sdlimage import *
from .sdl2.sdlttf import *
from .sdl2.sdlmixer import *
#except ImportError:
#    print("Error: cannot import pysdl2 - probably not installed")
#    sys.exit(-1) # abort program execution




lattice_on = True
audio_on = False


def clamp(minimum, x, maximum):
    return max(minimum, min(x, maximum))

def delay(sec):
    SDL_Delay(int(sec*1000))

def get_time():
    return SDL_GetTicks() / 1000.0


def get_canvas_width():
    return canvas_width

def get_canvas_height():
    return canvas_height


def open_canvas(w=int(800), h=int(600), sync=False, full=False):
    global window, renderer
    global canvas_width, canvas_height
    global debug_font
    global audio_on

    canvas_width, canvas_height = w, h

    # all the initialization needs to be check for working
    SDL_Init(SDL_INIT_EVERYTHING)
    IMG_Init(IMG_INIT_JPG | IMG_INIT_PNG | IMG_INIT_TIF | IMG_INIT_WEBP)
    TTF_Init()


    Mix_Init(MIX_INIT_MP3 | MIX_INIT_OGG)

    ret = Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, MIX_DEFAULT_CHANNELS, 1024)
    if -1 == ret:
        print('WARNING: Audio functions are disabled due to speaker or sound problems')
    else:
        audio_on = True


    if audio_on:
        Mix_Volume(-1, 128)
        Mix_VolumeMusic(128)


    #SDL_GL_SetAttribute(SDL_GL_DOUBLEBUFFER, 0);
    caption = ('Pico2D Canvas (' + str(w) + 'x' + str(h) + ')' + ' 1000.0 FPS').encode('UTF-8')
    if full:
        flags = SDL_WINDOW_FULLSCREEN
    else:
        flags = SDL_WINDOW_SHOWN
    #window = SDL_CreateWindow(caption, SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, w, h, flags)
    window = SDL_CreateWindow(caption, SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, w, h, flags)
    if sync:
        renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC)
    else:
        renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED)

    if renderer is None:
        renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_SOFTWARE)

    #SDL_ShowCursor(SDL_DISABLE)




    clear_canvas()
    update_canvas()
    clear_canvas()
    update_canvas()


    # debug not work when building release version including pico2d
    debug_font_path = os.getenv('PICO2D_DATA_PATH') + '/ConsolaMalgun.TTF'
    try:
        debug_font = load_font(debug_font_path, 16)
    except:
        debug_font = None
        print('warning: debug_print is not working')

def close_canvas():
    if audio_on:
        Mix_HaltMusic()
        Mix_HaltChannel(-1)
        Mix_CloseAudio()
        Mix_Quit()
    TTF_Quit()
    IMG_Quit()
    SDL_DestroyRenderer(renderer)
    SDL_DestroyWindow(window)
    SDL_Quit()



def resize_canvas(w, h):
    global canvas_height, canvas_width
    canvas_width, canvas_height = w, h
    SDL_SetWindowSize(window, w, h)
    caption = ('Pico2D Canvas (' + str(w) + 'x' + str(h) + ')' + ' 1000.0 FPS').encode('UTF-8')
    SDL_SetWindowTitle(window, caption)
    clear_canvas_now()





def show_lattice():
    global lattice_on
    lattice_on = True
    clear_canvas()
    update_canvas()

def hide_lattice():
    global lattice_on
    lattice_on = False
    clear_canvas()
    update_canvas()



def clear_canvas():
    SDL_SetRenderDrawColor(renderer, 200, 200, 210, 255)
    SDL_RenderClear(renderer)
    if lattice_on:
        SDL_SetRenderDrawColor(renderer, 180, 180, 180, 255)
        for x in range(0, canvas_width, 10):
            SDL_RenderDrawLine(renderer, x, 0, x, canvas_height)
        for y in range(canvas_height-1, 0, -10):
            SDL_RenderDrawLine(renderer, 0, y, canvas_width, y)
        SDL_SetRenderDrawColor(renderer, 160, 160, 160, 255)

        for x in range(0, canvas_width, 100):
            SDL_RenderDrawLine(renderer, x, 0, x, canvas_height)
        for y in range(canvas_height-1, 0, -100):
            SDL_RenderDrawLine(renderer, 0, y, canvas_width, y)


def clear_canvas_now():
	clear_canvas()
	update_canvas()
	clear_canvas()
	update_canvas()

def update_canvas():
    SDL_RenderPresent(renderer)

def show_cursor():
    SDL_ShowCursor(SDL_ENABLE)

def hide_cursor():
    SDL_ShowCursor(SDL_DISABLE)

cur_time = 0.0
def print_fps():
    global window
    global cur_time
    global canvas_width, canvas_height
    dt = get_time() - cur_time
    cur_time += dt
    dt = max(dt, 0.0001)
    caption = ('Pico2D Canvas (' + str(canvas_width) + 'x' + str(canvas_height) + ')' + ' %4.2f FPS' % (1.0/dt)).encode('UTF-8')
    SDL_SetWindowTitle(window, caption)


def debug_print(str):
    global canvas_height
    global debug_font
    if debug_font is not None:
        debug_font.draw(0, canvas_height - 10, str, (0,255,0))

class Event:
    """Pico2D Event Class"""
    def __init__(self, evt_type):
        self.type = evt_type
        self.key = None
        self.button = None
        self.x = None
        self.y = None


def get_events():
    print_fps()
    SDL_Delay(1)
    sdl_event = SDL_Event()
    events = []
    while SDL_PollEvent(ctypes.byref(sdl_event)):
        event = Event(sdl_event.type)
        if event.type in (SDL_QUIT, SDL_KEYDOWN, SDL_KEYUP, SDL_MOUSEMOTION, SDL_MOUSEBUTTONDOWN, SDL_MOUSEBUTTONUP):
            events.append(event)
            if event.type == SDL_KEYDOWN or event.type == SDL_KEYUP:
                if not sdl_event.key.repeat:
                    event.key = sdl_event.key.keysym.sym
            elif event.type == SDL_MOUSEMOTION:
                event.x, event.y = sdl_event.motion.x, sdl_event.motion.y
            elif event.type == SDL_MOUSEBUTTONDOWN or event.type == SDL_MOUSEBUTTONUP:
                event.button, event.x, event.y = sdl_event.button.button, sdl_event.button.x, sdl_event.button.y

    return events


def to_sdl_rect(x,y,w,h):
    return SDL_Rect(int(x), int(-y+canvas_height-h), int(w), int(h))

# for debugging draw
def draw_rectangle(x1,y1,x2,y2):
    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255)
    rect = SDL_Rect(int(x1),int(-y2+canvas_height-1),int(x2-x1+1),int(y2-y1+1))
    SDL_RenderDrawRect(renderer, rect)

class Image:
    """Pico2D Image Class"""

    def __init__(self, texture):
        self.texture = texture
        # http://wiki.libsdl.org/SDL_QueryTexture
        w, h = c_int(), c_int()
        SDL_QueryTexture(self.texture, None, None, ctypes.byref(w), ctypes.byref(h))
        self.w, self.h = w.value, h.value

    def __del__(self):
        SDL_DestroyTexture(self.texture)

    def rotate_draw(self, rad, x, y, w = None, h = None):
        """Rotate(in radian unit) and draw image to back buffer, center of rotation is the image center"""
        if w == None and h == None:
            w,h = self.w, self.h
        rect = to_sdl_rect(x-w/2, y-h/2, w, h)
        SDL_RenderCopyEx(renderer, self.texture, None, rect, math.degrees(-rad), None, SDL_FLIP_NONE)

    def composite_draw(self, rad, flip, x, y, w = None, h = None):
        if w is None and h is None:
            w,h = self.w, self.h
        rect = to_sdl_rect(x-w/2, y-h/2, w, h)
        flip_flag = SDL_FLIP_NONE
        if 'h' in flip:
            flip_flag |= SDL_FLIP_HORIZONTAL
        if 'v' in flip:
            flip_flag |= SDL_FLIP_VERTICAL
        SDL_RenderCopyEx(renderer, self.texture, None, rect, math.degrees(-rad), None, flip_flag)

    def draw(self, x, y, w=None, h=None):
        """Draw image to back buffer"""
        if w == None and h == None:
            w,h = self.w, self.h
        rect = to_sdl_rect(x-w/2, y-h/2, w, h)
        SDL_RenderCopy(renderer, self.texture, None, rect)

    def draw_to_origin(self, x, y, w=None, h=None):
        """Draw image to back buffer"""
        if w == None and h == None:
            w,h = self.w, self.h
        rect = to_sdl_rect(x, y, w, h)
        SDL_RenderCopy(renderer, self.texture, None, rect)



    def clip_draw(self, left, bottom, width, height, x, y, w=None, h=None):
        """Clip a rectangle from image and draw"""
        if w == None and h == None:
            w,h = width, height
        src_rect = SDL_Rect(left, self.h - bottom - height, width, height)
        dest_rect = to_sdl_rect(x-w/2, y-h/2, w, h)
        SDL_RenderCopy(renderer, self.texture, src_rect, dest_rect)

    def clip_composite_draw(self, left, bottom, width, height, rad, flip, x, y, w = None, h = None):
        if w is None and h is None:
            w,h = self.w, self.h
        src_rect = SDL_Rect(left, self.h - bottom - height, width, height)
        dst_rect = to_sdl_rect(x-w/2, y-h/2, w, h)
        flip_flag = SDL_FLIP_NONE
        if 'h' in flip:
            flip_flag |= SDL_FLIP_HORIZONTAL
        if 'v' in flip:
            flip_flag |= SDL_FLIP_VERTICAL
        SDL_RenderCopyEx(renderer, self.texture, src_rect, dst_rect, math.degrees(-rad), None, flip_flag)

    def clip_draw_to_origin(self, left, bottom, width, height, x, y, w=None, h=None):
        """Clip a rectangle from image and draw"""
        if w == None and h == None:
            w,h = width, height
        src_rect = SDL_Rect(left, self.h - bottom - height, width, height)
        dest_rect = to_sdl_rect(x, y, w, h)
        SDL_RenderCopy(renderer, self.texture, src_rect, dest_rect)


    def draw_now(self, x, y, w=None, h=None):
        """Draw image to canvas immediately"""
        self.draw(x,y,w,h)
        update_canvas()
        self.draw(x,y,w,h)
        update_canvas()
        '''
        if w == None and h == None:
            w,h = self.w, self.h
        rect = to_sdl_rect(x-w/2, y-h/2, w, h)
        SDL_RenderCopy(renderer, self.texture, None, rect);
        SDL_RenderPresent(renderer)
        '''

    def opacify(self, o):
        SDL_SetTextureAlphaMod(self.texture, int(o*255.0))

    def clip_image(self, left, bottom, width, height):
        clip_texture = SDL_CreateTexture(renderer, SDL_PIXELFORMAT_RGBA8888, SDL_TEXTUREACCESS_TARGET, width, height)
        SDL_SetRenderTarget(renderer, clip_texture)
        SDL_RenderClear(renderer)
        src_rect = SDL_Rect(left, self.h - bottom - height, width, height)
        SDL_RenderCopy(renderer, self.texture, src_rect, None)
        SDL_SetRenderTarget(renderer, None)
        return Image(clip_texture)


def load_image(name):
    texture = IMG_LoadTexture(renderer, name.encode('UTF-8'))
    if (not texture):
	    print('cannot load %s' % name)
	    raise IOError

    image = Image(texture)
    return image



class Font:
    def __init__(self, name, size=20):
        #print('font' + name + 'loaded')
        self.font = TTF_OpenFont(name.encode('utf-8'), size)
        if (not self.font):
            print('cannot load %s' % name)
            raise IOError

    def draw(self, x, y, str, color=(0,0,0)):
        sdl_color = SDL_Color(color[0], color[1], color[2])
        #print(str)
        surface = TTF_RenderUTF8_Blended(self.font, str.encode('utf-8'), sdl_color)
        texture = SDL_CreateTextureFromSurface(renderer, surface)
        SDL_FreeSurface(surface)
        image = Image(texture)
        image.draw(x+image.w/2, y)



def load_font(name, size = 20):
    font = Font(name, size)
    return font




# only one music can exist at one time
class Music:

    def __init__(self, data):
        self.music = data

    def repeat_play(self):
        Mix_PlayMusic(self.music,-1)

    def play(self, n=1):
        Mix_PlayMusic(self.music, n)

    def set_volume(self, v):
        Mix_VolumeMusic(v)

    def get_volume(self):
        return Mix_VolumeMusic(-1)

    def stop(self):
        Mix_HaltMusic()

    def pause(self):
        Mix_PauseMusic()

    def resume(self):
        Mix_ResumeMusic()

    def __del__(self):
        Mix_FreeMusic(self.music)



class Wav:

    def __init__(self, data):
        self.wav = data

    def repeat_play(self):
        Mix_PlayChannel(-1, self.wav, -1)

    def play(self, n=1):
        Mix_PlayChannel(-1, self.wav, n-1)

    def set_volume(self, v):
        Mix_VolumeChunk(self.wav, v)

    def get_volume(self):
        return Mix_VolumeChunk(self.wav, -1)

    def __del__(self):
        Mix_FreeChunk(self.wav)


def load_music(name):
    if audio_on:
        data = Mix_LoadMUS(name.encode('UTF-8'))
        if (not data):
            print('cannot load %s' % name)
            raise IOError

        return Music(data)
    else:
        print('audio fuctions cannot work due to sound or speaker problems')
        raise IOError


def load_wav(name):
    if audio_on:
        data = Mix_LoadWAV(name.encode('UTF-8'))
        if (not data):
            print('cannot load %s' % name)
            raise IOError

        return Wav(data)
    else:
        print('audio functions cannot work due to sound or speaker problems')
        raise IOError




# for pytmx
from functools import partial
#import pytmx

def pico2d_image_loader(filename, colorkey, **kwargs):

    def extract_image(rect=None, flags=None):
        if rect:
            try:
                flip = ''
                if flags.flipped_horizontally:
                    flip = 'h'
                if flags.flipped_vertically:
                    flip = 'v'
                if flags.flipped_diagonally:
                    flip = 'hv'

                return image, rect, flip

            except ValueError:
                print('Tile bounds outside bounds of tileset image')
                raise
        else:
            return image, None, ''

    image = load_image(filename)

    if colorkey:
        print('color key deprecated')

    return extract_image


def load_tilemap(filename):
    return pytmx.TiledMap(filename, image_loader=pico2d_image_loader)




def test_pico2d():
    pass


def main():
	pass


print("Pico2d is prepared.")
if __name__ == "__main__":
    test_pico2d()


