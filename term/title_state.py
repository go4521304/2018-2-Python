from pico2d import *

import game_framework
import main_state


def enter():
	global title
	global font
	title = load_image("../res_term/title.png")
	font = load_font('../res_term/netmarbleM.ttf', 100)

def exit():
	global title
	del(title)

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
			return
		
		elif (e.type, e.key) == (SDL_KEYDOWN, SDLK_SPACE):
			game_framework.push_state(main_state)
		
		
def update():
	pass

def draw():
	global font
	clear_canvas()
	title.draw(1280/2, 720/2)
	font.draw(200, 100,"동아줄을 타고 도망가자!", (255,255,255))
	update_canvas()

if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas(1280, 720)
	game_framework.run(current_module)
	close_canvas()
