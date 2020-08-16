import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
print("Setup LED")

GPIO.setup(24, GPIO.OUT)
GPIO.output(24, False)

