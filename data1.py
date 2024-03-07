import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

motor1_1=23
motor1_2=24
enable1=25

motor2_1=17
motor2_2=27
enable2=22

button=21

GPIO.setup(motor1_2,GPIO.OUT)
GPIO.setup(motor1_1,GPIO.OUT)
GPIO.setup(motor2_1,GPIO.OUT)
GPIO.setup(motor2_2,GPIO.OUT)
GPIO.setup(enable1,GPIO.OUT)
GPIO.setup(enable2,GPIO.OUT)

GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

p1=GPIO.PWM(enable1,1000)
p2=GPIO.PWM(enable2,1000)

p1.start(0)
p2.start(0)

def motor(motor,forward,speed):
    if motor == 1:
        if forward == 1:
            GPIO.output(motor1_1,True)
            GPIO.output(motor1_2,False)
        elif forward == 0:
            GPIO.output(motor1_1,False)
            GPIO.output(motor1_2,True)
        p1.ChangeDutyCycle(speed)
    elif motor == 2:
        if forward == 1:
            GPIO.output(motor2_1,True)
            GPIO.output(motor2_2,False)
        elif forward == 0:
            GPIO.output(motor2_1,False)
            GPIO.output(motor2_2,True)
        p2.ChangeDutyCycle(speed)

def motorstop(motor):
    if motor == 1:
        GPIO.output(motor1_1,False)
        GPIO.output(motor1_2,False)
        p1.ChangeDutyCycle(0)
    elif motor == 2:
        GPIO.output(motor2_1,False)
        GPIO.output(motor2_2,False)
        p2.ChangeDutyCycle(0)

while True:
    if GPIO.input(button) == GPIO.HIGH:
        motor(1,1,50)
        sleep(3)
        motorstop(1)
        sleep(0.5)

        motor(1,0,50)
        sleep(3)
        motorstop(1)
        sleep(1)

        motor(2,1,40)
        sleep(3)
        motorstop(2)
        sleep(0.5)

        motor(2,0,40)
        sleep(3)
        motorstop(2)
        sleep(2)

        motor(1,1,50)
        motor(2,1,40)
        sleep(3)
        motorstop(1)
        motorstop(2)
        sleep(0.5)

        motor(1,0,50)
        motor(2,0,40)
        sleep(3)
        motorstop(1)
        motorstop(2)
        sleep(1)