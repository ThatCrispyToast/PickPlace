#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT

import atexit
import multiprocessing

class StepperControl:

    X_LENGTH = 1490
    Y_LENGTH = 1580

    LEFT = Adafruit_MotorHAT.FORWARD
    RIGHT = Adafruit_MotorHAT.BACKWARD

    FORWARD = Adafruit_MotorHAT.FORWARD
    BACKWARD = Adafruit_MotorHAT.BACKWARD

    SINGLE = Adafruit_MotorHAT.SINGLE
    DOUBLE = Adafruit_MotorHAT.DOUBLE
    INTERLEAVE = Adafruit_MotorHAT.INTERLEAVE
    MICROSTEP = Adafruit_MotorHAT.MICROSTEP

    def __init__(self, rpm=3000):
        # create a default object, no changes to I2C address or frequency
        mh = Adafruit_MotorHAT()

        # recommended for auto-disabling motors on shutdown!
        def turnOffMotors():
            mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
            mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
            mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
            mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
        atexit.register(turnOffMotors)

        self.x_stepper = mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
        self.x_stepper.setSpeed(rpm)             # Attempts 3000 RPM

        self.y_stepper = mh.getStepper(200, 2)  # 200 steps/rev, motor port #2
        self.y_stepper.setSpeed(rpm)             # Attempts 3000 RPM
        
        self.xbusy = False
        self.ybusy = False

    def __x_control(self, x_stepper, steps, direction, step_type):
        if self.xbusy:
            return False
        self.xbusy = True
        x_stepper.step(steps, direction,  step_type)
        self.xbusy = False
        return True

    def __y_control(self, y_stepper, steps, direction, step_type):
        self.ybusy = True
        y_stepper.step(steps, direction,  step_type)
        self.ybusy = False

    def move_x(self, steps, direction, step_type):
        if self.xbusy:
            return False
        st1 = multiprocessing.Process(target=self.__x_control, args=(self.x_stepper, steps, direction, step_type,))
        st1.start()
        return True

    def move_y(self, steps, direction, step_type):
        if self.ybusy:
            return False
        st2 = multiprocessing.Process(target=self.__y_control, args=(self.y_stepper, steps, direction, step_type,))
        st2.start()
        return True

    def get_position(self):
        return self.x_stepper.currentstep, self.y_stepper.currentstep

    def is_busy(self):
        return not self.xbusy and not self.ybusy