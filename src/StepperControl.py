#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit
import multiprocessing

X_STEPS = 1490
Y_STEPS = 1580

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
atexit.register(turnOffMotors)

def x_control(myStepper, steps, direction):
    myStepper.step(steps, direction,  Adafruit_MotorHAT.SINGLE)
    print("X Done")

def y_control(myStepper2, steps, direction):
    myStepper2.step(steps, direction,  Adafruit_MotorHAT.SINGLE)
    print("Y Done")

myStepper = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
myStepper.setSpeed(3000)             # 30 RPM
myStepper2 = mh.getStepper(200, 2)  # 200 steps/rev, motor port #1
myStepper2.setSpeed(3000)             # 30 RPM

def move_x(steps, direction):
    print(steps, direction)
    st1 = multiprocessing.Process(target=x_control, args=(myStepper, steps, direction,))

    st1.start()
    st1.join()

def move_y(steps, direction):
    st2 = multiprocessing.Process(target=y_control, args=(myStepper2, steps, direction,))

    st2.start()
    st2.join()

move_x(200, Adafruit_MotorHAT.FORWARD)