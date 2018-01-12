#!/usr/bin/python

from mpu6050 import mpu6050 as mpu

sensor = mpu(0x68)

print 'acc', sensor.get_accel_data()
