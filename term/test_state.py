import game_framework
from pico2d import *

# 임시로 테스트용 스테이트를 만듬
# 본 게임 예상 / 캐릭터 선택창 -> 본게임 -> 엔딩 -> 타이틀
name = 'Test_state'

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