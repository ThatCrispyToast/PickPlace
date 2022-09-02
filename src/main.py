from stepper_control import StepperControl

stepper_control = StepperControl()

stepper_control.move_x(StepperControl.X_LENGTH/2, StepperControl.LEFT)
print(stepper_control.get_pos())