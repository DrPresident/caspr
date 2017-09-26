#!/usr/bin/python

from picamera import PiCamera
from time import sleep

if __name__ == "__main__":
    cam = PiCamera()

    try:
        print "starting camera..."
        cam.start_preview()
        sleep(5)
        print "stopping camera..."
        cam.stop_preview()
    finally:
        cam.close()
