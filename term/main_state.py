from pico2d import *
import game_framework
import math

class Player:
	image = None
	
	def __init__(self):
		if (Player.image == None):
			Player.image = load_image("../res_term/character_1.png")
		
		self.way = 0
		self.angle_max = 0.0
		self.angle = 0.0
		self.velocity = 0.0
		self.radius = 200
		self.pos = [240, 720 - self.radius]

	def update(self):
		if (self.way == 0):
			return




	def draw(self):
		clear_canvas()
		Player.image.clip_draw(0, 0, 120, 160, self.pos[0], self.pos[1])
		update_canvas()
	
def enter():
	global player
	player = Player()

def exit():
	global player
	del(player)

def pause():
	pass

def resume():
	pass

def handle_events():
	global player
	events = get_events()
	for e in events:
		if (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
			game_framework.pop_state()

def update():
	global player
	player.update()

def draw():
	global player
	player.draw()