import l293d
import time as sleep

l293d.cleanup()
l293d.Config.pin_numbering = 'BOARD'

motor2data = l293d.DC(15,11,13)
motor1data=l293d.DC(22,18,16)

while True:
    l293d.cleanup()
    motor1data=l293d.DC(22,18,16)
    motor1data.clockwise(speed=50,duration=3)
    sleep(0.5)
    l293d.cleanup()
    motor1data=l293d.DC(18,22,16)
    motor1data.clockwise(speed=50,duration=3)
    sleep(0.5)
    l293d.cleanup()
    motor2data=l293d.DC(15,11,13)
    motor2data.clockwise(speed=40,duration=3)
    sleep(0.5)
    l293d.cleanup()
    motor2data=l293d.DC(11,15,13)
    motor2data.clockwise(speed=40,duration=3)

    l293d.cleanup()
    motor1data=l293d.DC(22,18,16)
    motor2data=l293d.DC(15,11,13)
    motor1data.clockwise(speed=50,wait=False)
    motor2data.clockwise(speed=40,duration=3)
    motor1data.stop()
    sleep(1)

    l293d.cleanup()
    motor1data=l293d.DC(18,22,16)
    motor2data=l293d.DC(11,15,13)
    motor1data.clockwise(speed=50,wait=False)
    motor2data.clockwise(speed=40,duration=3)
    motor1data.stop()
    sleep(3)