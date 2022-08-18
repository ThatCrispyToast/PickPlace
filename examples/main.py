#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

# myStepper = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
# myStepper.setSpeed(3000)             # 30 RPM

# start = time.time()
# myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
# myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
# print(time.time()-start)

myStepper = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
myStepper2 = mh.getStepper(200, 2)  # 200 steps/rev, motor port #1
myStepper.setSpeed(3000)             # 30 RPM
myStepper2.setSpeed(3000)

start = time.time()
for i in range(100):
    myStepper.step(Adafruit_MotorHAT.FORWARD)
    myStepper2.step(Adafruit_MotorHAT.FORWARD)
print(time.time()-start)