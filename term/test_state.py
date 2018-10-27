import game_framework
from pico2d import *
import math

# 임시로 테스트용 스테이트를 만듬
# 본 게임 예상 / 캐릭터 선택창 -> 본게임 -> 엔딩 -> 타이틀
name = 'Test_state'

class Rope:
    def __init__(self):
        self.angle = 0
        self.Max = 50
        self.line = 300
        self.dir = 1
        self.image = load_image('..\\resource\\character.png')

    def draw(self):
        clear_canvas()
        tmp = [self.line * math.sin(self.angle * 3.14 * 180), self.line * math.cos(self.angle * 3.14 * 180)]
        self.image.clip_draw(0,0,100,100,tmp[0],720-tmp[1])
        update_canvas()

    def update(self):
        if dir == 1:
            self.angle += 1

        else:
            self.angle -= 1

        if self.angle == 50 or self.angle == -50:
            dir = (dir + 1) % 2


def enter():
    pass

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
    pass

def draw():
    pass

def update():
    pass

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