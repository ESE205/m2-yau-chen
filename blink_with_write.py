import RPi.GPIO as GPIO
import time
from time import sleep
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

ITER_COUNT = 15
INPUT_PIN = 11
LED_PIN = 16
LED_IS_ON = False
i = 0

DEBUG = False
if '-debug' in sys.argv:
    DEBUG = True
GPIO.setup(INPUT_PIN,GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT, initial = GPIO.LOW)

with open('data.txt','w') as data:
    while i == 0:
        if not GPIO.input(INPUT_PIN):
            BlinkRate = int(input("Input Blink Rate: "))
            TIME = int(input("Input Time: "))
            while TIME > 0:                         # Run TIME seconds
                TIME -= BlinkRate * 2                # Decrement counter
                GPIO.output(LED_PIN, GPIO.HIGH)         # Turn on
                sleep(BlinkRate)                     # Sleep for 1 second
                LED_IS_ON = not LED_IS_ON
                data.write(f'{time.time():1.0f} {LED_IS_ON}\n')
                GPIO.output(LED_PIN, GPIO.LOW)          # Turn off
                sleep(BlinkRate)                     # Sleep for 1 second
                LED_IS_ON = not LED_IS_ON
                data.write(f'{time.time():1.0f} {LED_IS_ON}\n')
                if DEBUG:
                    print("Led is on: {LED_IS_ON}")
        else:
            GPIO.output(LED_PIN, False)
GPIO.cleanup()
