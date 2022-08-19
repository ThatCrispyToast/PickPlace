#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from traceback import print_tb
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

def x_control(myStepper):
    myStepper.step(X_STEPS/4, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
    print("X Done")

def y_control(myStepper2):
    myStepper2.step(Y_STEPS/4, Adafruit_MotorHAT.FORWARD,  Adafruit_MotorHAT.SINGLE)
    print("Y Done")

def main():
    myStepper = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
    myStepper.setSpeed(3000)             # 30 RPM
    myStepper2 = mh.getStepper(200, 2)  # 200 steps/rev, motor port #1
    myStepper2.setSpeed(3000)             # 30 RPM

    # create empty threads (these will hold the stepper 1 and 2 threads)
    st1 = multiprocessing.Process(target=x_control, args=(myStepper,))
    st2 = multiprocessing.Process(target=y_control, args=(myStepper2,))

    start = time.time()
    st1.start()
    st2.start()

    # st1.join()
    # st2.join()
    print("Hello, World!")
    time.sleep(50)
    print(time.time() - start)

    print("Hello")


if __name__ == "__main__":
    main()