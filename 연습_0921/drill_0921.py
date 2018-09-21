from pico2d import *
import random


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
        self.image = load_image("..\\resource\\grass.png")

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image("..\\resource\\run_animation.png")
        self.frame = 0
        self.x, self.y = random.randint(0, 200), random.randint(90, 550)
        self.frame = random.randint(0, 7)
        self.speed = random.uniform(1.0, 2.0)

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.speed


open_canvas()

boys = [Boy() for i in range(20)]
#boys = [ Boy() ] * 20 이건 안됨

grass = Grass()

running = True

while(running):
    handle_events()

    clear_canvas()
    grass.draw()

    for b in boys:
        b.draw()

    update_canvas()

    for b in boys:
        b.update()
    delay(0.03)

close_canvas()