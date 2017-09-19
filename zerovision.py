#!/usr/bin/python

from gpiozero import DistanceSensor

sensor = DistanceSensor(4, 17)

print 'Distance:', sensor.distance
