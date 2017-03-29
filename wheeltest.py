#!/usr/bin/python

import RPi.GPIO as io
from time import sleep

io.setmode(io.BCM)

io.setup(21,io.OUT)
io.setup(20,io.OUT)
io.setup(19,io.OUT)
io.setup(26,io.OUT)

def rotate_left():
    io.output(21,True)
    io.output(20,False)
    io.output(19,False)
    io.output(26,True)

def rotate_right():
    io.output(21,False)
    io.output(20,True)
    io.output(19,True)
    io.output(26,False)

def rotate(deg):
    if deg > 0:
        rotate_right()
        sleep(1 * (deg / 360.))
    elif deg < 0:
        rotate_left()
        sleep(1 * (abs(deg) / 360.))
    stop()


def back():
	io.output(21,True)
	io.output(20,False)
	io.output(19,True)
	io.output(26,False)

def forward(t=0):
	io.output(21,False)
	io.output(20,True)
	io.output(19,False)
	io.output(26,True)
        if t > 0:
            sleep(t)
            stop()


def stop():
	io.output(21,False)
	io.output(20,False)
	io.output(19,False)
	io.output(26,False)

def demo():
    try:
        print "forward"
        forward()
        sleep(1)
        print "back"
        back()
        sleep(1)
        print "turn around"
        rotate(180)
        print "forward"
        forward()
        sleep(1)
        print "back"
        back()
        sleep(1)
        print "turn back around"
        rotate(-180)
        stop()
    except Error as e:
        print e
        stop()

