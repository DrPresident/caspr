#!/usr/bin/python

import RPi.GPIO as io
from time import sleep,time
import atexit

io.setmode(io.BCM)

trig = 17
echo = 4
timeout = .3 

io.setup(trig, io.OUT)
io.setup(echo, io.IN)

def avgpulse(p):
    sum = 0.
    for i in xrange(p):
        sum += pulse()

    return sum / p

def pulse():
    io.output(trig,1)
    sleep(0.0001)
    io.output(trig,0)

    check_start = time()
    is_timedout = False
    print 'waiting on echo:0'

    while io.input(echo) == 0 and not is_timedout:
        print time() - check_start
        if time() - check_start >= timeout:
            is_timedout = True

    pulse_start = time()

    print 'waiting on echo:1'
    while io.input(echo) == 1 and not is_timedout: 
        if time() - pulse_start >= timeout:
            is_timedout = True

    pulse_end = time()

    dist = 17150 * (pulse_end - pulse_start)
    print "distance:", dist
    if is_timedout:
        print "Pulse Timeout:", pulse_end - pulse_start
    return dist

pulse()
atexit.register(io.cleanup)
