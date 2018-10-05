from pico2d import *
import game_framework

import random
import math

class Grass:
    def __init__(self):
        self.image = load_image("..\\resource\\grass.png")

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image("..\\resource\\run_animation.png")
        self.x = random.randint(0, 800 - 1)
        self.y = random.randint(90, 200)
        self.frame = random.randint(0, 7)
        self.speed = random.randint(2 ,5)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def image_update(self):
        global way

        self.degree = math.atan2(float(way[1]) - float(self.y), float(way[0]) - float(self.x))

        self.x += math.cos(self.degree) * self.speed
        self.y += math.sin(self.degree) * self.speed
        self.frame = (self.frame + 1) % 8

grass = None
boys = []
way = []

def handle_events():
    global way

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()

        elif event.type == SDL_MOUSEMOTION:
            way = [event.x, 600 - 1 - event.y]

def enter():
    global grass
    global boys
    global way

    grass = Grass()
    boys = [Boy() for i in range(20)]
    way = [0, 0]

def exit():
    global boys
    global grass
    global way

    del(boys)
    del(grass)
    del(way)
    

def draw():
    global grass
    global boys

    clear_canvas()

    grass.draw()
    for i in boys:
        i.draw()

    update_canvas()


def update():
    global boys
    for i in boys:
        i.image_update()

    delay(0.03)


if __name__ == '__main__':
    import sys
    current_module = sys.modules[__name__]
    open_canvas()
    game_framework.run(current_module)
    close_canvas()