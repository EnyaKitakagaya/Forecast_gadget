#!/use/bin/python3
# -*- coding: utf-8 -*-

# モジュールのロード
import time
import RPi.GPIO as GPIO

# GPIOの設定
GPIO.setmode(GPIO.BCM)

# 出力LEDのGPIOピン番号
GPIO_LED = 17

# GPIOのピン番号を出力に設定
GPIO.setup(GPIO_LED, GPIO.OUT)

try:
    while(1):
        GPIO.output(GPIO_LED, GPIO.HIGH) 
        time.sleep(1)
        GPIO.output(GPIO_LED, GPIO.LOW) 
        time.sleep(1)
except KeyboardInterrupt:
    pass

# GPIOの終了処理
GPIO.cleanup()
