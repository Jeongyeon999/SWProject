import RPi.GPIO as GPIO

motor_pin = 18 # 모터의 핀번호
GPIO.setmode(GPIO.BCM) # BCM2835 CPU 칩의 신호 이름 사용
GPIO.setup(motor_pin, GPIO.OUT)
motor = GPIO.PWM(motor_pin, 50) # frequency = 50
angle = 7 # 초기값 (모터 정지 상태)
motor.start(angle)

while True:
    cmd = input("r/l:")
    direction = cmd[0]
    if direction == "r": # 시계방향(오른쪽)으로 회전
        angle = 8
    elif direction == "l": # 반시계방향(왼쪽)으로 회전
        angle = 6
    else: # 정지
        angle = 7
    print("anlge=", angle)
    motor.ChangeDutyCycle(angle)
GPIO.cleanup()
