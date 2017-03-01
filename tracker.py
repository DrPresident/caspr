#!./bin/python
from pygame import draw,display
from pygame.locals import *
from time import sleep
from math import sin,cos

class Tracker:
    def __init__(self,motion_controller=None,rotation=0,location=(0,0)):
        self.rotation = rotation
        self.location = location
        self.graph = list()

        self.width = 640
        self.height = 480
        self.window = None

        self.moving = False
        self.speed = -1
        self.max_speed = 10
        self.speedometer_radius = 10
        self.speedometer_center = (11,11)

        self.compass_radius = 50
        self.compass_center = (self.width - self.compass_radius - 10, \
                self.compass_radius + 10)

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
        self.init_window()
        self.update_rotation()

    def update_path(self):
        for p in self.graph:
            draw.circle(self.window,(255,0,0),p,1)
        draw.lines(self.window, (0,0,255), False, self.graph)
        display.flip()

    def update_speed(self):
        display.flip()

    def update_rotation(self):
        self.rotation = self.rotation % 360
        draw.circle(self.window,(0,255,0),self.compass_center, \
                self.compass_radius, 1) 
        point = (self.compass_radius * cos(self.rotation) + self.compass_center[0], \
                self.compass_radius * sin(self.rotation) + self.compass_center[1])
        draw.line(self.window, (0,255,0), self.compass_center, point, 2)
        display.flip()

if __name__ == "__main__":
    
    t = Tracker()
    t.graph = ((100,100),(200,100),(200,200),(100,200))
    t.show_path()
    t.rotation = 180
    t.show_rotation()
        
