from stepper_control import StepperControl
import time

steppers = StepperControl()

start = time.time()
steppers.move(0, steppers.Z_LENGTH/16, steppers.Z_LENGTH/16)
print(time.time() - start)

print("Done")