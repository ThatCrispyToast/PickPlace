from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import atexit
import multiprocessing

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
        # Initialize Stepper Motors
        self.kit = MotorKit()
        self.kit2 = MotorKit(address=0x61)
        # Register release function to be called on exit
        atexit.register(self.release)
        # Initialize Position
        self.x_pos = 0
        self.y_pos = 0
        self.z_pos = 0
        self.running = False

    def release(self):
        self.kit.stepper1.release()
        self.kit.stepper2.release()
        self.kit2.stepper1.release()
        self.kit2.stepper2.release()

    def move_x(self, steps, direction=LEFT):
        self.running = True
        for _ in range(steps):
            self.kit.stepper1.onestep(direction=direction, style=stepper.DOUBLE)
            self.x_pos += 1 if direction == StepperControl.LEFT else -1
        self.release()
        self.running = False
    
    def move_y(self, steps, direction=FORWARD):
        self.running = True
        for _ in range(steps):
            self.kit.stepper2.onestep(direction=direction, style=stepper.DOUBLE)
            self.y_pos += 1 if direction == StepperControl.FORWARD else -1
        self.release()
        self.running = False

    def move_z(self, steps, direction=UP):
        self.running = True
        for _ in range(steps):
            self.kit2.stepper1.onestep(direction=direction, style=stepper.DOUBLE)
            self.kit2.stepper2.onestep(direction=direction, style=stepper.DOUBLE)
            self.z_pos += 1 if direction == StepperControl.UP else -1
        self.release()
        self.running = False

    def move(self, x, y, z):
        self.running = True
        max_move = max(abs(x), abs(y), abs(z))
        for i in range(max_move):
            if i < abs(x):
                self.kit.stepper1.onestep(direction=StepperControl.LEFT if x > 0 else StepperControl.RIGHT, style=stepper.DOUBLE)
                self.x_pos += 1 if x > 0 else -1
            if i < abs(y):
                self.kit.stepper2.onestep(direction=StepperControl.FORWARD if y > 0 else StepperControl.BACKWARD, style=stepper.DOUBLE)
                self.y_pos += 1 if y > 0 else -1
            if i < abs(z):
                self.kit2.stepper1.onestep(direction=StepperControl.UP if z > 0 else StepperControl.DOWN, style=stepper.DOUBLE)
                self.kit2.stepper2.onestep(direction=StepperControl.UP if z > 0 else StepperControl.DOWN, style=stepper.DOUBLE)
                self.z_pos += 1 if z > 0 else -1
        self.release()
        self.running = False

    def move_async(self, x, y, z):
        self.running = True
        self.procs = []
        if x < 0:
            x = abs(x)
            x_dir = StepperControl.RIGHT
        else:
            x_dir = StepperControl.LEFT
        if y < 0:
            y = abs(y)
            y_dir = StepperControl.BACKWARD
        else:
            y_dir = StepperControl.FORWARD
        if z < 0:
            z = abs(z)
            z_dir = StepperControl.DOWN
        else:
            z_dir = StepperControl.UP
        p1 = multiprocessing.Process(target=self.move_x, args=(x, x_dir,))
        p2 = multiprocessing.Process(target=self.move_y, args=(y, y_dir,))
        p3 = multiprocessing.Process(target=self.move_z, args=(z, z_dir,))
        self.procs.append(p1)
        self.procs.append(p2)
        self.procs.append(p3)
        p1.start()
        p2.start()
        p3.start()
        
    
    def get_pos(self):
        return (self.x_pos, self.y_pos, self.z_pos)

    def is_running(self):
        return any(proc.is_alive() for proc in self.procs)