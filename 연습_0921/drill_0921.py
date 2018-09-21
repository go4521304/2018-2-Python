from pico2d import *
import os

os.chdir("..\\resource")

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

class Grass:
    def __init__(self):
        self.image = load_image("grass.png")

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image("run_animation.png")
        self.frame = 0
        self.x, self.y = 0, 90

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5


open_canvas()

boy = Boy()
grass = Grass()

running = True

while(running):
    handle_events()

    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

    boy.update()
    delay(0.02)

close_canvas()