from stepper_control import StepperControl
import time

steppers = StepperControl()

start = time.time()
steppers.move(-steppers.X_LENGTH/4, 0, steppers.Z_LENGTH/16)
print(time.time() - start)

print("Done")