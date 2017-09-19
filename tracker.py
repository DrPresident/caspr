#!/usr/bin/python
from pygame import draw,display,FULLSCREEN
from pygame.locals import *
from time import sleep
from math import sin,cos,radians

class Tracker:
    def __init__(self,motion_controller=None,rotation=0,location=(0,0)):
        self.rotation = rotation
        self.location = location
        self.graph = list()

        self.map_width = 640
        self.map_height = 480
        self.map_window = None

        self.compass_width = 120 
        self.compass_height = 120 
        self.compass_radius = 50
        self.compass_center = (self.compass_radius + 5, self.compass_radius + 5)
        self.compass_window = None

        self.moving = False
        self.speed = -1
        self.max_speed = 10
        self.speedometer_radius = 10
        self.speedometer_center = (11,11)

        display.init()

    def rotate(self,deg):
        self.rotation += abs(deg)
    
    def init_window(self):
        if self.window is None:
            self.window = display.set_mode((self.width,self.height))

    def show_path(self):
        self.init_window()
        self.update_path()

    def show_speed(self):
        self.init_window()
        self.update_speed()

    def show_rotation(self):
        self.compass_window = display.set_mode((720,480),FULLSCREEN) 
        self.update_rotation()

    def update_path(self):
        for p in self.graph:
            draw.circle(self.window,(255,0,0),p,1)
        draw.lines(self.window, (0,0,255), False, self.graph)

    def update_speed(self):
        print "update_speed not implemented"

    def update_rotation(self):

        self.compass_window.fill((0,0,0))
        self.rotation = self.rotation % 360
        draw.circle(self.compass_window,(0,255,0),self.compass_center, \
                self.compass_radius, 1) 
        point = (self.compass_radius * cos(radians(self.rotation - 90)) + self.compass_center[0], \
                self.compass_radius * sin(radians(self.rotation - 90)) + self.compass_center[1])
        draw.line(self.compass_window, (0,255,0), self.compass_center, point, 2)

if __name__ == "__main__":
    
    t = Tracker()
    #t.graph = ((100,100),(200,100),(200,200),(100,200))
    #t.show_path()
    t.show_rotation()
    display.flip()
    for r in range(0,361,45):
        t.compass_window.fill((0,0,0))
        t.rotation = r
        t.update_rotation()
        display.flip()
        sleep(1)
