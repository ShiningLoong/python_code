# coding: GBK
from matplotlib import pyplot as plt
# import numpy as np
from random import random


class Stack(object):
    def __init__(self):
        self.data = list()

    def push(self, e):
        self.data.insert(0, e)

    def pop(self):
        return self.data.pop(0)

    def get_top(self):
        if len(self.data) != 0:
            return self.data[0]
        else:
            return None

    def is_empty(self):
        return len(self.data) == 0


def generate_maze(n):
    _maze = list()
    for num in range(n-2):
        _maze.append([0 if random() >= 0.30 else 1 for _num in range(n-2)])
    # build the wall
    for num in range(n-2):
        _maze[num] = [1] + _maze[num] + [1]
    _maze = [[1]*n] + _maze + [[1]*n]
    return _maze


def mov_x(_x, step):  # 画图时的移动方式
    for num in range(len(_x)):
        _x[num] += step
    return _x


def solve_maze(_maze, _entrance, _out):
    current = _entrance
    stk = Stack()
    _maze[current[0]][current[1]] = -1
    stk.push(current)
    while current != _out and not stk.is_empty():
        up_block = (current[0]-1, current[1])
        rt_block = (current[0], current[1]+1)
        down_block = (current[0]+1, current[1])
        lt_block = (current[0], current[1]-1)
        for blk in (up_block, rt_block, down_block, lt_block):
            if _maze[blk[0]][blk[1]] == 0:
                current = blk
                break
        if _maze[current[0]][current[1]] == -1:  # 不通
            stk.pop()
            current = stk.get_top()
        else:
            _maze[current[0]][current[1]] = -1
            stk.push(current)
    if current == _out:
        return stk.data
    else:
        print("Dead Maze")
        return None


def show_solution(_solution):
    slt_x = list()
    slt_y = list()
    for item in _solution:
        slt_x.append(item[1]+0.5)
        slt_y.append(-item[0]+0.5)
    plt.plot(slt_x, slt_y, 'blue')


maze_size = 20
entrance = (1, 1+round(random()*(maze_size-3)))
out = (maze_size-2, 1+round(random()*(maze_size-3)))
# 坐标起始点
x = [0, 1, 1, 0]
y = [0, 0, 1, 1]
maze = generate_maze(maze_size)
for _item in maze:
    for _num in _item:
        print(_num, end=',')
print('\n')
for i in range(len(maze)):
    for j in range(len(maze[i])):
        if (i, j) == entrance:
            color = "red"
            maze[i][j] = 0
        elif (i, j) == out:
            color = "green"
            maze[i][j] = 0
        elif maze[i][j]:
            color = 'black'
        else:
            color = 'white'
        plt.fill(x, y, facecolor=color, alpha=0.9)
        x = mov_x(x, 1)
    y = mov_x(y, -1)
    x = [0, 1, 1, 0]

solution = solve_maze(maze, entrance, out)
# print(solution.data)
if solution is not None:
    show_solution(solution)
plt.show()



