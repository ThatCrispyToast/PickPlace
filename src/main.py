from stepper_control import StepperControl
import time

steppers = StepperControl()

start = time.time()
steppers.move_async(int(-steppers.X_LENGTH/2), int(-steppers.Y_LENGTH/4), int(-steppers.Z_LENGTH/32))
while steppers.is_running():
    time.sleep(0.1)
print(time.time() - start)

start = time.time()
steppers.move(int(-steppers.X_LENGTH/2), int(-steppers.Y_LENGTH/4), int(-steppers.Z_LENGTH/32))
print(time.time() - start)

print("Done")