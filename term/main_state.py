from pico2d import *
import game_framework
import game_world

from player import Player
from rope import Rope


def handle_events():
    pass


def enter():
    global player
    global rope_main

    player = Player()
    rope_main = Rope()

def exit():
    global player
    global rope_main

def draw():
    pass

def update():
    pass


if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas(1280, 720)
    game_framework.run(current_module)
    close_canvas()