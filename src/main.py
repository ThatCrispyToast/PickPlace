from stepper_control import StepperControl
import time

steppers = StepperControl()

total = 0

for _ in range(10):
    start = time.time()
    steppers.move(int(steppers.X_LENGTH/2), int(steppers.Y_LENGTH/4), int(steppers.Z_LENGTH/16))
    total = time.time() - start

print(total/10)