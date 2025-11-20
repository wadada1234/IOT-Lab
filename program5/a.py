# (A) Flash an LED based on cron output (acts as an alarm)
 PROGRAM
 Python code: blink.py
 import RPi.GPIO as GPIO
 import time
 LedPin = 11 # pin11
 def setup():
 GPIO.setmode(GPIO.BOARD) # Numbers GPIOs by physical location
 GPIO.setup(LedPin, GPIO.OUT) # Set LedPin's mode is output
 GPIO.output(LedPin, GPIO.HIGH) # Turn ON led
 def blink():
 while True:
 GPIO.output(LedPin, GPIO.HIGH) # led on
 time.sleep(1)
 GPIO.output(LedPin, GPIO.LOW) # led off
 time.sleep(1)
 def destroy():
 GPIO.output(LedPin, GPIO.LOW) # led off
 GPIO.cleanup() # Release resource
 if
 name ==' main ': #Programstart from here
 setup()
 try:
 blink()
 except KeyboardInterrupt: # When 'Ctrl+C' is pressed, the child program destroy()
 will be executed.
 destroy()