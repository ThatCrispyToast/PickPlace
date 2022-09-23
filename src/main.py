from stepper_control import StepperControl
import time

steppers = StepperControl()

start = time.time()
steppers.move(int(steppers.X_LENGTH/2), 0, 0)
print(time.time() - start)

print("Done")