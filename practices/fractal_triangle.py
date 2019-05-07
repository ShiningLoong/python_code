# -*- coding: gbk -*-
from turtle import *
import random


def draw_tri(side, d=1):
    c = list(map(lambda x: round(random.random()*x), [230, 230, 230]))
    pencolor(*c)
    for i in range(3):
        fd(side)
        lt(120*d)


def draw_tri_inner(side, d=1):
    side /= 2
    fd(side)
    left(60*d)
    draw_tri(side, d)
    right(60*d)
    bk(side)


def recursive_draw(side, d):
    draw_tri_inner(side, d)
    side /= 2
    if side > 20:  # 最小的三角形不能小于1个像素
        # 1
        recursive_draw(side, d)
        # 2
        lt(60*d)
        fd(side)
        rt(60*d)
        recursive_draw(side, d)
        # 3
        recursive_draw(side, -d)
        # 4
        rt(60*d)
        fd(side)
        lt(60*d)
        recursive_draw(side, d)
        bk(side)


if __name__ == "__main__":
    ht()
    speed("fastest")
    colormode(255)
    width(2)
    pencolor(235,133,0)
    origin = (-200, -200)
    s = 512
    penup()
    goto(*origin)
    pendown()
    # Turtle().screen.delay(0)
    tracer(0)
    draw_tri(512)
    recursive_draw(512, 1)
    tracer(1)
    done()
