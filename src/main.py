from stepper_control import StepperControl

steppers = StepperControl()

# steppers.move_x(int(StepperControl.X_LENGTH/2), StepperControl.LEFT
steppers.move_z(800 * 4, StepperControl.UP)


print(steppers.get_pos())