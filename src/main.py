from stepper_control import StepperControl
import time

steppers = StepperControl()

total = 0

for _ in range(3):
    start = time.time()
    steppers.move_async(int(steppers.X_LENGTH/2), int(steppers.Y_LENGTH/4), int(steppers.Z_LENGTH/16))
    while steppers.is_running():
        pass
    total += time.time() - start
    start = time.time()
    steppers.move_async(int(-steppers.X_LENGTH/2), int(-steppers.Y_LENGTH/4), int(-steppers.Z_LENGTH/16))
    while steppers.is_running():
        pass
    total += time.time() - start

print(total/3)