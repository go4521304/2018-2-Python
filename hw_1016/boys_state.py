from pico2d import *
import json
import game_framework

import random
import math

class Grass:
    def __init__(self):
        self.image = load_image("..\\resource\\grass.png")

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    image = None

    def __init__(self):
        self.x = random.randint(0, 800 - 1)
        self.y = random.randint(90, 200)
        self.name = "None"
        self.frame = random.randint(0, 7)
        self.speed = random.uniform(1 ,30)
        self.state = 0
        self.check = False

        if Boy.image == None:
            Boy.image = load_image("..\\resource\\animation_sheet.png")

    def draw(self):
        Boy.image.clip_draw(self.frame * 100, self.state * 100, 100, 100, self.x, self.y)

    def image_update(self):
        global way

        d = [way[0] - self.x, way[1] - self.y]
        #way[0] - self.x, way[1] - self.y

        dist = math.sqrt(d[0] ** 2 + d[1] ** 2)

        if dist > 0:
            self.check = False

            self.x += self.speed * d[0] / dist
            self.y += self.speed * d[1] / dist

            if d[0] < 0 and self.x < way[0]: self.x = way[0]
            if d[0] > 0 and self.x > way[0]: self.x = way[0]
            if d[0] < 0:
                self.state = 0
                if self.x < way[0]:
                    self.x = way[0]
            if d[0] > 0:
                self.state = 1
                if self.x > way[0]:
                    self.x = way[0]

            if d[1] < 0 and self.y < way[1]: self.y = way[1]
            if d[1] > 0 and self.y > way[1]: self.y = way[1]

        if dist == 0 and self.check == False:
            self.check = True
            self.state = (self.state + 2) % 4

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

    boys = []
    fh = open('boys_data.json')
    data = json.load(fh)
    for e in data['boys']:
        b = Boy()
        b.name = e['name']
        b.x = e['x']
        b.y = e['y']
        b.speed = e['speed']
        boys.append(b)

    grass = Grass()
    way = [0, 0]
    #boys = [Boy() for i in range(1000)]

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