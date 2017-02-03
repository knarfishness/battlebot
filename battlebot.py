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
from Adafruit_MotorHAT import Adafruit_MotorHAT

print "Initializing"
p=ps3()		#Create a PS3 object

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
		leftSpeed = abs((left_stick-90)*2.8)
		left.setSpeed(int(leftSpeed))
		left.run(Adafruit_MotorHAT.FORWARD)
	elif left_stick < 90:
		leftSpeed = abs((left_stick-90)*2.8)
		left.setSpeed(int(leftSpeed))
		left.run(Adafruit_MotorHAT.BACKWARD)
	else:
		left.run(Adafruit_MotorHAT.RELEASE)

	if right_stick > 90:
		rightSpeed = abs((right_stick-90)*2.8)
		right.setSpeed(int(rightSpeed))
		right.run(Adafruit_MotorHAT.FORWARD)
	elif right_stick < 90:
		rightSpeed = abs((right_stick-90)*2.8)
		right.setSpeed(int(rightSpeed))
		right.run(Adafruit_MotorHAT.BACKWARD)
	else:
		right.run(Adafruit_MotorHAT.RELEASE)

	time.sleep(.01)