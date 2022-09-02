from stepper_control import StepperControl

steppers = StepperControl()

steppers.move_z(steppers.Z_LENGTH, StepperControl.UP)
print(steppers.get_pos())
steppers.move_z(steppers.Z_LENGTH, StepperControl.DOWN)
print(steppers.get_pos())
