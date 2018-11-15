from pico2d import *
import time
import math

class Player:
    def __init__(self):
        # stable value
        self.image = load_image("../res_term/character_1.png")
        self.gravity = 0.1
        self.length = 500

        # floating value
        self.pos = [640, 720 - 1 - (self.length)]
        self.angle = 0.0

        # L->R == 1
        # L<-R == -1
        self.angle_dir = 1

        # 각속도
        self.angle_velocity = 1.0

        # 가/감속 상태
        # gravity * state
        self.state = -1

        #self.resistance = 0.0
        self.velocity = 0
        self.parabola_high_pos = [0,0]

    def swing(self, frame_time):
        current_angle = self.angle
        current_velocity = self.angle_velocity

        # 속도 적용
        self.angle = self.angle + (self.angle_velocity * self.angle_dir) * frame_time

        # 속도 변화
        self.angle_velocity = self.angle_velocity + (self.gravity * self.state)

        # 방향 감지하고 바꿔줌
        if (current_velocity > 0.0 and self.angle_velocity < 0.0) or (current_velocity < 0.0 and self.angle_velocity > 0.0):
            self.angle_velocity = 0.0
            self.state *= -1
            self.angle_dir *= -1

        # 가/감속 상태 변화
        elif (current_angle > 0.0 and self.angle < 0.0) or (current_angle < 0.0 and self.angle > 0.0):
            self.angle = 0.0
            self.state *= -1

        self.pos[0] = (int)(640 + (self.length * math.sin(self.angle)))
        self.pos[1] = (int)(720 - 1 - self.length * math.cos(self.angle))
        #print (self.angle)

        print ("angle_dir: %d    angle: %f   angle_velocity: %f    pos: [%f, %f]   state: %f"\
               %(self.angle_dir, self.angle, self.angle_velocity, self.pos[0], self.pos[1], self.state))
        pass

    def jump(self):
        self.velocity = self.angle_velocity * self.length
        self.parabola_high_pos = [(self.velocity**2) * math.sin(self.angle) * math.cos(self.angle) / self.gravity,
                                  (self.velocity ** 2) * (math.sin(self.angle)**2)/2/self.gravity]
        

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