#!/usr/bin/python

import RPi.GPIO as io
from time import sleep

io.setmode(io.BCM)

right_0 = 26 
right_1 = 19 
left_0  = 13
left_1  = 6

io.setup(right_0,io.OUT)
io.setup(right_1,io.OUT)
io.setup(left_0,io.OUT)
io.setup(left_1,io.OUT)

def rotate_left():
    io.output(right_0,True)
    io.output(right_1,False)
    io.output(left_0,False)
    io.output(left_1,True)

def rotate_right():
    io.output(right_0,False)
    io.output(right_1,True)
    io.output(left_0,True)
    io.output(left_1,False)

def rotate(deg):
    if deg > 0:
        rotate_right()
        sleep(1 * (deg / 360.))
    elif deg < 0:
        rotate_left()
        sleep(1 * (abs(deg) / 360.))
    stop()


def back():
	io.output(right_0,True)
	io.output(right_1,False)
	io.output(left_0,True)
	io.output(left_1,False)

def forward(t=0):
	io.output(right_0,False)
	io.output(right_1,True)
	io.output(left_0,False)
	io.output(left_1,True)
        if t > 0:
            sleep(t)
            stop()


def stop():
	io.output(right_0,False)
	io.output(right_1,False)
	io.output(left_0,False)
	io.output(left_1,False)

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

if __name__ == '__main__':
    demo()
