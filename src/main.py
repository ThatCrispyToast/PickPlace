from StepperControl import StepperControl
import time

steppers = StepperControl()

# start = time.time()
# steppers.move_y(523, StepperControl.FORWARD, StepperControl.SINGLE, block=False)
# steppers.move_x(StepperControl.X_LENGTH/2, StepperControl.LEFT, StepperControl.SINGLE, block=True)
# print(time.time() - start)

print(steppers.move_xy(StepperControl.X_LENGTH/2, StepperControl.LEFT, StepperControl.SINGLE, 523, StepperControl.FORWARD, StepperControl.SINGLE))