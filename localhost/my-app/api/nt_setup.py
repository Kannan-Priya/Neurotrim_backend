#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:18:28 2021
Sensor setup function
@author: Priya Kannan
"""

import time
import logging
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

#################################----------------------------#####################################
## Setup for both sensors

#Setup for sensor AMT23 -1 
CLK_ER = 17
DAT_ER = 18
CS_ER  = 27
delay = 0.0000005
BITCOUNT = 16

#Setup for sensor RM08 - 2

CLK_ET = 4
DAT_ET = 2

#Setup for solenoid 1

SR_1 = 10
SR_2 = 11

#Setup for solenoid 1

ST_1 = 10
ST_2 = 11

###############################------------------------------#######################################
#TRY SETTING UP THE GPIO

try:
    ##ER
    GPIO.setup(CLK_ER,GPIO.OUT)
    GPIO.setup(DAT_ER,GPIO.IN)
    GPIO.setup(CS_ER,GPIO.OUT)                                                                                                    
    GPIO.output(CLK_ER,1)
    GPIO.output(DAT_ER,1)

    ##ET
    GPIO.setup(CLK_ET,GPIO.OUT)
    GPIO.setup(DAT_ET,GPIO.IN)
    GPIO.output(CLK_ET,1)

    ##SR
    GPIO.setup(SR_1,GPIO.OUT)
    GPIO.setup(SR_2,GPIO.OUT)

    ##ST
    GPIO.setup(ST_1,GPIO.OUT)
    GPIO.setup(ST_2,GPIO.OUT)
   
    
except:
    print ("ERROR. Unable to setup the configuration requested")                                     
    logging.error("GPIO configurations not setup")
    
#wait some time to start
time.sleep(0.5)

print( "GPIO configuration enabled")
logging.info("Configure enabled")

#############################------------------Sensor functions------------------#################################

"""
Sensor amt23 data collection
function to collect angle
returns angle
takes global variables like pin setup
"""

def readpos():
    GPIO.output(PIN_CS1,0)
    time.sleep(delay*2)
    GPIO.output(PIN_CLK1,0)
    l=[]
    for i in range(0,BITCOUNT):
        if i<14:
            
            GPIO.output(PIN_CLK1,1)
            data=GPIO.input(PIN_DAT1)
            l.append(data)
            GPIO.output(PIN_CLK1,0)
        else:
            for k in range(0,6):
                GPIO.output(PIN_CLK1,1)
                GPIO.output(PIN_CLK1,0)
    GPIO.output(PIN_CS1,1)
    ##conversion of rotation bits to angle
    pos_dec= ''
    i=2
    while i<len(l):
          pos_dec += str(l[i])
          i=i+1
    pos_dec=int(pos_dec, 2)
    angle=pos_dec*360/4096
    logging.info('amt_23 data logged')
    return angle

"""
Sensor rm08 data collection
function to collect angle
returns angle
takes global variables like pin setup
"""

def ang_pos_rm08():
  
    k=[]
  
    for i in range(0,BITCOUNT-4):
            GPIO.output(PIN_CLK2,1)
            time.sleep(0.0000001)
            GPIO.output(PIN_CLK2,0)
     
            data=GPIO.input(PIN_DAT2)
            k.append(data)
            GPIO.output(PIN_CLK2,1)
            
    
    pos_dec1=' '
    j=0
    while j<len(k):
          pos_dec1 += str(k[j])
          j=j+1
       
    pos1_dec=int(pos_dec1, 2)
    angle1=pos1_dec*360/4096
    logging.info('rm08 data logged')       

    return angle1

"""
Solenoid latching
function to lock and unlock
returns null
takes global variables like pin setup
"""

def solenoid_latch(pos):
    
       
       GPIO.setup(RELAY_PIN,0)
       GPIO.output(PIN_1,1)
       GPIO.output(PIN_2,0)
       time.sleep(0.2)
       logging.info("solenoid latched")
       print("Solenoid latched")
       GPIO.setup(RELAY_PIN,1)
    
def solenoid_unlatch():
    GPIO.setup(RELAY_PIN,0)
    GPIO.output(PIN_1,0)
    GPIO.output(PIN_2,1)
    time.sleep(0.1)
    GPIO.setup(RELAY_PIN,1)
    logging.info("solenoid unlatched")
    print("Solenoid unlatched")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 13:18:28 2021
Sensor setup function
@author: Priya Kannan
"""

import time
import logging
import RPi.GPIO as GPIO


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

#Relay pin
RELAY_PIN = 22

#TRY SETTING UP THE GPIO

try:
    GPIO.setup(PIN_CLK1,GPIO.OUT)
    GPIO.setup(PIN_DAT1,GPIO.IN)
    GPIO.setup(PIN_CS1,GPIO.OUT)                                                                                                    
    GPIO.output(PIN_CS1,1)
    GPIO.output(PIN_CLK1,1)

    GPIO.setup(PIN_CLK2,GPIO.OUT)
    GPIO.setup(PIN_DAT2,GPIO.IN)
    GPIO.output(PIN_CLK2,1)
    #GPIO.setup(PIN_1,GPIO.OUT)
    #GPIO.setup(PIN_2,GPIO.OUT)
    #GPIO.setup(RELAY_PIN.OUT)
    #GPIO.setup(RELAY_PIN,1)
    
except:
    print ("ERROR. Unable to setup the configuration requested")                                     
   
#wait some time to start
time.sleep(0.5)

print( "GPIO configuration enabled")



"""
Sensor amt23 data collection
function to collect angle
returns angle
takes global variables like pin setup
"""

def readpos():
    GPIO.output(PIN_CS1,0)
    time.sleep(delay*2)
    GPIO.output(PIN_CLK1,0)
    l=[]
    for i in range(0,BITCOUNT):
        if i<14:
            
            GPIO.output(PIN_CLK1,1)
            data=GPIO.input(PIN_DAT1)
            l.append(data)
            GPIO.output(PIN_CLK1,0)
        else:
            for k in range(0,6):
                GPIO.output(PIN_CLK1,1)
                GPIO.output(PIN_CLK1,0)
    GPIO.output(PIN_CS1,1)
    ##conversion of rotation bits to angle
    pos_dec= ''
    i=2
    while i<len(l):
          pos_dec += str(l[i])
          i=i+1
    pos_dec=int(pos_dec, 2)
    angle=pos_dec*360/4096
    logging.info('amt_23 data logged')
    return angle

"""
Sensor rm08 data collection
function to collect angle
returns angle
takes global variables like pin setup
"""

def ang_pos_rm08():
  
    k=[]
  
    for i in range(0,BITCOUNT-4):
            GPIO.output(PIN_CLK2,1)
            time.sleep(0.0000001)
            GPIO.output(PIN_CLK2,0)
     
            data=GPIO.input(PIN_DAT2)
            k.append(data)
            GPIO.output(PIN_CLK2,1)
            
    
    pos_dec1=' '
    j=0
    while j<len(k):
          pos_dec1 += str(k[j])
          j=j+1
       
    pos1_dec=int(pos_dec1, 2)
    angle1=pos1_dec*360/4096
    logging.info('rm08 data logged')       

    return angle1

"""
Solenoid latching
function to lock and unlock
returns null
takes global variables like pin setup
"""

def solenoid_latch(pos):
    
       
       GPIO.setup(RELAY_PIN,0)
       GPIO.output(PIN_1,1)
       GPIO.output(PIN_2,0)
       time.sleep(0.2)
       logging.info("solenoid latched")
       print("Solenoid latched")
       GPIO.setup(RELAY_PIN,1)
    
def solenoid_unlatch():
    GPIO.setup(RELAY_PIN,0)
    GPIO.output(PIN_1,0)
    GPIO.output(PIN_2,1)
    time.sleep(0.1)
    GPIO.setup(RELAY_PIN,1)
    logging.info("solenoid unlatched")
    print("Solenoid unlatched")