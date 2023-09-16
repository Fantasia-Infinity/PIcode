#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/28
########################################################################
import RPi.GPIO as GPIO
import time

ledPin = 11    # define ledPin

def setup():
    GPIO.setmode(GPIO.BOARD)       # use PHYSICAL GPIO Numbering
    GPIO.setup(ledPin, GPIO.OUT)   # set the ledPin to OUTPUT mode
    GPIO.output(ledPin, GPIO.LOW)  # make ledPin output LOW level 
    print ('using pin%d'%ledPin)

def loop():
    while True:
        #if there is keyboard input, change the LED state accordingly
        if input() != '1':
            if GPIO.input(ledPin)==GPIO.LOW:
                GPIO.output(ledPin,GPIO.HIGH)
                print('led turned on >>>')
            else :
                GPIO.output(ledPin,GPIO.LOW)
                print('led turned off <<<')
        time.sleep(0.1)
        


def destroy():
    GPIO.cleanup()                      # Release all GPIO

if __name__ == '__main__':    # Program entrance
    print ('Program is starting ... \n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()

