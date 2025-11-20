 #(b) Get input from two switches and switch on corresponding LEDs Controlling an LED by a Button.
 # ...existing code...
#!/usr/bin/env python3
# ...existing code...
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# Use two LEDs and two buttons (BOARD numbering)
LED_PINS = [11, 13]   # physical pins for LEDs
BTN_PINS = [12, 16]   # physical pins for buttons

# True means LED is currently off (we initialize outputs HIGH to keep them off
# if the LEDs are wired active-low). Adjust logic if your wiring is different.
led_states = [True, True]

def setup():
    GPIO.setmode(GPIO.BOARD)                 # Numbers GPIOs by physical location
    GPIO.setwarnings(False)
    for lp in LED_PINS:
        GPIO.setup(lp, GPIO.OUT)             # LED as output
        GPIO.output(lp, GPIO.HIGH)           # set LED off (HIGH for active-low wiring)
    for bp in BTN_PINS:
        GPIO.setup(bp, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # button with pull-up

def swLed(channel):
    # Find which button triggered and toggle corresponding LED
    try:
        idx = BTN_PINS.index(channel)
    except ValueError:
        return
    led_states[idx] = not led_states[idx]
    # If using active-low wiring: GPIO.LOW -> ON, GPIO.HIGH -> OFF
    GPIO.output(LED_PINS[idx], GPIO.LOW if not led_states[idx] else GPIO.HIGH)
    print(f"LED {idx+1} {'on' if not led_states[idx] else 'off'}")

def loop():
    # attach event detection for each button (falling edge = press)
    for bp in BTN_PINS:
        GPIO.add_event_detect(bp, GPIO.FALLING, callback=swLed, bouncetime=200)
    try:
        while True:
            time.sleep(1)  # idle, callbacks handle button events
    finally:
        for bp in BTN_PINS:
            GPIO.remove_event_detect(bp)

def destroy():
    # turn LEDs off and cleanup
    for lp in LED_PINS:
        GPIO.output(lp, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Exiting on user interrupt")
    finally:
        destroy()
# ...existing code...