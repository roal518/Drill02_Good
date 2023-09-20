from pico2d import *
import math
open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')
#문제의조건을 먼저 제대로 인식하자.
#pass는 아무 일도 안하는 c로 따지면 {}와 같다.
#idle 창을 왔다갔다 하면서 의도한대로 움직이는지 확인해보자
#문제를 체크하는 시간을 많이 줄일수 있따.
#가독성을 중요하게 코딩하자.
#for문 이용법을 정확하게 알아 두자.
def render_all(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)
    

def run_circle():
    print("circle")
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400,90)
    delay(1)
    cx = 800/2
    cy = 600/2
    r = 200
    for deg in range(0,360,5):
        x=cx+r*math.cos(math.radians(deg))
        y=cy+r*math.sin(math.radians(deg))
        render_all(x,y)

def run_rectangle():
    for x in range(50,750,10):
         render_all(x,90)
    for y in range(90,550+1,+10):
        render_all(750,y)
    for x in range(750,50-1,-10):
        render_all(x,550)
    for y in range(550,90-1,-10):
        render_all(50,y)


while True:
    run_circle()
    run_rectangle()

close_canvas()
