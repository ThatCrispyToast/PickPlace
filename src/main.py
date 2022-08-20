from StepperControl import StepperControl
import time

steppers = StepperControl()

# Moves X Rail to 1/4 of It's Rail Length to the Left 
steppers.move_x(StepperControl.X_LENGTH/8, StepperControl.LEFT, StepperControl.SINGLE)
print(steppers.get_position)
print("Hello!")