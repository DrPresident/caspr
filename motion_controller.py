#!/usr/bin/python

from time import sleep, time
from sys import stdout, stdin, argv
from getch import getch

class Motion:
    # left and right are wheel pin numbers
    # (pin0, pin1)
    def __init__(self,gpio, left, right):

        self.sec_per_inch = 0.5
        self.sec_per_degree = 0.1
        self.left = left
        self.right = right
        self.time_start = -1

        self.gpio = gpio
        for w in left + right:
            self.gpio.setup(w,self.gpio.OUT)

        self.stop()


    def rotate_right(self):
        self.stopped = False
        self.gpio.output(self.left[0], False)
        self.gpio.output(self.left[1], True)
        self.gpio.output(self.right[0], True)
        self.gpio.output(self.right[1], False)

    def rotate_left(self):
        self.stopped = False
        self.gpio.output(self.left[0], True)
        self.gpio.output(self.left[1], False)
        self.gpio.output(self.right[0], False)
        self.gpio.output(self.right[1], True)

    def rotate(self, deg=0):
        print "turning", "right" if deg > 0 else "left"

        self.stopped = False
        for w in self.left:
            self.gpio.output(w, (deg > 0))
        for w in self.right:
            self.gpio.output(w, (deg <= 0))

        if abs(deg) > 0:
            sleep(self.sec_per_degree * abs(deg))
            self.stop()

    def forward(self):
        self.time_start = time()
        self.stopped = False
        self.gpio.output(self.left[0], False)
        self.gpio.output(self.left[1], True)
        self.gpio.output(self.right[0], False)
        self.gpio.output(self.right[1], True)

    def back(self):
        self.time_start = time()

        self.stopped = False
        self.gpio.output(self.left[0], True)
        self.gpio.output(self.left[1], False)
        self.gpio.output(self.right[0], True)
        self.gpio.output(self.right[1], False)

    def stop(self):
        self.gpio.output(self.left[0], False)
        self.gpio.output(self.left[1], False)
        self.gpio.output(self.right[0], False)
        self.gpio.output(self.right[1], False)
        self.stopped = True

        self.distance = (time() - self.time_start) * self.sec_per_inch


if __name__ == "__main__":
    import RPi.GPIO as gpio

    gpio.setmode(gpio.BCM)
    motion = Motion(gpio, (13, 6), (26, 19))
    
    motion.forward()
    sleep(3)
    motion.back()
    sleep(3)
    motion.stop()


