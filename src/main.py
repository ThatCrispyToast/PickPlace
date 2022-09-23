from stepper_control import StepperControl
import time

steppers = StepperControl()

while (True):
    steppers.move(steppers.X_LENGTH/2, 0, 0)
    steppers.move(-steppers.X_LENGTH/2, 0, 0)

print("Done")