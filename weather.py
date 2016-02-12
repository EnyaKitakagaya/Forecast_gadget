import time
import urllib.request
import json
import re
import RPi.GPIO as GPIO

url = 'http://api.openweathermap.org/data/2.5/forecast?q=Osaka-shi,jp&mode=json&appid='
response = urllib.request.urlopen(url)
encoding = response.headers.get_content_charset()
line = response.read().decode(encoding)

pattern = re.compile(r'\d+')
for i in range(8):
    decode = json.loads(line)
    dt_txt = decode['list'][i]['dt_txt']
    strlist = pattern.findall(dt_txt)
    if strlist[3] == "06":
        weather_06 = decode['list'][i]['weather'][0]['main']
    elif strlist[3] == "12":
        weather_12 = decode['list'][i]['weather'][0]['main']
    elif strlist[3] == "18":
        weather_18 = decode['list'][i]['weather'][0]['main']

print("06: " + weather_06)
print("12: " + weather_12)
print("18: " + weather_18)

GPIO.setmode(GPIO.BCM)

GPIO_06 = 17
GPIO_12 = 18
GPIO_18 = 27

GPIO.setup(GPIO_06, GPIO.OUT)
GPIO.setup(GPIO_12, GPIO.OUT)
GPIO.setup(GPIO_18, GPIO.OUT)

GPIO.output(GPIO_06, GPIO.LOW) 
GPIO.output(GPIO_12, GPIO.LOW) 
GPIO.output(GPIO_18, GPIO.LOW) 

p06 = GPIO.PWM(GPIO_06, 60)
p12 = GPIO.PWM(GPIO_12, 60)
p18 = GPIO.PWM(GPIO_18, 60)

p06.start(0)
p12.start(0)
p18.start(0)

if weather_06 == "Rain" or weather_06 == "Snow":
    p06.ChangeDutyCycle(100)
elif weather_06 == "Clouds":
    p06.ChangeDutyCycle(50)

if weather_12 == "Rain" or weather_12 == "Snow":
    p12.ChangeDutyCycle(100)
elif weather_12 == "Clouds":
    p12.ChangeDutyCycle(50)

if weather_18 == "Rain" or weather_18 == "Snow":
    p18.ChangeDutyCycle(100)
elif weather_18 == "Clouds":
    p18.ChangeDutyCycle(50)

try:
    while(1):
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

p06.stop()
p12.stop()
p18.stop()

GPIO.cleanup()
