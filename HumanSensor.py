#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sched, time, datetime, threading
import os
import RPi.GPIO as GPIO
from picamera import PiCamera
from google.cloud import storage

client = storage.Client()
bucket = client.get_bucket('test-bucket-mail')
PICTURE_WIDTH = 3280
PICTURE_HEIGHT = 2464
SAVEDIR = "/home/pi/HUMAN-SENSOR/pic/"

INTAVAL = 5
SLEEPTIME = 5

GPIO_PIN = 9
GPIO.setmode( GPIO.BCM )
GPIO.setup( GPIO_PIN, GPIO.IN )

cam = PiCamera()
cam.resolution = ( PICTURE_WIDTH, PICTURE_HEIGHT )
cam.vflip = True
cam.brightness = 55
st = time.time() - INTAVAL

# check → export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/seraphic-scarab-228015-84e9a2d6c81b.json

while True:
    if ( GPIO.input(GPIO_PIN) == GPIO.HIGH ) and (st + INTAVAL < time.time() ):
        st = time.time()
        fileName = time.strftime( "%Y%m%d%H%M%S" ) + ".jpg"
        absoluteFileName = SAVEDIR + fileName
        cam.capture( absoluteFileName , quality=100)
        print("PIN STATUS：" + str(GPIO.input(GPIO_PIN)) + "　captured!!")
        blob = bucket.blob(fileName)
        blob.upload_from_filename(absoluteFileName)
    time.sleep( SLEEPTIME )


