#!/usr/bin/env python

from time import time, sleep
from sys import stdout
import threading

class Vision:
    def __init__(self,gpio,trigger,echo):
        self.trigger = trigger
        self.echo    = echo

        self.dist = -1

        self.pulse_timeout  = .1 
        self.pulse_interval = .5
        self.no_hit = float("inf")

        self.updated = False

        self.gpio = gpio
        self.gpio.setup(self.trigger,self.gpio.OUT)
        self.gpio.setup(self.echo,self.gpio.IN)

        self.gpio.output(self.trigger,False)

        self.on_pulse = list()
        self.on_update = list()

    def refresh(self):
        updated = False
        return self.dist

    def pulse(self):
        for f in self.on_pulse:
            f(self)

        self.gpio.output(self.trigger, True)
        sleep(0.0001)
        self.gpio.output(self.trigger, False)
        pulse_start = -1
        pulse_end = -1
        timeout = False

        check_start = time()

        while self.gpio.input(self.echo) == 0 and not timeout:
            pulse_start = time()
            if pulse_start - check_start > self.pulse_timeout:
                timeout = True

        while self.gpio.input(self.echo) == 1 and not timeout:
            pulse_end = time()
            if pulse_end - pulse_start > self.pulse_timeout:
                timeout = True

        if timeout:
            self.dist = -1
        else:
            self.dist = 17150 * (pulse_end - pulse_start)
        updated = True
        for f in self.on_update:
            f(self)

        return self.dist

    def run(self):
        while True:
            self.dist = self.pulse()
            sleep(self.pulse_interval)

    def start(self):
        self.daemon = threading.Thread(target=self.run)
        self.daemon.setDaemon(True)
        self.daemon.start()


if __name__ == "__main__":
    import RPi.GPIO as gpio

    gpio.setmode(gpio.BCM)
    left = Vision(gpio, 22, 27)
    center = Vision(gpio, 17, 4)
    right = Vision(gpio, 9, 10)

    while True:
        print round(left.pulse(), 2), round(center.pulse(), 2), round(right.pulse(), 2)
        sleep(1)

