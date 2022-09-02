from shutil import move
from stepper_control import StepperControl
import time

steppers = StepperControl()


steppers.move(int(steppers.X_LENGTH/2), int(steppers.Y_LENGTH/2), int(steppers.Z_LENGTH/8))
print(steppers.get_pos())
