#!/usr/bin/env python

from time import time, sleep
from sys import stdout
import threading

class Vision:
    def __init__(self,gpio,trigger,echo):
        self.trigger = trigger
        self.echo    = echo

        self.dist = -1

        self.pulse_timeout  = .001
        self.pulse_interval = .5
        self.no_hit = float("inf")

        self.updated = False

        self.gpio = gpio
        self.gpio.setup(self.front_trigger,self.gpio.OUT)
        self.gpio.setup(self.front_echo,self.gpio.IN)
        self.gpio.setup(self.right_trigger,self.gpio.OUT)
        self.gpio.setup(self.right_trigger,self.gpio.OUT)
        self.gpio.setup(self.left_echo,self.gpio.IN)
        self.gpio.setup(self.left_echo,self.gpio.IN)

        self.gpio.output(self.trigger,False)
        sleep(1)

    def refresh(self):
        updated = False
        return self.dist

    def pulse(self):
        self.gpio.output(trigger, True)
        sleep(0.0001)

        check_start = time()

        while gpio.input(echo) == 0:
            pulse_start = time()
            if pulse_start - check_start > pulse_timeout:
                return -1

        while gpio.input(echo) == 1:
            pulse_end = time()

        return round(17150 * (pulse_end - pulse_start), 2)

    def run(self):
        while True:
            self.dist = self.pulse(self.trigger, self.echo)
            updated = True

            sleep(self.pulse_interval)

    def start(self):
        self.daemon = threading.Thread(target=self.run)
        self.daemon.setDaemon(True)
        self.daemon.start()


#./vision_controller trigger_pin echo_pin
if __name__ == "__main__":
    import RPi.GPIO as gpio
    from sys import argv
    if(len(argv) >= 2):
        
    vis = Vision(gpio, argv[0], argv[1])
    vis.pulse()
    while not vis.updated:
        continue
    dist = vis.refresh()
    stdout.write("distance: " + vis.refresh())

