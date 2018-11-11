from pico2d import *
import game_framework
import main_state

def enter():
	global bgImage
	bgImage = load_image('../res/title.png')

def exit():
	global bgImage
	del bgImage

def draw():
	clear_canvas()
	bgImage.draw(640, 360)
	update_canvas()

def update():
	delay(0.03)

def handle_events():
	events = get_events()
	for e in events:
		if e.type == SDL_QUIT:
			game_framework.quit()
		elif e.type == SDL_KEYDOWN:
			if e.key == SDLK_ESCAPE:
				game_framework.quit()
			elif e.key == SDLK_SPACE:
				game_framework.push_state(main_state)

def pause():
	pass

def resume():
	pass

if __name__ == '__main__':
	import sys
	current_module = sys.modules[__name__]	
	open_canvas(1280, 720)
	game_framework.run(current_module)
	close_canvas()
