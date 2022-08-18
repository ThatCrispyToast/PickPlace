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

def main():
    atexit.register(turnOffMotors)

    myStepper = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
    myStepper.setSpeed(3000)             # 30 RPM

    start = time.time()
    myStepper.step(1494, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
    print(time.time() - start)

    # c = 0
    # while True:
    #     myStepper.step(50, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
    #     c += 1
    #     print(c, " 1/4 Rotations")

if __name__ == "__main__":
    main()