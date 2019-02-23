#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sched, time, datetime, threading
import os
import RPi.GPIO as GPIO
from picamera import PiCamera
from google.cloud import storage

PICTURE_WIDTH = 1000
PICTURE_HEIGHT = 1000
SAVEDIR = "/home/pi/HUMAN-SENSOR/pic/"

INTAVAL = 5
SLEEPTIME = 5

GPIO_PIN = 9

GPIO.setmode( GPIO.BCM )
GPIO.setup( GPIO_PIN, GPIO.IN )

cam = PiCamera()
cam.resolution = ( PICTURE_WIDTH, PICTURE_HEIGHT )

st = time.time() - INTAVAL

while True:
    if ( GPIO.input(GPIO_PIN) == GPIO.HIGH ) and (st + INTAVAL < time.time() ):
        st = time.time()
        filename = time.strftime( "%Y%m%d%H%M%S" ) + ".jpg"
        save_file = SAVEDIR + filename
        cam.capture( save_file )
        print("PIN STATUS：" + str(GPIO.input(GPIO_PIN)) + "　captured!!")
    
    time.sleep( SLEEPTIME )


