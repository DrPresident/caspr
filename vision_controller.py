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
        sleep(1)

    def refresh(self):
        updated = False
        return self.dist

    def pulse(self):
        self.gpio.output(self.trigger, True)
        sleep(0.0001)
        self.gpio.output(self.trigger, False)

        check_start = time()

        while gpio.input(self.echo) == 0:
            pulse_start = time()
            if pulse_start - check_start > self.pulse_timeout:
                return -1

        while gpio.input(self.echo) == 1:
            pulse_end = time()
            if pulse_end - pulse_start > self.pulse_timeout:
                return -1

        return 17150 * (pulse_end - pulse_start)

    def run(self):
        while True:
            self.dist = self.pulse(self.trigger, self.echo)
            updated = True

            sleep(self.pulse_interval)

    def start(self):
        self.daemon = threading.Thread(target=self.run)
        self.daemon.setDaemon(True)
        self.daemon.start()


if __name__ == "__main__":
    import RPi.GPIO as gpio

    gpio.setmode(gpio.BCM)
    vis = Vision(gpio, 17, 4)

    while True:
        print round(vis.pulse(), 2)
        sleep(1)

