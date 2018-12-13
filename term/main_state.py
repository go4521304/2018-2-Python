from pico2d import *
import game_framework
import math

class Player:
	image = None


	WH = [120, 160]
	state = ['Sleep', 'Click', 'Swing', 'Jump']
	pos_center = [320, 720] 
	
	def __init__(self):
		if (Player.image == None):
			Player.image = load_image("../res_term/character_1.png")
		
		self.cur_state = Player.state[0]
		self.radious = 100

		self.pos = [320, 720 - self.radious]
		self.t_pos = [0, 0]

		self.way = 0

		self.max_angle = 0.0
		self.angle = 0.0
		self.velocity = 0.0

	def change_state(self, key):
		# Sleep
		if key == Player.state[0]:
			self.cur_state = player.state[0]
		# Click
		elif key == Player.state[1]:
			self.cur_state = player.state[1]
		# Swing
		elif key == Player.state[2]:
			self.cur_state = player.state[2]
		# Jump
		elif key == Player.state[3]:
			self.cur_state = player.state[3]

	def update(self):
		# Sleep
		if self.cur_state == player.state[0]:
			pass

		# Click
		elif self.cur_state == player.state[1]:
			self.angle = math.atan2((player.t_pos[1] - player.pos_center[1]), (player.t_pos[0] - player.pos_center[0]))
			self.angle += math.pi / 2
			if self.angle > 3.0:
				self.angle = -1.5707963267948966
			
			self.max_angle = self.angle
			if self.max_angle > 0:
				self.way = 1
			else:
				self.way = -1

			self.pos = [Player.pos_center[0] + (math.sin(self.angle) * self.radious), 720 - (math.cos(self.angle) * self.radious)]			
			print (self.angle)

		# Swing	
		elif self.cur_state == player.state[2]:
			if self.velocity == 0:
				self.way *= -1
				self.angle = self.angle + (self.way * 0.001)
				
			if (abs(self.angle) > abs(self.max_angle)):
				self.angle = abs(self.max_angle) * (self.way)

			self.velocity = math.sqrt(2 * 9.8 * self.radious / 100 * (math.cos(self.angle) - math.cos(self.max_angle)))
			print(self.velocity, self.angle)
			self.angle = self.angle + (self.velocity / self.radious * self.way)

			self.pos = [Player.pos_center[0] + (math.sin(self.angle) * self.radious), 720 - (math.cos(self.angle) * self.radious)]

		elif self.cur_state == player.state[3]:
			pass



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
			
		# M_BT_L
		elif (e.type, e.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_LEFT):
			player.change_state('Jump')
			print ('Jump state')

		# M_BT_R
		if player.cur_state == 'Jump':
			return
		elif (e.type, e.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_RIGHT):
			if abs(player.pos[0] - e.x) <= player.WH[0] and abs(720 - player.pos[1] - e.y) <= player.WH[1]:
				player.change_state('Click')
				player.t_pos = [e.x, 720 - e.y]
				player.max_angle = 0
				player.angle = 0
				player.velocity = 0
				print ('Click state')

		elif (e.type, player.cur_state) == (SDL_MOUSEMOTION, player.state[1]) and player.cur_state == player.state[1]:
			player.t_pos = [e.x, 720 - e.y]

		elif (e.type, e.button) == (SDL_MOUSEBUTTONUP, SDL_BUTTON_RIGHT) and player.cur_state == player.state[1]:
			player.change_state('Swing')
			print ("Swing State")


			 

def update():
	global player
	player.update()

def draw():
	global player
	player.draw()