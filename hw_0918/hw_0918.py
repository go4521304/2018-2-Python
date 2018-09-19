from pico2d import *
import os

def handle_events():
    global running
    global dir
    global tx, ty

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir = 5
            elif event.key == SDLK_LEFT:
                dir = -5
        elif event.type == SDL_MOUSEMOTION:
            tx, ty = event.x, 600 - 1 - event.y

os.chdir('..\\resource')

running = True
x, y = 0 ,0
tx, ty = 0, 0
frame = 0
dir = 0

speed = 5

open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')
while running:
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()

    if tx < x:
        x -= speed
        if tx > x:
            x = tx
    elif tx > y:
        x += speed
        if tx < x:
            x = tx

    if ty < y:
        y -= speed
        if ty > y:
            y = ty

    elif ty > y:
        y += speed
        if ty < y:
            y = ty

    frame = (frame + 1) % 8

close_canvas()