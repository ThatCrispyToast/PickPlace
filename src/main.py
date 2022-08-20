from StepperControl import StepperControl

steppers = StepperControl()

# Moves X Rail to 1/4 of It's Rail Length to the Left 
steppers.move_x(StepperControl.X_LENGTH/4, StepperControl.LEFT, StepperControl.SINGLE)