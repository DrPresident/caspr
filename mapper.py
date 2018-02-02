#!/usr/bin/python
import curses
import sys
from time import sleep

#log = open('log', 'w')

unknown = 0
empty = 1
block = 2

class Mapper:
    def __init__(self):
        self.screen = curses.initscr()
        curses.cbreak()
        curses.noecho()

        # cell types
        self.unknown = 0
        self.empty = 1
        self.block = 2
        # cell characters
        self.colors = ('?', ' ', 'X')

        if curses.has_colors() and curses.can_change_color():
            #log.write('Colors Initialized!')
            curses.init_color(0,0,300,500)
            # color codes
            self.colors = (2, 8, 9)

        # cm
        self.map_size = 1000
        self.car_len = 5
        self.car_width = 7

        self.area_map = list()
        for x in xrange(self.map_size):
            self.area_map.append(list())
            for y in xrange(self.map_size):
                self.area_map[x].append(self.colors[unknown])

        self.screen_size = self.screen.getmaxyx()
        self.screen_size = (self.screen_size[0] - 2, self.screen_size[1] - 2)

        self.map_center = (self.map_size / 2, self.map_size / 2)
        self.start_location = self.map_center
        self.location = self.start_location

        # test objects
        """
        self.make_box((self.map_center[0] + 10, self.map_center[1] + 10), 5, 5)
        self.make_box((self.map_center[0] - 20, map_center[1] - 20), 10, 20)
        """
        # draw car
        self.make_box((self.map_center[0] - self.car_len / 2,\
            self.map_center[1] - self.car_width / 2),\
            self.car_len, self.car_width, 'B')

    def __del__(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def draw(self):
        # draw map
        dx = 0
        #log.write('screen_size1 / -2' + str(screen_size[1] / -2) + '\n')
        for x in xrange(self.screen_size[1] / -2, self.screen_size[1] / 2):
            dy = 0
            for y in xrange(self.screen_size[0] / -2, self.screen_size[0] / 2):
                dy += 1
                self.screen.addch(dy, dx, self.area_map[ self.location[0] + x ][ self.location[1] + y ])
            dx += 1

        self.screen.refresh()


    def make_pt(self, loc, color='?'):
        self.area_map[loc[0]][loc[1]] = color

    def make_pt_rel_car_center(self, loc, color='?'):
        self.area_map[self.location[0] + loc[0]][self.location[1] + loc[1]] = color

    def make_pt_rel_car(self, loc, color='?'):
        self.area_map[self.location[0] + loc[0]][self.location[1] + loc[1]] = color

    def make_box_rel_center(self, loc, h=1, w=1, color='?'):
        self.make_box((self.map_center[0] + loc[0], self.map_center[1] + loc[1]), h, w, color)

    def make_box_rel_car(self, loc, h=1, w=1, color='?'):
        self.make_box((self.location[0] + loc[0], self.location[1] + loc[1]), h, w, color)

    def make_box(self, loc, h=1, w=1, color='?'):
        # setup test objects
        for x in xrange(w):
            for y in xrange(h):
                self.area_map[loc[0] + x][loc[1] + y] = color

if __name__ == "__main__":
    mapper = Mapper(curses.initscr())

    mapper.make_box((map_center[0] + 10, map_center[1] + 10), 5, 5, mapper.colors[mapper.block])
    mapper.make_box((map_center[0] - 20, map_center[1] - 20), 10, 20, mapper.colors[mapper.block])

    mapper.draw()
    sleep(10)
