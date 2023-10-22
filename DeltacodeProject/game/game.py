import keyboard
from time import sleep
import time
from os import system as cmd
from os import get_terminal_size
from random import randint
import curses
from curses import wrapper


class Playterm:
    def __init__(self, std=curses.window, points=1, speed=0.001, player_xy=None):
        self.std = std
        # self.std.nodelay()
        self.limit_color = (158, 3, 16,)
        self.bg = (0, 0, 0,)
        self.point_color = (255, 255, 255,)
        self.term_size = get_terminal_size()
        self.speed = speed
        self.points = []
        self.map_x = self.term_size.columns
        self.map_y = self.term_size.lines
        for n in range(points):
            point = (randint(2, self.map_x-1), randint(2, self.map_y-1))
            while point in self.points:
                point = (randint(2, self.map_x-1), randint(2, self.map_y-1))
                
            self.points.append(point)
        if player_xy:
            self.player_xy = player_xy
        else:
            self.player_xy = (4, 2)
        self.short_time = []

    def move(self, key):
        x, y = self.player_xy
        match key:
            case "KEY_LEFT":
                x -= 1
            case "KEY_RIGHT":
                x += 1
            case "KEY_UP":
                y -= 1
            case "KEY_DOWN":
                y += 1
            case 'q':
                exit()
            case other:
                return False
        if x not in range(self.map_x) or y not in range(1, self.map_y) or (x, y) == (self.map_x-1, self.map_y-1):
            return False
        self.player_xy = (x, y)
        return True

    def show_map(self):
        x, y = self.player_xy
        self.std.addstr(y, x, "P", curses.A_REVERSE | curses.A_BOLD)
        for point in self.points:
            x, y = point
            self.std.addstr(y, x, "0")


    def show(self, std):
        self.std = std
        self.show_map()
        while True:
            key = std.getkey()
            if self.move(key):
                if self.player_xy in self.points:
                    del self.points[self.points.index(self.player_xy)]
                    if len(self.points) == 0:
                        break
                self.std.clear()
                self.show_map()
                self.std.refresh()
                # sleep(self.speed)


if __name__ == "__main__":
    curses.initscr()
    curses.noecho()

    speed = 0.1
    points = 1
    player_xy = None
    for level in range(1, 10):
        # Playterm(points=int(round(points)), speed=speed).show()
        playterm = Playterm(points=int(round(points)), speed=speed, player_xy=player_xy)
        wrapper(playterm.show)
        player_xy = playterm.player_xy
        speed = speed/7 * 3
        points = points*1.40
        # sleep(2)