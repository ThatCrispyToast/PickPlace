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

x = time.time()

for i in range(800):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    # kit2.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

print(time.time() - x)


release()