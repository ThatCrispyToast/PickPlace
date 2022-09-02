from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

class StepperControl:

    UP = stepper.BACKWARD
    DOWN = stepper.FORWARD
    RIGHT = stepper.BACKWARD
    LEFT = stepper.FORWARD
    BACKWARD = stepper.BACKWARD
    FORWARD = stepper.FORWARD

    def __init__(self):
        self.kit = MotorKit()
        self.kit2 = MotorKit(address=0x61)

    def release(self):
        self.kit.stepper1.release()
        self.kit.stepper2.release()
        self.kit2.stepper1.release()
        self.kit2.stepper2.release()

    def move_x(self, steps, direction=LEFT):
        try:
            for _ in range(steps):
                self.kit.stepper1.onestep(direction=direction, style=stepper.DOUBLE)
        except KeyboardInterrupt as e:
            self.release()
            raise KeyboardInterrupt from e
        self.release()
    
    def move_y(self, steps, direction=FORWARD):
        for _ in range(steps):
            self.kit.stepper2.onestep(direction=direction, style=stepper.DOUBLE)
        self.release()

    def move_z(self, steps, direction=UP):
        for _ in range(steps):
            self.kit2.stepper1.onestep(direction=direction, style=stepper.DOUBLE)
            self.kit2.stepper2.onestep(direction=direction, style=stepper.DOUBLE)
        self.release()