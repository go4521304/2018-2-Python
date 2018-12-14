from pico2d import *

import game_framework
import main_state
import title_state


class Game_over:
    image = None
    def __init__(self):
        if (Game_over.image == None):
            Game_over.image = load_image('../res_term/Game_over.png')
        
        self.font = load_font('../res_term/netmarbleM.ttf', 50)
        self.message_Re = [50,720 - 100]
        self.message_Title = [50, 720 - 250]

    def draw(self):
        clear_canvas()
        Game_over.image.clip_draw(0, 0, 1280, 720, 1280/2, 720/2)
        self.font.draw(self.message_Re[0], self.message_Re[1], "RETRY", (255,140,0))
        self.font.draw(self.message_Re[0], self.message_Re[1] - 50, "press Space", (255,140,0))

        self.font.draw(self.message_Title[0], self.message_Title[1], "Title", (255,140,0))
        self.font.draw(self.message_Title[0], self.message_Title[1] - 50, "press ESC", (255,140,0))

        update_canvas()


def enter():
    global over
    over = Game_over()

def exit():
	pass

def pause():
	pass

def resume():
	pass

def handle_events():
    global over
    events = get_events()
    for e in events:
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()
        
        elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)


def update():
	pass

def draw():
    global over
    over.draw()
