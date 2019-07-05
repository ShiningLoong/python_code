# coding: GBK
# try to solve maze problem with queue
from matplotlib import pyplot as plt
# import numpy as np
from random import random


class MazeQueue:
    def __init__(self):
        self.step_queue = list()

    def en_queue(self, e):
        self.step_queue.append(e)

    def de_queue(self):
        if self.step_queue:
            return self.step_queue.pop(0)
        else:
            return None

    def is_empty(self):
        if self.step_queue:
            return False
        else:
            return True

    def get_head(self):
        if not self.is_empty():
            return self.step_queue[0]
        else:
            return None

    def get_tail(self):
        if not self.is_empty():
            return self.step_queue[-1]
        else:
            return None


def generate_maze(n):
    _maze = list()
    for num in range(n-2):
        _maze.append([0 if random() >= 0.35 else 1 for _num in range(n-2)])
    # build the wall
    for num in range(n-2):
        _maze[num] = [1] + _maze[num] + [1]
    _maze = [[1]*n] + _maze + [[1]*n]
    return _maze


def mov_x(_x, step):  # 画图时的移动方式
    for num in range(len(_x)):
        _x[num] += step
    return _x


def solve_maze(_maze, _entrance, _out):  # 这个解法跟队列没什么关系,用的是树形结构
    maze_queue = MazeQueue()
    step_list = [(*_entrance, -1)]  # 标识上一个block 的位置，-1表示没有上一个
    maze_queue.en_queue(step_list)
    _maze[_entrance[0]][_entrance[1]] = -1
    find = False
    while step_list and step_list[-1][:-1] != _out:
        tmp_list = []   # 清空step_list
        _index = 0
        while _index < len(step_list) and find is False:
            crt = step_list[_index][:-1]
            up_blk = (crt[0]-1, crt[1])
            down_blk = (crt[0]+1, crt[1])
            rt_blk = (crt[0], crt[1]+1)
            lt_blk = (crt[0], crt[1]-1)
            for _blk in (up_blk, down_blk, rt_blk, lt_blk):  # 扫描上下左右
                if _blk == _out:
                    tmp_list.append((*_blk, _index))
                    find = True
                    break
                elif _maze[_blk[0]][_blk[1]] == 0:
                    tmp_list.append((*_blk, _index))  # 添加一个可走的block
                    _maze[_blk[0]][_blk[1]] = -1  # 标记为已走
            _index += 1
        step_list = tmp_list
        maze_queue.en_queue(step_list)
    if not step_list:
        print("Dead Maze")
        return None
    else:
        _solution = list()
        _solution.append(maze_queue.get_tail()[-1][:-1])
        pre_blk = maze_queue.get_tail()[-1][-1]
        maze_queue.step_queue.pop(-1)
        while pre_blk != -1:
            _solution.append(maze_queue.get_tail()[pre_blk][:-1])
            pre_blk = maze_queue.get_tail()[pre_blk][-1]
            maze_queue.step_queue.pop(-1)
        return _solution


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
# for _item in maze:
#     for _num in _item:
#         print(_num, end=',')
# print('\n')
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
print(solution)
if solution is not None:
    show_solution(solution)
plt.show()

