from StepperControl import StepperControl
import time

steppers = StepperControl()

start = time.time()
# Moves X Rail to 1/4 of It's Rail Length to the Left 
steppers.move_y(523, StepperControl.FORWARD, StepperControl.SINGLE, block=False)
steppers.move_x(StepperControl.X_LENGTH/2, StepperControl.LEFT, StepperControl.SINGLE, block=True)
print(time.time() - start)