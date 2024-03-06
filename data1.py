import l293d

motor1 = l293d.DC(22,18,16)
motor2 = l293d.DC(15,11,13)

while True:
    motor1.clockwise(speed=50,duration=5)
    