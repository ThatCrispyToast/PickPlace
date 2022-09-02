from stepper_control import StepperControl
import time

steppers = StepperControl()

start = time.time()
steppers.move(int(steppers.X_LENGTH/2), int(steppers.Y_LENGTH/4), 0)
print(time.time() - start)

start = time.time()
steppers.move_x(int(steppers.X_LENGTH/2), StepperControl.RIGHT)
steppers.move_y(int(steppers.Y_LENGTH/4), StepperControl.BACKWARD)
print(time.time() - start)
