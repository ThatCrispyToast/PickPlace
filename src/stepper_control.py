from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

class StepperControl:
    def __init__(self):
        self.kit = MotorKit()
        self.kit2 = MotorKit(address=0x61)

    def release(self):
        self.kit.stepper1.release()
        self.kit.stepper2.release()
        self.kit2.stepper1.release()
        self.kit2.stepper2.release()

    def move_x(self, steps):
        for _ in range(steps):
            self.kit.stepper1.onestep(style=stepper.DOUBLE)
        self.release()