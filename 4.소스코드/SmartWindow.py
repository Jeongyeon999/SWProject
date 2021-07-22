from urllib.request import urlopen, Request
import urllib
import bs4
import RPi.GPIO as GPIO
import time

led_r = 2 # rgb_led red 핀번호
led_g = 3 # rgb_led green 핀번호
led_b = 4 # rgb_led blue 핀번호

motor_pin = 18 # 모터의 핀번호

trig = 23 # trig 핀번호
echo = 24 # echo 핀번호

motor_c = 6
motor_o = 8
motor_s = 7

GPIO.setmode(GPIO.BCM) # BCM2835 CPU 칩의 신호 이름 사용
GPIO.setwarnings(False)

# LED
GPIO.setup(led_r, GPIO.OUT)
GPIO.setup(led_g, GPIO.OUT)
GPIO.setup(led_b, GPIO.OUT)
# Motor
GPIO.setup(motor_pin, GPIO.OUT)
# Ultrasonic
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

# LED OFF
GPIO.output(led_r, GPIO.LOW)
GPIO.output(led_g, GPIO.LOW)
GPIO.output(led_b, GPIO.LOW)

motor = GPIO.PWM(motor_pin, 50) # frequency = 50
angle = 7 # 초기값 (모터 정지 상태)
motor.start(angle)

location = input("지역:")
while(True):
    # 미세먼지 수치 크롤링
    input_location = urllib.parse.quote(location + '미세먼지')

    url = 'https://search.naver.com/search.naver?ie=utf8&query='+ input_location

    req = Request(url)
    page = urlopen(req)
    html = page.read()
    soup = bs4.BeautifulSoup(html, 'html5lib')
    fine_dust = (soup.find('div', class_='state_info _fine_dust')
          .find('span', class_='num _value').text)

    ultra_fine_dust = (soup.find('div', class_='state_info _ultrafine_dust')
          .find('span', class_='num _value').text)

    if(fine_dust == "-" or ultra_fine_dust == "-"):
        GPIO.output(led_b, GPIO.HIGH)
        #############################
        while(True):
            GPIO.output(trig, False)
            time.sleep(0.5)
            
            GPIO.output(trig, True)
            time.sleep(0.00001)
            GPIO.output(trig, False)
            
            while GPIO.input(echo) == False: 
                pulse_start = time.time()
            
            while GPIO.input(echo) == True: 
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start 
            distance = pulse_duration * 17000
            distance = round(distance, 2)

            # 창문 닫혀있으면 열기
            motor.ChangeDutyCycle(motor_o)            
            if(distance <= 6):
                motor.ChangeDutyCycle(motor_s)
                break
        ##############################
        
        print("미세먼지: " + fine_dust)
        print("초미세먼지: " + ultra_fine_dust)
        print("미세먼지 상태: 측정불가(좋음)")
        
    else:
        i_fine_dust = int(fine_dust)
        i_ultra_fine_dust = int(ultra_fine_dust)
        
        if(i_fine_dust > 150 or i_ultra_fine_dust > 75):
            GPIO.output(led_r, GPIO.HIGH)
            #############################
            while(True):
                GPIO.output(trig, False)
                time.sleep(0.5)
                
                GPIO.output(trig, True)
                time.sleep(0.00001)
                GPIO.output(trig, False)
                
                while GPIO.input(echo) == False: 
                    pulse_start = time.time()
                
                while GPIO.input(echo) == True: 
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start 
                distance = pulse_duration * 17000
                distance = round(distance, 2)

                # 창문 열려 있으면 닫기
                motor.ChangeDutyCycle(motor_c)
                if(distance >= 11.3):
                    motor.ChangeDutyCycle(motor_s)
                    break
            ##############################
            print("미세먼지: " + fine_dust)
            print("초미세먼지: " + ultra_fine_dust)
            print("미세먼지 상태: 매우 나쁨")
            
        elif(i_fine_dust > 80 or i_ultra_fine_dust > 35):
            GPIO.output(led_r, GPIO.HIGH)
            GPIO.output(led_b, GPIO.HIGH)
            #############################
            while(True):
                GPIO.output(trig, False)
                time.sleep(0.5)
                
                GPIO.output(trig, True)
                time.sleep(0.00001)
                GPIO.output(trig, False)
                
                while GPIO.input(echo) == False: 
                    pulse_start = time.time()
                
                while GPIO.input(echo) == True: 
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start 
                distance = pulse_duration * 17000
                distance = round(distance, 2)

                # 창문 열려 있으면 닫기
                motor.ChangeDutyCycle(motor_c)
                if(distance >= 11.3):
                    motor.ChangeDutyCycle(motor_s)
                    break
            ##############################
            print("미세먼지: " + fine_dust)
            print("초미세먼지: " + ultra_fine_dust)
            print("미세먼지 상태: 나쁨")
            
        elif(i_fine_dust > 30 or i_ultra_fine_dust > 15):
            GPIO.output(led_g, GPIO.HIGH)
            #############################
            while(True):
                GPIO.output(trig, False)
                time.sleep(0.5)
                
                GPIO.output(trig, True)
                time.sleep(0.00001)
                GPIO.output(trig, False)
                
                while GPIO.input(echo) == False: 
                    pulse_start = time.time()
                
                while GPIO.input(echo) == True: 
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start 
                distance = pulse_duration * 17000
                distance = round(distance, 2)

                # 창문 닫혀있으면 열기
                motor.ChangeDutyCycle(motor_o)
                if(distance <= 6):
                    motor.ChangeDutyCycle(motor_s)
                    break
            ##############################
            print("미세먼지: " + fine_dust)
            print("초미세먼지: " + ultra_fine_dust)
            print("미세먼지 상태: 보통")
            
        else:
            GPIO.output(led_b, GPIO.HIGH)
            #############################
            while(True):
                GPIO.output(trig, False)
                time.sleep(0.5)
                
                GPIO.output(trig, True)
                time.sleep(0.00001)
                GPIO.output(trig, False)
                
                while GPIO.input(echo) == False: 
                    pulse_start = time.time()
                
                while GPIO.input(echo) == True: 
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start
                distance = pulse_duration * 17000
                distance = round(distance, 2)

                # 창문 닫혀있으면 열기
                motor.ChangeDutyCycle(motor_o)
                if(distance <= 6):
                    motor.ChangeDutyCycle(motor_s)
                    break
            ##############################
            print("미세먼지: " + fine_dust)
            print("초미세먼지: " + ultra_fine_dust)
            print("미세먼지 상태: 좋음")
