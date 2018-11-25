import game_framework
from pico2d import *
import time

import title_state

def enter():
	global image, startOn
	image = load_image("../res_term/logo.png")
	startOn = time.time()

def exit():
	global image
	del(image)

def pause():
	pass

def resume():
	pass

def handle_events():
	events = get_events()
	for e in events:
		if e.type == SDL_QUIT:
			game_framework.quit()

		elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
			game_framework.change_state(title_state)
			return

def update():
	global startOn
	elapsed = time.time() - startOn

	if (elapsed >= 1.0):
		game_framework.change_state(title_state)
		return

	delay(0.03)

def draw():
	clear_canvas()
	image.draw(1280/2, 720/2)
	update_canvas()

if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas(1280, 720)
	game_framework.run(current_module)
	close_canvas()