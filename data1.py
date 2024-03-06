import RPi.GPIO as GPIO
import time

motoRPin1=13
motoRPin2=11
enablePin=15

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motoRPin1)