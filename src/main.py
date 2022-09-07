from stepper_control import StepperControl

steppers = StepperControl()

steppers.move_async(int(steppers.X_LENGTH/2), int(steppers.Y_LENGTH/4), int(steppers.Z_LENGTH/16))