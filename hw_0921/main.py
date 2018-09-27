from pico2d import *
import random
<<<<<<< HEAD
import math
=======

def handle_events():
    global running
    global x, y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, event.y
>>>>>>> 7e2bb9511926f07769d90c4083375d83b920a63f

class Grass:
    def __init__(self):
        self.image = load_image("..\\resource\\grass.png")

    def draw(self):
        self.image.draw(400, 30)

<<<<<<< HEAD
class Boy:
    def __init__(self):
        self.image = load_image("..\\resource\\run_animation.png")
        self.x = random.randint(0, 800 - 1)
        self.y = random.randint(90, 200)
        self.frame = random.randint(0, 7)
        self.speed = random.randint(5 ,10)
        #speed 는 확인후 수정 예정

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

    def image_update(self):
        global way_x, way_y

        self.degree = math.atan2(float(way_y) - float(self.y), float(way_x) - float(self.x))

        self.x += math.cos(self.degree) * self.speed
        self.y += math.sin(self.degree) * self.speed

        self.frame = (self.frame + 1) % 8


def handle_get():
    global running
    global way_x, way_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_MOUSEMOTION:
            way_x, way_y = event.x, 600 - 1 - event.y

open_canvas(800, 600)
grass = Grass()
boys = [Boy() for i in range(20)]

running = True
way_x, way_y = 0, 0

while(running):
    handle_get()

    clear_canvas()
    grass.draw()
    for i in boys:
        i.draw()

    update_canvas()

    for i in boys:
        i.image_update()
    delay(0.03)
=======
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
>>>>>>> 7e2bb9511926f07769d90c4083375d83b920a63f
