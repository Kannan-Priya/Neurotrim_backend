#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 13:13:43 2021
@author: Priyadarshini Kannan
"""

import time
import RPi.GPIO as GPIO
import setup_sensor

GPIO.setmode(GPIO.BCM)


## Setup for both sensors

#Setup for sensor AMT23 -1 
PIN_CLK1 = 17
PIN_DAT1 = 18
PIN_CS1  = 27
delay = 0.0000005
BITCOUNT = 16

#Setup for sensor RM08 - 2

PIN_CLK2 = 4
PIN_DAT2 = 2

#Setup for solenoid 1

PIN_1 = 10
PIN_2 = 11

#TRY SETTING UP THE GPIO

try:
    #amt23
    GPIO.setup(PIN_CLK1,GPIO.OUT)
    GPIO.setup(PIN_DAT1,GPIO.IN)
    GPIO.setup(PIN_CS1,GPIO.OUT)                                                                                                    
    GPIO.output(PIN_CS1,1)
    GPIO.output(PIN_CLK1,1)
    #rm08
    GPIO.setup(PIN_CLK2,GPIO.OUT)
    GPIO.setup(PIN_DAT2,GPIO.IN)
    GPIO.output(PIN_CLK2,1)
    GPIO.setup(PIN_1,GPIO.OUT)
    GPIO.setup(PIN_2,GPIO.OUT)
    
except:
    print ("ERROR. Unable to setup the configuration requested")                                     
    logging.error("GPIO configurations not setup")

#wait some time to start
time.sleep(0.5)

print( "GPIO configuration enabled")

def read_val():
    i=0
    while(i<60):
        
            pos=setup_sensor.readpos()
            print("The the angle of amt23 is{}".format(pos))
        
        
            position=setup_sensor.ang_pos_rm08()
       
            print("The the angle of rm08 is{}".format(position))
            i=i+1

            return(pos,position)

[a,b] = read_val()           