from stepper_control import StepperControl
import time

steppers = StepperControl()

start = time.time()
steppers.move(int(steppers.X_LENGTH/2), int(steppers.Y_LENGTH/4), int(steppers.Z_LENGTH/16))
print(time.time() - start)