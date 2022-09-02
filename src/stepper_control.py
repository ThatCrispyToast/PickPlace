from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import atexit

class StepperControl:

    # Movement Direction Constants
    UP = stepper.BACKWARD
    DOWN = stepper.FORWARD
    RIGHT = stepper.BACKWARD
    LEFT = stepper.FORWARD
    BACKWARD = stepper.BACKWARD
    FORWARD = stepper.FORWARD

    # Track Lengths
    X_LENGTH = 1490
    Y_LENGTH = 1550
    Z_LENGTH = 10400

    def __init__(self):
        self.kit = MotorKit()
        self.kit2 = MotorKit(address=0x61)
        atexit.register(self.release)
        self.x_pos = 0
        self.y_pos = 0
        self.z_pos = 0

    def release(self):
        self.kit.stepper1.release()
        self.kit.stepper2.release()
        self.kit2.stepper1.release()
        self.kit2.stepper2.release()

    def move_x(self, steps, direction=LEFT):
        for _ in range(steps):
            self.kit.stepper1.onestep(direction=direction, style=stepper.DOUBLE)
            self.x_pos += 1 if direction == StepperControl.LEFT else -1
        self.release()
    
    def move_y(self, steps, direction=FORWARD):
        for _ in range(steps):
            self.kit.stepper2.onestep(direction=direction, style=stepper.DOUBLE)
            self.y_pos += 1 if direction == StepperControl.FORWARD else -1
        self.release()

    def move_z(self, steps, direction=UP):
        for _ in range(steps):
            self.kit2.stepper1.onestep(direction=direction, style=stepper.DOUBLE)
            self.kit2.stepper2.onestep(direction=direction, style=stepper.DOUBLE)
            self.z_pos += 1 if direction == StepperControl.UP else -1
        self.release()

    def move(self, x, y, z):
        return max(x, y)
    
    def get_pos(self):
        return (self.x_pos, self.y_pos, self.z_pos)