#!/usr/bin/python

import RPi.GPIO as io
from time import sleep,time

io.setmode(io.BCM)

trig = 23
echo = 24

io.setup(trig,io.OUT)
io.setup(echo,io.IN)

def pulse():
    io.output(trig,1)
    sleep(0.0001)
    io.output(trig,0)

    check_start = time()

    while io.input(echo) == 0:
        pass
    pulse_start = time()

    while io.input(echo) == 1:
        pass
    pulse_end = time()

    dist = 17150 * (pulse_end - pulse_start)
    print "distance: " + str(dist)
    return dist
