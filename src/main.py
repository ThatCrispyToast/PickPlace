from stepper_control import StepperControl
import time

steppers = StepperControl()

steppers.move_async(int(steppers.X_LENGTH/2), int(steppers.Y_LENGTH/4), int(steppers.Z_LENGTH/32))
while steppers.is_running():
    time.sleep(0.1)

print("Done")