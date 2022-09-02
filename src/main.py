from shutil import move
from stepper_control import StepperControl
import time

steppers = StepperControl()


steppers.move(steppers.X_LENGTH/2, steppers.Y_LENGTH/2, steppers.Z_LENGTH/2)
print(steppers.get_pos)
