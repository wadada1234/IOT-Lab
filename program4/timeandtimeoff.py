#(c ) Flash an LED at a given on time and off time cycle, where the two times are taken from a file.
 # (c) Flash an LED with on/off times read from a file (times.txt).
import time

# Safe import for development on non-Raspberry Pi systems
try:
    import RPi.GPIO as GPIO
except (ImportError, RuntimeError):
    from unittest import mock
    GPIO = mock.MagicMock()
    GPIO.BOARD = 'BOARD'
    GPIO.OUT = 'OUT'
    GPIO.HIGH = True
    GPIO.LOW = False

LED_PIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED_PIN, GPIO.OUT)

def read_times(path="times.txt"):
    """Read two floats (on_time, off_time) from a file. One value per line or space-separated.
    Returns default (1.0, 1.0) on error."""
    try:
        with open(path, "r") as f:
            parts = f.read().strip().split()
            if len(parts) >= 2:
                return float(parts[0]), float(parts[1])
            elif len(parts) == 1:
                t = float(parts[0])
                return t, t
    except Exception:
        pass
    return 1.0, 1.0

if __name__ == "__main__":
    on_time, off_time = read_times()
    print(f"Using on_time={on_time}s, off_time={off_time}s (edit times.txt to change)")

    try:
        while True:
            GPIO.output(LED_PIN, GPIO.HIGH)  # LED on
            time.sleep(on_time)
            GPIO.output(LED_PIN, GPIO.LOW)   # LED off
            time.sleep(off_time)
    except KeyboardInterrupt:
        print("Interrupted by user, exiting.")
    finally:
        GPIO.output(LED_PIN, GPIO.LOW)
        GPIO.cleanup()