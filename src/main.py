from stepper_control import StepperControl
import time

steppers = StepperControl()

start = time.time()
steppers.move(0, int(steppers.Y_LENGTH/4), 0)
print(time.time() - start)

print("Done")