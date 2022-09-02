from stepper_control import StepperControl
import time

steppers = StepperControl()

total_combined = 0
total_individual = 0

TRIALS = 10

for _ in range(TRIALS):
    start = time.time()
    steppers.move(int(steppers.X_LENGTH/2), int(steppers.Y_LENGTH/4), 0)
    total_combined += time.time() - start

    start = time.time()
    steppers.move_x(int(steppers.X_LENGTH/2), StepperControl.RIGHT)
    steppers.move_y(int(steppers.Y_LENGTH/4), StepperControl.BACKWARD)
    total_individual += time.time() - start

print("Combined: ", total_combined / TRIALS)
print("Individual: ", total_individual / TRIALS)