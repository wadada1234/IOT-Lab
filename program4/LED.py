# (a) Light an LED through Python program.

# ...existing code...
import RPi.GPIO as GPIO
import time

LED_PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    print("LED on")
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(LED_PIN, GPIO.LOW)
finally:
    GPIO.cleanup()
# ...existing code...