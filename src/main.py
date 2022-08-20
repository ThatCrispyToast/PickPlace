from StepperControl import StepperControl
import time

steppers = StepperControl()

# Moves X Rail to 1/4 of It's Rail Length to the Left 
steppers.move_y(StepperControl.Y_LENGTH, StepperControl.FORWARD, StepperControl.SINGLE)
print(steppers.get_position())
print("Hello!")