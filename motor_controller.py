#!/usr/bin/python

from time import sleep, time
from sys import stdout, stdin, argv
from getch import getch

class Motor:
    # left and right are wheel pin numbers
    # (pin0, pin1)
    def __init__(self, gpio, left, speed=50):

        self.sec_per_inch = 0.5
        self.sec_per_degree = 0.1
        self.left = left
        self.time_start = -1
        self.speed = abs(min(speed, 100))
        self.motion = None

        self.gpio = gpio
        for w in left: 
            self.gpio.setup(w,self.gpio.OUT)

        self.fpwm = gpio.PWM(left[1], 100)
        self.fpwm.start(0)
        self.rpwm = gpio.PWM(left[0], 100)
        self.rpwm.start(0)

        self.stop()

    def set_speed(self, speed):
        self.speed = speed
        if self.motion:
            if self.motion == 'f':
                self.fpwm.ChangeDutyCycle(self.speed)
                self.rpwm.ChangeDutyCycle(0)
                
            elif self.motion == 'r':
                self.rpwm.ChangeDutyCycle(self.speed)
                self.fpwm.ChangeDutyCycle(0)


    def forward(self):
        self.motion = 'f'
        self.time_start = time()
        self.stopped = False
        #self.gpio.output(self.left[0], False)
        #self.gpio.output(self.left[1], True)
        self.fpwm.ChangeDutyCycle(self.speed)
        self.rpwm.ChangeDutyCycle(0)

    def reverse(self):
        self.motion = 'r'
        self.time_start = time()
        self.stopped = False
        #self.gpio.output(self.left[0], True)
        #self.gpio.output(self.left[1], False)
        self.fpwm.ChangeDutyCycle(0)
        self.rpwm.ChangeDutyCycle(self.speed)

    def stop(self):
        self.motion = None
        self.stopped = True
        self.distance = (time() - self.time_start) * self.sec_per_inch
        self.fpwm.ChangeDutyCycle(0)
        self.rpwm.ChangeDutyCycle(0)


if __name__ == "__main__":
    import RPi.GPIO as gpio

    gpio.setmode(gpio.BCM)
    left_motor = Motor(gpio, (13, 6), 0)
    right_motor = Motor(gpio, (26, 19), 0)
    left_motor.forward()
    right_motor.forward()

    for s in xrange(10, 100, 10):
        left_motor.set_speed(s)
        right_motor.set_speed(s)
        print "speed:",s 
        sleep(1)
    for s in xrange(100, 10, -10):
        left_motor.set_speed(s)
        right_motor.set_speed(s)
        print "speed:",s 
        sleep(1)

    gpio.cleanup()

