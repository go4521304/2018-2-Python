import game_framework
from pico2d import *
import math

# 임시로 테스트용 스테이트를 만듬
# 본 게임 예상 / 캐릭터 선택창 -> 본게임 -> 엔딩 -> 타이틀
name = 'Test_state'

class Chacter:
    def __init__(self):
        self.image = load_image("..\\res\\character_1.png")

        self.POS = [720/2, 1280-200]   # Current position

        #self.R = 0.5        # Resistance
        self.A =  0.0        # Angle
        self.L = 200         # Length

        self.T = [0.0, 10.0]    # Tension
        self.G = [0.0, -10.0]   # Gravity
        self.V = [0.0, 0.0]     # Velocity
        self.F = [0.0, 0.0]     # Force (by character)

    def draw(self):
        #self.image.clip_draw(0, 0, 120, 160, self.POS[0], self.POS[1])
        print(self.POS, self.T, self.V, self.A)


    def update(self):
        self.POS += [(int)(self.V[0] + self.F[0] + self.G[0] + self.T[0]), (int)(self.V[1] + self.F[1] + self.G[1] + self.T[1])]


ch = None

def enter():
    global ch
    ch = Chacter()

def exit():
    global ch
    del(ch)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
    pass

def draw():
    global ch
    ch.draw()
    delay(1)

def update():
    global ch
    ch.update

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