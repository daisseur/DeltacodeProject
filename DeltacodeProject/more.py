import os
import sys

import keyboard
from time import sleep
import time
from os import system as cmd
from os import get_terminal_size
from random import randint
import signal

nocolor = "\033[0;0m"
colors = {
    'black': '0;',
    'red': '1;',
    'green': '2;',
    'yellow': '3;',
    'blue': '4;',
    'violet': '5;',
    'cyan': '6;',
    'grey': '7;',
    'white': '9;'}
effects = {
    'bold': '1m',
    'classic': '2m',
    'italic': '3m',
    'underline': '4m',
    'strike': '9m'}
highlights = {
    'False': '\033[3',
    'True': '\033[4'}

def print_color(*args, color='white', effect='classic', highlight='False', end=False) -> None:
    if end:
        print(highlights[highlight] + colors[color] + effects[effect] + ' '.join(str(arg) for arg in args) + nocolor, end='')
    else:
        print(highlights[highlight] + colors[color] + effects[effect] + ' '.join(str(arg) for arg in args) + nocolor)

class playterm:
    def __init__(self, points=1, speed=0.001):
        self.term_size = get_terminal_size()
        self.speed = speed
        self.map = [[*(self.term_size.columns-2)*'█'] for i in range(self.term_size.lines-5)]

        # set outlines
        self.map.insert(0, [i for i in len(self.map[0]) * "-"])
        self.map.extend([(len(self.map[0]) * " -").split()])
        self.points = []
        for n in range(points):
            point = [randint(2, len(self.map)-2), randint(2, len(self.map[1])-1)]
            while point in self.points:
                point = [randint(2, len(self.map)-1), randint(2, len(self.map[1])-1)]
            self.points.append(point)
            self.map[point[0]][point[1]] = "$"
        for line in self.map:
            line.insert(0, "|")
            line.extend(["|"])
        self.map[2][1] = "P"
        self.location = [2, 1]
        self.short_time = []

    def up(self, location=[2, 1]):
        if location[0] != 1:
            self.map[location[0]][location[1]] = ' '
            location[0] -= 1
            self.map[location[0]][location[1]] = 'P'
            return location
        else:
            print("UP ERROR")
            return location

    def down(self, location=[2, 1]):
        if location[0] != len(self.map) -2:
            self.map[location[0]][location[1]] = ' '
            location[0] += 1
            self.map[location[0]][location[1]] = 'P'
            return location
        else:
            print("DOWN ERROR")
            return location

    def right(self, location=[2, 1]):
        if location[1] != len(self.map[location[0]]) -2:
            self.map[location[0]][location[1]] = ' '
            location[1] += 1
            self.map[location[0]][location[1]] = 'P'
            return location
        else:
            print("RIGHT ERROR")
            return location

    def left(self, location=[2, 1]):
        if location[1] != 1:
            self.map[location[0]][location[1]] = ' '
            location[1] -= 1
            self.map[location[0]][location[1]] = 'P'
            return location
        else:
            print("LEFT ERROR")
            return location

    def show_map(self, map):
        s = time.perf_counter()
        for line in map:
            if "P" in line:
                for char in line:
                    if char == "P":
                        print(f"\033[0;0m\033[34;1mP", end='')
                    else:
                        print(f"\033[34;1m{char}", end='')
                print("\033[0;0m")
            else:
                print(f"\033[34;1m{''.join(line)}\033[0;0m")
        # self.short_time.append(time.perf_counter() - s)
        # print(min(self.short_time))


    def show(self):
        self.show_map(self.map)
        while True:
            if keyboard.is_pressed("z"):
                location = self.up(self.location)
            elif keyboard.is_pressed("s"):
                location = self.down(self.location)
            elif keyboard.is_pressed("d"):
                location = self.right(self.location)
            elif keyboard.is_pressed("q"):
                location = self.left(self.location)
            else:
                continue
            cmd("cls")
            print("press z, s, d or q\n")
            print(location)
            self.show_map(self.map)
            sleep(self.speed)
            if location in self.points:
                del self.points[self.points.index(location)]
                if len(self.points) == 0:
                    break

if __name__ == "__main__":
    if "start" in sys.argv:
        speed = float(sys.argv[-1])
        blevel = int(sys.argv[-2])
        points = blevel * 1.4
    else:
        speed = 0.1
        points = 1
        blevel = 1
    for level in range(blevel, 10):
        playterm(points=int(round(points)), speed=speed).show()
        speed = speed/7 * 3
        print(speed)
        points = level*1.40
        print(points)
        sleep(2)