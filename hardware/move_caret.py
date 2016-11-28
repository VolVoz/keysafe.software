# -*- coding: utf-8 -*-
from hardware.magnet_driver import Magnet
from hardware.motor_driver_a4988 import MotorDRV_a4988
from time import sleep
from hardware.constants import *

mtr1 = MotorDRV_a4988(motor1_step, motor1_dir, motors_enable)
mtr2 = MotorDRV_a4988(motor2_step, motor2_dir, motors_enable)
mgn = Magnet(magnet)


def move_mechanical_system(coordinates, key_way):
    if key_way is 'push':
        sleep(0.1)
        mgn.up()
    for comnd in coordinates.split():
        motor = int(comnd[-1])
        direction = int(comnd[-2])
        steps = int(comnd[:-2])
        if motor is 1:
            mtr1.spin(steps, direction)  # 500 1 1
        if motor is 2:
            mtr2.spin(steps, direction)
    if key_way is 'push':
        sleep(0.1)
        mgn.down()
    if key_way is 'pull':
        sleep(0.1)
        mgn.up()
    for comnd in coordinates.split()[::-1]:
        motor = int(comnd[-1])
        direction = 0 if int(comnd[-2]) == 1 else 1
        steps = int(comnd[:-2])
        if motor is 1:
            mtr1.spin(steps, direction)  # 500 1 1
        if motor is 2:
            mtr2.spin(steps, direction)
    if key_way is 'pull':
        sleep(0.1)
        mgn.down()
