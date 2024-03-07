import RPi.GPIO as GPIO
import l293d

GPIO.setmode(GPIO.BOARD)

motor1 = l293d.DC(22,18,16)

motor2 = l293d.DC(15,11,13)
motor2data = l293d.DC(15,11,13)
GPIO.setup(40,GPIO.IN,pull_up_down=GPIO.PUD_UP)
motor1data=l293d.DC(22,18,16)
while True:
    motor1data=l293d.DC(22,18,16)
    motor1data.clockwise(speed=50,duration=3)
    motor1data=l293d.DC(18,22,16)
    motor1data.clockwise(speed=50,duration=3)
    motor2data=l293d.DC(15,11,13)
    motor2data.clockwise(speed=40,duration=3)
    motor2data=l293d.DC(11,15,13)
    motor2data.clockwise(speed=40,duration=3)
    motor1data=l293d.DC
