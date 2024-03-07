import RPi.GPIO as GPIO
import l293d

GPIO.setmode(GPIO.BOARD)

motor1 = l293d.DC(22,18,16)

motor2 = l293d.DC(15,11,13)
GPIO.setup(40,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(40)==1:
        motor1.clockwise(speed=50,duration=3)
