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

    UP = Adafruit_MotorHAT.FORWARD
    DOWN = Adafruit_MotorHAT.BACKWARD

    SINGLE = Adafruit_MotorHAT.SINGLE
    DOUBLE = Adafruit_MotorHAT.DOUBLE
    INTERLEAVE = Adafruit_MotorHAT.INTERLEAVE
    MICROSTEP = Adafruit_MotorHAT.MICROSTEP

    x_steps = 0
    y_steps = 0

    def __init__(self, rpm=3000):
        # create a default object, no changes to I2C address or frequency
        self.mh = Adafruit_MotorHAT()

        # recommended for auto-disabling motors on shutdown!
        def turnOffMotors():
            self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
            self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
            self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
            self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)
        atexit.register(turnOffMotors)

        self.x_stepper = self.mh.getStepper(200, 1)  # 200 steps/rev, motor port #1
        self.x_stepper.setSpeed(rpm)             # Attempts 3000 RPM

        self.y_stepper = self.mh.getStepper(200, 2)  # 200 steps/rev, motor port #2
        self.y_stepper.setSpeed(rpm)             # Attempts 3000 RPM

        self.z1_stepper = self.mh.getStepper(200, 3)  # 200 steps/rev, motor port #2
        self.z1_stepper.setSpeed(rpm)             # Attempts 3000 RPM

        self.z2_stepper = self.mh.getStepper(200, 4)  # 200 steps/rev, motor port #2
        self.z2_stepper.setSpeed(rpm)             # Attempts 3000 RPM
        
        self.xbusy = False
        self.ybusy = False
        self.z1busy = False
        self.z2busy = False

        # self.x_steps = 0
        # self.y_steps = 0

    def __x_control(self, x_stepper, steps, direction, step_type):
        if self.xbusy:
            return False
        self.xbusy = True
        x_stepper.step(steps, direction,  step_type)
        self.x_steps += steps
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.xbusy = False
        return True

    def __y_control(self, y_stepper, steps, direction, step_type):
        if self.ybusy:
            return False
        self.ybusy = True
        y_stepper.step(steps, direction,  step_type)
        self.y_steps += steps
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.ybusy = False
        return True

    def move_x(self, steps, direction, step_type, block=True):
        if self.xbusy:
            return False
        st1 = multiprocessing.Process(target=self.__x_control, args=(self.x_stepper, int(steps), direction, step_type,))
        st1.start()
        if block:
            st1.join()
        return True

    def move_y(self, steps, direction, step_type, block=True):
        if self.ybusy:
            return False
        st2 = multiprocessing.Process(target=self.__y_control, args=(self.y_stepper, int(steps), direction, step_type,))
        st2.start()
        if block:
            st2.join()
        return True

    def get_position(self):
        return self.x_steps, self.y_steps

    def is_busy(self):
        return not self.xbusy and not self.ybusy

    def move_xy(self, xsteps, xdirection, xstep_type, ysteps, ydirection, ystep_type, block=True):
        # if self.is_busy():
        #     return "asd"
        if block:
            if xsteps < ysteps:
                self.move_x(xsteps, xdirection, xstep_type, block=False)
                self.move_y(ysteps, ydirection, ystep_type, block=True)
            else:
                self.move_y(ysteps, ydirection, ystep_type, block=False)
                self.move_x(xsteps, xdirection, xstep_type, block=True)
        else:
            self.move_x(xsteps, xdirection, xstep_type, block=False)
            self.move_y(ysteps, ydirection, ystep_type, block=False)
        return True

    def goto(self, x, y):
        posx, posy = self.get_position()

