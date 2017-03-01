#!/usr/bin/env python

import RPi.GPIO as gpio
from time import sleep
from vision_controller import VisionController
from motion_controller import MotionController

GPIO.setmode(gpio.BCM)

front_vision = VisionController(gpio,0,0)
motion = MotionController(gpio,0,0)

vision_controller.start()

too_close = 10
look_for_turn = 50

while True:

    if front_vision.updated:
        front_dist = front_vision.refresh()

        if front_dist > too_close:
            motion.go()
        
        #turn around if nowhere to go
        if front_dist < look_for_turn:

            if front_dist < too_close:
                motion.stop()

            if right_dist > front_dist or left_dist > front_dist:
                if right_dist > left_dist:
                    motion.turn_right()
                elif right_dist < left_dist:
                    motion.turn_left()

            elif front_dist < too_close:
                motion.turn_around()

stdout.write("All done!\n")
gpio.cleanup()
