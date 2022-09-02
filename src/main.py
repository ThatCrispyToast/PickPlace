import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()
kit2 = MotorKit(address=0x61)

def release():
    kit.stepper1.release()
    kit.stepper2.release()
    kit2.stepper1.release()
    kit2.stepper2.release()

for i in range(400):
    kit2.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    kit2.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
print("single")
for i in range(400):
    kit2.stepper1.onestep(direction=stepper.BACKWARD)
    kit2.stepper2.onestep(direction=stepper.BACKWARD)


release()