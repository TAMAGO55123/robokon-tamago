import l293d
import time as sleep


motor2data = l293d.DC(15,11,13)
motor1data=l293d.DC(22,18,16)

while True:
    motor1data=l293d.DC(22,18,16)
    motor1data.clockwise(speed=50,duration=3)
    sleep(0.5)
    motor1data=l293d.DC(18,22,16)
    motor1data.clockwise(speed=50,duration=3)
    sleep(0.5)
    motor2data=l293d.DC(15,11,13)
    motor2data.clockwise(speed=40,duration=3)
    sleep(0.5)
    motor2data=l293d.DC(11,15,13)
    motor2data.clockwise(speed=40,duration=3)

    motor1data=l293d.DC(22,18,16)
    motor2data=l293d.DC(15,11,13)
    motor1data.clockwise(speed=50,wait=False)
    motor2data.clockwise(speed=40,duration=3)
    motor1data.stop()
    sleep(1)

    motor1data=l293d.DC(18,22,16)
    motor2data=l293d.DC(11,15,13)
    motor1data.clockwise(speed=50,wait=False)
    motor2data.clockwise(speed=40,duration=3)
    motor1data.stop()
    sleep(3)


