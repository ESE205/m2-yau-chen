
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep from time module
GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BOARD)   # Use physical pin numbering

ITER_COUNT = 15
INPUT_PIN = 11
LED_PIN = 16
i = 0

GPIO.setup(pin1, GPIO.OUT, initial=GPIO.LOW)   

GPIO.setup(INPUT_PIN,GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT, initial = GPIO.LOW)
while i = 0:
    if !GPIO.input(INTPUT_PIN):
        GPIO.output(LED_PIN, true)
    else:
        GPIO.output(LED_PIN, false)
GPIO.cleanup()
