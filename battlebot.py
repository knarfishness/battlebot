#!/usr/bin/env python
########################################################################                                               
# This example controls a Raspberry Pi Motor Hat using a PS3 Dualshock 3 controller
#                                
# History
# ------------------------------------------------
# Author     	Date      		Comments
# Frank Avery   2 Feb 2017		Initial Authoring                                                        
#

########################################################################
from ps3 import *		#Import the PS3 library
from Adafruit_MotorHAT import Adafruit_MotorHAT

print "Initializing BattleBot Sequence"

#Create a PS3 controller object
p=ps3()

# Initialize motor HAT and left, right motor.
mh = Adafruit_MotorHAT(0x60)

print "BattleBot Sequence Complete. BattleBot is GO!"

# Reverse these values to switch motor sides
left_id = 2
right_id = 1
left = mh.getMotor(left_id)
right = mh.getMotor(right_id)

# Start with motors turned off
left.run(Adafruit_MotorHAT.RELEASE)
right.run(Adafruit_MotorHAT.RELEASE)

# This is the main loop of the program
while True:

	# Reads in the values from the PS3 controller
	p.update()

	# value will be 90 at neutral, 0 at full throttle and 179 at full down
	left_stick = (p.a_joystick_left_y+1)*90 
	right_stick = (p.a_joystick_right_y+1)*90

	# speed control logic, left
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

	# speed control logic, right
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

	# for stability
	time.sleep(.01)