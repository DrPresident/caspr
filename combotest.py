#!/usr/bin/python

from wheeltest import *
from visiontest import *

def avgpulse():
    data = (pulse(),pulse(),pulse())
    dist = reduce(lambda x, y: x + y, data) / len(data)
    print "avg: " + str(dist)
    return dist

d = avgpulse()
print "going"
forward()
print "d " + str(d)
while d > 20: 
    d = avgpulse()
print "avoiding"
rotate_right()
while d < 30:
    d = avgpulse()
print "stop"
stop()
