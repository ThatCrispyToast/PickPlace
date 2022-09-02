from shutil import move
from stepper_control import StepperControl
import time

steppers = StepperControl()


print(steppers.move(200, 200, 200))
