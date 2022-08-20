from StepperControl import StepperControl
import time

steppers = StepperControl()

# Moves X Rail to 1/4 of It's Rail Length to the Left 
steppers.move_x(StepperControl.X_LENGTH, StepperControl.LEFT, StepperControl.SINGLE)
print("Hello!")