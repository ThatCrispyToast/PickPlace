from stepper_control import StepperControl
import time

steppers = StepperControl()

while (True):
    steppers.move(steppers.X_LENGTH/4, steppers.Y_LENGTH/4, steppers.Z_LENGTH/32)
    steppers.move(-steppers.X_LENGTH/4, -steppers.Y_LENGTH/4, -steppers.Z_LENGTH/32)

print("Done")