from StepperControl import StepperControl
import time

steppers = StepperControl()

# Moves X Rail to 1/4 of It's Rail Length to the Left 
steppers.move_x(StepperControl.X_LENGTH/4, StepperControl.LEFT, StepperControl.SINGLE, block=False)
time.sleep(1)
print(steppers.get_position())
print("Hello!")