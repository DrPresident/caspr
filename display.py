#!/usr/bin/python

from lib_oled96 import ssd1306
from time import sleep
from PIL import ImageFont, ImageDraw, Image
from smbus import SMBus
import commands
import socket

from sys import argv
from os import path

class Display:
    def __init__(self):
        self.font = ImageFont.load_default()
        self.oled = ssd1306(SMBus(1))
        self.oled.cls()
        self.width = self.oled.width
        self.height = self.oled.height
        self.draw = self.oled.canvas
        self.left_vis = None
        self.right_vis = None
        self.center_vis = None
        self.relative_path = path.dirname(path.abspath(__file__))
        self.logo = Image.open(self.relative_path + '/caspr_logo.pcx')
        self.animation = None
        self.animation_fps = 100

    def __del__(self):
        if self.animation is not None:
            for frame in self.animation:
                frame.close()

    def show_heading(self):
        ip = commands.getoutput('hostname -I').split(' ')[0]
        display.draw.text((0,0), 'CASPR ' + ip, font=self.font, fill=1)
        self.oled.display()

    def refresh(self):
        self.oled.cls()
        self.oled.display()

    def intro_anim(self):
        if self.animation is None:
            self.animation = list()
            i = 0
            # open all caspr frames starting at 0
            try:
                while True:
                    self.animation.append(Image.open(self.relative_path + '/caspr' + str(i) + '.pcx'))
                    i += 1
            except IOError:
                pass

        # self.oled.cls()
        if self.animation:
            for frame in self.animation:
                self.draw.bitmap((0,16), frame, fill=1)
                self.oled.display()
                sleep(60 / self.animation_fps) 
        else:
            self.off()

    def show_logo(self):
        self.draw.bitmap((0,16), self.logo, fill=1)
        self.oled.display()

    def clear(self):
        self.oled.cls()

    def off(self):
        self.oled.onoff(0)

    def on(self):
        self.oled.onoff(1)

    def center_vision(self, vis):
        self.center_vis = vis

        def pulse_callback(v):
            pass

        vis.on_pulse.append(pulse_callback)

        def update_callback(v):
            s = str(round(v.dist, 1))
            if v.dist < 0:
                s = "TO"
            self.draw.rectangle((self.width / 2 - 25, 0, self.width / 2 + 25, 10), fill=0)
            self.draw.text((self.width / 2 - len(s) * 3, 0), s, font=self.font, fill=1)
            self.oled.display()

        vis.on_update.append(update_callback)

    def right_vision(self, vis):
        self.right_vis = vis
        s = str(round(v.dist, 1))
        vis.on_update.append(lambda v: self.draw.text((self.oled.width - len(s) , 0), s))

    def left_vision(self, vis):
        self.left_vis = vis
        vis.on_update.append(lambda v: self.draw.text((0,self.oled.height / 2), str(round(v.dist))))

if __name__ == '__main__':
    display = Display()
    display.intro_anim()
