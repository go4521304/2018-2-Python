from pico2d import *
import time
import math

class Player:
    def __init__(self):
        # stable value
        self.image = load_image("../res_term/character_1.png")
        self.gravity = 1
        self.length = 50

        # floating value
        self.pos = [640, 720 - 1 - (self.length * 10)]
        self.angle = 0.0

        self.velocity = 10
        self.dir = 1
        self.state = -1

        #self.resistance = 0.0

    def swing(self, frame_time):
        current_velocity = self.velocity
        # pos update
        self.pos[0] += (self.velocity * self.dir) * frame_time
        x = 640 - self.pos[0]
        self.angle = math.acos(x/self.length)
        self.pos[1] = 720 - 1 -(self.length * math.cos(self.angle))

        # velocity update
        self.velocity = self.velocity + (self.gravity * self.state)

        if (self.velocity > 0 and current_velocity < 0) or (self.velocity < 0 and current_velocity > 0):
            self.dir *= -1
            self.state *= -1

        elif self.angle == 0:
            self.state *= -1

        print ("pos: %d, %d    angle: %f    dir: %d    state: %d    velocity: %f" %(self.pos[0], self.pos[1], self.angle, self.dir, self.state, self.velocity))

        pass

    def jump(self):
        pass

    def draw(self):
        clear_canvas()
        self.image.clip_draw(0, 0, 120, 160, self.pos[0], self.pos[1])
        update_canvas()


open_canvas(1280, 720, sync=True)

frame_time = 0.0

player = Player()
current_time = time.time()
delay(0.1)
while(True):
    frame_time = time.time() - current_time
    frame_rate = 1.0 / frame_time
    current_time += frame_time
    #print ("Frame Time: %f sec, Frame Rate: %f fps" %(frame_time, frame_rate))

    player.swing(frame_time)
    player.draw()
