from stepper_control import StepperControl
import time

steppers = StepperControl()

start = time.time()
steppers.move_z(steppers.Z_LENGTH, StepperControl.UP)
upz = time.time() - start
print(upz)
print(steppers.get_pos())
start = time.time()
steppers.move_z(steppers.Z_LENGTH, StepperControl.DOWN)
downz = time.time() - start
print(downz)
print(steppers.get_pos())

start = time.time()
steppers.move_x(steppers.X_LENGTH, StepperControl.LEFT)
leftx = time.time() - start
print(leftx)
print(steppers.get_pos())
start = time.time()
steppers.move_z(steppers.X_LENGTH, StepperControl.RIGHT)
rightx = time.time() - start
print(rightx)
print(steppers.get_pos())

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

print(upz, downz, leftx, rightx, forwardy, backwardy)