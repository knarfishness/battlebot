#!/usr/bin/env python
########################################################################                                               
# This example controls the GoPiGo and using a PS3 Dualshock 3 controller
#                                
# http://www.dexterindustries.com/GoPiGo/                                                                
# History
# ------------------------------------------------
# Author     	Date      		Comments
# Karan Nayan   11 July 14		Initial Authoring                                                   
'''
## License
 GoPiGo for the Raspberry Pi: an open source robotics platform for the Raspberry Pi.
 Copyright (C) 2015  Dexter Industries

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl-3.0.txt>.
'''         
#
# left,right,up,down to control
# cross to stop
# left joy to turn the camera servo
# l2 to increase speed
# r2 to decrease speed
########################################################################
from ps3 import *		#Import the PS3 library
import Robot
from Adafruit_MotorHAT import Adafruit_MotorHAT


# Set the trim offset for each motor (left and right).  This is a value that
# will offset the speed of movement of each motor in order to make them both
# move at the same desired speed.  Because there's no feedback the robot doesn't
# know how fast each motor is spinning and the robot can pull to a side if one
# motor spins faster than the other motor.  To determine the trim values move the
# robot forward slowly (around 100 speed) and watch if it veers to the left or
# right.  If it veers left then the _right_ motor is spinning faster so try
# setting RIGHT_TRIM to a small negative value, like -5, to slow down the right
# motor.  Likewise if it veers right then adjust the _left_ motor trim to a small
# negative value.  Increase or decrease the trim value until the bot moves
# straight forward/backward.
LEFT_TRIM   = 0
RIGHT_TRIM  = 0

print "Initializing"
p=ps3()		#Create a PS3 object

# Create an instance of the robot with the specified trim values.
# Not shown are other optional parameters:
#  - addr: The I2C address of the motor HAT, default is 0x60.
#  - left_id: The ID of the left motor, default is 1.
#  - right_id: The ID of the right motor, default is 2.
robot = Robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)

print "Done"
s=150	#Initialize

# Initialize motor HAT and left, right motor.
mh = Adafruit_MotorHAT(0x60)
left_id = 2
right_id = 1
left = mh.getMotor(left_id)
right = mh.getMotor(right_id)

# Start with motors turned off.
left.run(Adafruit_MotorHAT.RELEASE)
right.run(Adafruit_MotorHAT.RELEASE)


flag=0
while True:
	p.update()			#Read the ps3 values

	# value will be 90 at neutral, 0 at full throttle and 179 at full down
	left_stick = (p.a_joystick_left_y+1)*90 
	right_stick = (p.a_joystick_right_y+1)*90


	if left_stick > 90:
		left.run(Adafruit_MotorHAT.FORWARD)
		leftSpeed = abs((left_stick-90)*2.8)
		left.setSpeed(leftSpeed)
	elif left_stick < 90:
		left.run(Adafruit_MotorHAT.BACKWARD)
		leftSpeed = (left_stick-90)*2.8
	else:
		left.run(Adafruit_MotorHAT.RELEASE)

	if right_stick > 90:
		right.run(Adafruit_MotorHAT.FORWARD)
		rightSpeed = abs((right_stick-90)*2.8)
		right.setSpeed(rightSpeed)
	elif right_stick < 90:
		right.run(Adafruit_MotorHAT.BACKWARD)
		rightSpeed = (left_stick-90)*2.8
		right.setSpeed(rightSpeed)
	else:
		right.run(Adafruit_MotorHAT.RELEASE)

	time.sleep(.01)