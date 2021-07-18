import RPi.GPIO as GPIO
import time

led_r = 2
led_g = 3
led_b = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(led_r, GPIO.OUT)
GPIO.setup(led_g, GPIO.OUT)
GPIO.setup(led_b, GPIO.OUT)

while(True):
    rgb = input("input:")
    if rgb == "r":
        GPIO.output(led_r, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_r, GPIO.LOW)
    elif rgb == "g":
        GPIO.output(led_g, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_g, GPIO.LOW)
    elif rgb == "b":
        GPIO.output(led_b, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_b, GPIO.LOW)
    elif rgb == "p":
        GPIO.output(led_r, GPIO.HIGH)
        GPIO.output(led_b, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(led_r, GPIO.LOW)
        GPIO.output(led_b, GPIO.LOW)
