from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.parameters import Axis

# Initialize the hub.
hub = PrimeHub()

# # Get the acceleration or angular_velocity along a single axis.
# # If you need only one value, this is more memory efficient.
# while True:
#     # Read the forward acceleration.
#     forward_acceleration = hub.imu.acceleration(Axis.X)

#     # Read the yaw rate.
#     yaw_rate = hub.imu.angular_velocity(Axis.Z)

#     # Print the yaw rate.
#     print(yaw_rate)
#     wait(100)
left_motor = Motor(Port.E)
right_motor = Motor(Port.F)

while True:
    left_motor.dc(-50)
    right_motor.dc(50)