from StepperControl import StepperControl
import time

steppers = StepperControl()

# Moves X Rail to 1/4 of It's Rail Length to the Left 
steppers.move_x(StepperControl.X_LENGTH/2, StepperControl.LEFT, StepperControl.SINGLE, block=False)
steppers.move_y(StepperControl.Y_LENGTH/2, StepperControl.FORWARD, StepperControl.SINGLE, block=True)
print(steppers.get_position())
print("Hello!")