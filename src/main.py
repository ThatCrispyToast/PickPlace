from stepper_control import StepperControl
import time

steppers = StepperControl()

total = 0

for _ in range(2):
    start = time.time()
    steppers.move_async(int(steppers.X_LENGTH/2), int(steppers.Y_LENGTH/4), int(steppers.Z_LENGTH/16))
    total += time.time() - start
    start = time.time()
    steppers.move_async(int(-steppers.X_LENGTH/2), int(-steppers.Y_LENGTH/4), int(-steppers.Z_LENGTH/16))
    total += time.time() - start


totala = 0

for _ in range(2):
    start = time.time()
    steppers.move(int(steppers.X_LENGTH/2), int(steppers.Y_LENGTH/4), int(steppers.Z_LENGTH/16))
    totala += time.time() - start
    start = time.time()
    steppers.move(int(-steppers.X_LENGTH/2), int(-steppers.Y_LENGTH/4), int(-steppers.Z_LENGTH/16))
    totala += time.time() - start


# Output:
print("Total time for async: ", total)
print("Total time for sync: ", totala)