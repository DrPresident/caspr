#!./bin/python

from time import sleep
from sys import stdout, argv

class MotionController:
    #pins=(left1,right1,left2,right2...)
    def __init__(self,gpio,wheel_pins):

        self.sec_per_inch = 0.5
        self.wheels = wheel_pins
        self.time_start = -1
        self.go_listeners = list()
        self.stop_listeners = list()
        self.rotate_listeners = list()

        self.gpio = gpio
        for w in self.wheels:
            self.gpio.setup(w,self.gpio.OUT)

        self.stop()

    def rotate_subscribe(self,func):
        self.rotate_listeners.append(func)
    def go_subscribe(self,func):
        self.go_listeners.append(func)
    def stop_subscrib(self,func):
        self.stop_listeners.append(func)

    def turn_right(self):
        stdout.write("turning right...\n")
        self.rotate(-90)

    def turn_left(self):
        stdout.write("turning left...\n")
        self.rotate(90)

    def turn_around(self):
        stdout.write("turning around...\n")
        self.rotate(180)

    def rotate(self, deg=0):
        for f in rotate_listeners:
            f(deg)

        for w in range(0,len(self.wheels),2):
            self.gpio.output(self.left_wheel, (deg > 0))
        for w in range(1,len(self.wheels),2):
            self.gpio.output(w, (deg < 0))

        if abs(deg) > 0:
            sleep(self.sec_per_degree * abs(deg))
            self.stop()

    def go_foot(self,feet):
        self.go_inch(feet * 12)

    def go_inch(self,inches):
        stdout.write("go ")
        if inches > 12: 
            stdout.write(inches / 12 + "'")
        stdout.write(inches % 12 + "\"\n")

        self.go()
        if inches:
            sleep(inches * self.sec_per_inch)
            self.stop()

    def go(self):
        self.time_start = time()
        for f in go_listeners:
            f()
        for x in self.wheels:
            self.gpio.output(w,True)

    def stop(self):
        stdout.write("stopping...\n")
        for f in stop_listeners:
            f()
        for x in self.wheels:
            self.gpio.output(w,False)
        self.distance = (time() - self.time_start) * self.sec_per_inch

#run tests for calibration
if __name__ == "__main__":
    import RPi.GPIO as gpio
    motion = Motion(gpio)
    stdout.write("going forward 1ft, " + motion.sec_per_inch * 12 + "s")
    for r in range(-360, 360, 90):
        stdout.write("rotating " + r + " degrees in " + motion.sec_per_degree + "s")
        motion.rotate(rotation)
        sleep(1)
