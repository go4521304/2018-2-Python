import game_framework
from pico2d import *

def enter():
	pass

def exit():
	pass

def pause():
	pass

def resume():
	pass

def handle_events():
	events = get_events()
	for e in events:
		if e.type == SDL_QUIT:
			game_framework.quit()
		elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
			game_framework.quit()


def update():
	pass

def draw():
	pass