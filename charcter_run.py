from pico2d import *
import math
open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')
#문제의조건을 먼저 제대로 인식하자.
#pass는 아무 일도 안하는 c로 따지면 {}와 같다.

def run_circle():
    print("circle")
    pass
def run_rectangle():
    printf("rectangle")
    pass

while True:
    run_circle()
    run_rectangle()
    break
close_canvas()
