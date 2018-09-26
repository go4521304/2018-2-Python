from pico2d import *
import random

def handle_events():
    global running
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, event.y

class Grass:
    def __init__(self):
        self.image = load_image("..\\resource\\grass.png")

    def draw(self):
        self.image.draw(400, 30)

class Boy():
    def __init__(self):
        self.image = load_image("..\\resource\\run_animation.png")

open_canvas()
grass = Grass()

running = True
x, y = 400,90

while(running):
    handle_events()

    clear_canvas()
    grass.draw()

    update_canvas()
    delay(0.01)


close_canvas()