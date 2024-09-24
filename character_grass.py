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
    for x in range(50,750,10):
        draw_boy(x, 550)

def run_right():
    for y in range(550,50,-10):
        draw_boy(750, y)

def run_bottom():
    for x in range(750,50,-10):
        draw_boy(x, 50)

def run_left():
    for y in range(50,550,10):
        draw_boy(50, y)

def run_right_up():
    pass

def run_right_down():
    pass


def run_rectangle():
    run_top()
    run_right()
    run_bottom()
    run_left()

def run_circle():
    r, cx, cy = 200 , 800 // 2, 600 // 2

    for d in range(270, -(90 + 1), -1):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy
        draw_boy(x,y)

def run_triangle():
    run_bottom()
    run_right_up()
    run_right_down()
    pass

while True:
    #run_rectangle()
    #run_circle()
    run_triangle()

close_canvas()