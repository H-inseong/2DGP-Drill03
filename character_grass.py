from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x,y):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.01)

def run_top():
    print('top')
    for x in range(50,750,10):
        draw_boy(x, 550)
    pass

def run_right():
    print('right')
    for y in range(550,50,-10):
        draw_boy(750, y)
    pass

def run_bottom():
    print('bottom')
    for x in range(750,50,-10):
        draw_boy(x, 50)
    pass

def run_left():
    print('left')
    for y in range(50,550,10):
        draw_boy(50, y)
    pass

def run_rectangle():
    print('rectangle')
    run_top()
    run_right()
    run_bottom()
    run_left()

    pass

def run_circle():
    print('circle')

    r, cx, cy = 200 , 800 // 2, 600 // 2

    for d in range(270, -(90 + 1), -1):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy
        draw_boy(x,y)


while True:
    run_rectangle()
    run_circle()
    break


close_canvas()
