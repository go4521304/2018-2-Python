from pico2d import *
import game_framework
import math
import time
import json

class Obj:
	WH = [10, 100]
	def __init__(self):
		self.stage = '0'
		self.num = '0'
		self.length = []
		self.monster_num = 0
		self.monster = []
		self.monster_type = []

class Player:
	STAGE_NUM = None

	image = None
	image_back = None
	image_rope = None
	WH = [120, 160]
	state = ['Sleep', 'Click', 'Swing', 'Jump']
	pos_center = [320, 720] 
	
	def __init__(self):
		global rope
		if (Player.image == None):
			Player.image = load_image("../res_term/character_1.png")
		if (Player.image_back == None):
			Player.image_back = [load_image("../res_term/Stage_1_B.png"), load_image("../res_term/Stage_2_B.png")\
			, load_image("../res_term/Stage_3_B.png"), load_image("../res_term/Stage_4_B.png")]
		if (Player.image_rope == None):
			Player.image_rope = load_image("../res_term/Rope.png")
		
		if (Player.STAGE_NUM == None):
			Player.STAGE_NUM = 0

		self.rope_num = 0
		
		self.cur_state = Player.state[0]
		self.radious = rope[Player.STAGE_NUM].length[self.rope_num]

		self.pos = [320, 720 - self.radious]
		self.t_pos = [0, 0]

		self.way = 0

		self.max_angle = 0.0
		self.angle = 0.0
		self.velocity = 0.0

		self.fram_count = 0

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

	# type == 0 / rope
	def check_Boundary(self, Target, type):
		if (type == 0):
			if (self.pos[0] + self.WH[0] > 960 and self.pos[0] - self.WH[0] < 960) and\
			 (self.pos[1] - self.WH[1] < Target * 100 and self.pos[1] + self.WH[1] > (Target + 1) * 100):
			 return True 

	def scrolling(self):
		

	def reset(self):
		self.rope_num += 1
		self.radious = rope[Player.STAGE_NUM].length[self.rope_num]
		self.pos = [320, 720 - self.radious]
		self.t_pos = [0, 0]
		self.way = 0
		self.max_angle = 0.0
		self.angle = 0.0
		self.velocity = 0.0
		self.fram_count = 0

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

			self.velocity = math.sqrt(2 * 9.8 * self.radious / 50 * (math.cos(self.angle) - math.cos(self.max_angle)))
			print(self.velocity, self.angle)
			self.angle = self.angle + (self.velocity / self.radious * self.way)

			self.pos = [Player.pos_center[0] + (math.sin(self.angle) * self.radious), 720 - (math.cos(self.angle) * self.radious)]

		# Jump
		elif self.cur_state == player.state[3]:
			self.pos[0] = self.pos[0] + (self.velocity * math.cos(self.angle)) * 3
			self.pos[1] = self.pos[1] + ((self.velocity * math.sin(self.angle) - (9.8 * (time.time() - self.fram_count)/2)))

			for i in range ((int)(rope[self.STAGE_NUM].length[self.rope_num]/100)):
				if (self.check_Boundary(i, 0) == True):
					self.change_state('Sleep')
					self.scrolling()
					self.reset()
					return


			#if self.pos[1] > 620:
			#	game_framework.change_state(game_over)
			#	return


	def draw(self):
		global rope
		clear_canvas()
		player.image_back[self.STAGE_NUM].clip_draw(0, 0, 1280, 720, 1280/2, 720/2)
		for i in range((int)(rope[self.STAGE_NUM].length[self.rope_num]/100)):
			Player.image_rope.clip_composite_draw(0, 0, 35, 100, self.angle, 'None',\
			 Player.pos_center[0] + (math.sin(self.angle) * i * 100), 720 - (math.cos(self.angle) * i * 100), 10, 100)

		for i in range((int)(rope[self.STAGE_NUM].length[self.rope_num + 1]/100)):
			Player.image_rope.clip_draw(0, 0, 35, 100, 960, 720 - (i * 100), 10, 100)

		Player.image.clip_draw(0, 0, 120, 160, self.pos[0], self.pos[1])
		update_canvas()
	

def enter():
	global player
	global rope
	rope = []

	fh = open('obj_date.json', 'r')
	data = json.load(fh)
	for e in data["Stage"]:
		St = Obj()
		St.stage = e['stage_num']
		St.num = e['num']
		St.length = e['length']
		St.monster_num = e['monster_num']
		St.monster = e['monster']
		St.monster_type = e['monster_type']
		rope.append(St)
	
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
			player.fram_count = time.time()
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