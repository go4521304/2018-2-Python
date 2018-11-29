from pico2d import *
import game_framework
import math

class Player:
	image = None
	
	def __init__(self):
		if (Player.image == None):
			Player.image = load_image("../res_term/character_1.png")
		
		self.gravity = 9.8
		self.pos = [240, 720 - 100]
		self.way = 1
		self.angle_max = 0.0
		self.angle = 0.0
		self.velocity = 0.0
		self.velocity_angle = 0.0
		self.radius = 100

	def update(self):
		if self.angle_max == 0:
			return

		self.velocity = math.sqrt(2 * self.gravity * self.radius * (math.cos(self.angle) - math.cos(self.angle_max)))
		self.velocity_angle = self.velocity / self.radius

		self.pos = [240 + (self.radius * math.sin(self.angle)), 720 - (self.radius * math.cos(self.angle))]

		self.angle = self.angle + (self.velocity_angle * self.way * game_framework.frame_time)

		if (self.angle < self.angle_max or self.angle > self.angle_max):
			self.angle_max = self.angle_max * -1 / 2
			if (abs(self.angle_max) < 1 * math.pi):
				self.angle_max = 0.0
				self.angle = 0.0
				self.velocity = 0.0
				self.velocity_angle = 0.0

	def draw(self):
		clear_canvas()
		Player.image.clip_draw(0, 0, 120, 160, self.pos[0], self.pos[1])
		update_canvas()
	
def enter():
	global player
	player = Player

def exit():
	global player
	del(player)

def pause():
	pass

def resume():
	pass

def handle_events():
    events = get_events()
    for e in events:
        if (e.type, e.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.pop_state()

def update():
	global player
	player.update

def draw():
	global player
	player.draw