#!/usr/bin/python

from time import sleep, time
from sys import stdout, stdin, argv

class Servo:
    def __init__(self, gpio, pin):
        self.pin = pin
        self.gpio = gpio

        self.gpio.setup(pin, self.gpio.OUT)
        # 20 ms
        self.period = 2000
        self.pwm = gpio.PWM(self.pin, 100)

        self.rot = 0
        self.pwm.start(self.rot)
        self.duty = 0
        self.set_rotation(90)

    def __del__(self):
        self.pwm.stop()

    def set_rotation(self, rotation):
        self.rot = min(max(rotation, 0.0), 180.0)
        print 'Rotation:', self.rot
        # normalize 180 degrees to a 0-20ms duty cycle
        duty = self.rot / 180.0 * 20.0 + 1
        print 'Duty:', duty

        # rotate asynchronously
        self._set_duty(duty)
        sleep(.1 * abs(self.duty - duty) / 2)
        self.duty = duty
        self._idle()
        # Thread(target=rotate).start()
    
    def _set_duty(self, duty):
        self.pwm.ChangeDutyCycle(duty)

    def _idle(self):
        self._set_duty(0)

    def rotate_up(self):
        self.set_rotation(self.rot + 15)

    def rotate_down(self):
        self.set_rotation(self.rot - 15)
    

if __name__ == '__main__':
    import RPi.GPIO as gpio

    gpio.setmode(gpio.BCM)
    servo = Servo(gpio, 18)

    servo.set_rotation(0)

    for pulse in xrange(0, 12):
        servo.rotate_up()

    servo.set_rotation(90)

    gpio.cleanup()
