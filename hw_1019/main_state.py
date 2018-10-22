from pico2d import *
import game_framework

from boy import Boy
from grass import Grass

name = 'main_state'

boy = None
grass = None

def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()

def exit():
    global boy, grass
    del(boy)
    del(grass)

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        else:
            boy.handle_event(event)

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()