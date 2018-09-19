import os
from pico2d import *

def handle_events():
	global running

	events = get_events()

	for event in events:
		if event.type == SDL_QUIT:
			running = False
		elif event.type == SDL_KEYDOWN:
			if event.key == SDLK_ESCAPE:
				running = False

def draw_canvas():
	global x, y
	global frame

	grass = load_image('grass.png')
	character = load_image('run_animation.png')

	grass.draw(400, 30)
	character.clip_draw(frame * 100, 0, 100, 100, x, y)
	update_canvas()

open_canvas(800, 600)

os.chdir('..\\resource')
running = True
x, y = 400, 90
frame = 0

while (running):
	i = 0
	while (i < 5 and running):
		clear_canvas()
		draw_canvas()
		if i == 0 or i == 4:
			x += 5
		elif i == 1:
			y += 5
		elif i == 2:
			x -= 5
		elif i == 3:
			y -= 5

		if (x < 0 or x > 800 or y < 90 or y > 600):
			i += 1

		frame = (frame + 1) % 8
		delay(0.01)
		handle_events()

close_canvas()