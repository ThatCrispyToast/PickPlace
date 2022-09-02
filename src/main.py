from stepper_control import StepperControl
import time

steppers = StepperControl()

start = time.time()
steppers.move_z(steppers.Z_LENGTH, StepperControl.UP)
print(time.time() - start)
print(steppers.get_pos())
start = time.time()
steppers.move_z(steppers.Z_LENGTH, StepperControl.DOWN)
print(time.time() - start)
print(steppers.get_pos())
