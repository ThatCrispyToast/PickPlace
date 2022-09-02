# from StepperControl import StepperControl
# import time

# steppers = StepperControl()

# # start = time.time()
# # steppers.move_y(523, StepperControl.FORWARD, StepperControl.SINGLE, block=False)
# # steppers.move_x(StepperControl.X_LENGTH/2, StepperControl.LEFT, StepperControl.SINGLE, block=True)
# # print(time.time() - start)

# print(steppers.move_xy(StepperControl.X_LENGTH/2, StepperControl.LEFT, StepperControl.SINGLE,
#                         523, StepperControl.FORWARD, StepperControl.SINGLE))


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

myStepper = mh.getStepper(200, 3)  # 200 steps/rev, motor port #1
myStepper.setSpeed(30)             # 30 RPM

while (True):
    print("Single coil steps")
    start = time.time()
    myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
    myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
    print(time.time() - start)

    start = time.time()
    print("Double coil steps")
    myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.DOUBLE)
    myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
    print(time.time() - start)

    start = time.time()
    print("Interleaved coil steps")
    myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.INTERLEAVE)
    myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)
    print(time.time() - start)
    
    start = time.time()
    print("Microsteps")
    myStepper.step(100, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.MICROSTEP)
    myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.MICROSTEP)
    print(time.time() - start)
