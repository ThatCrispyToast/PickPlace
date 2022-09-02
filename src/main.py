from stepper_control import StepperControl
import time

steppers = StepperControl()


start = time.time()
steppers.move_y(steppers.Y_LENGTH, StepperControl.FORWARD)
forwardy = time.time() - start
print(forwardy)
print(steppers.get_pos())
start = time.time()
steppers.move_y(steppers.Y_LENGTH, StepperControl.BACKWARD)
backwardy = time.time() - start
print(backwardy)
print(steppers.get_pos())
