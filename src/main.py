from stepper_control import StepperControl

steppers = StepperControl()

# steppers.move_x(int(StepperControl.X_LENGTH/2), StepperControl.LEFT
steppers.move_z(int(6400 * 1.5), StepperControl.UP)


print(steppers.get_pos())