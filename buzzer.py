import RPi.GPIO as GPIO
import time

# Set #17 as buzzer pin
BeepPin = 26


    # Set the GPIO modes to BCM Numbering
GPIO.setmode(GPIO.BCM)
    # Set LedPin's mode to output,
    # and initial level to High(3.3v)
GPIO.setup(BeepPin,GPIO.OUT,initial = GPIO.LOW)
def destroy():
    # Turn off buzzer
    GPIO.output(BeepPin, GPIO.HIGH)
    # Release resource
    GPIO.cleanup()
def main():
    for i in range(2):
        id = int(input('what is the password, it is five digits'))
        if id != 12345:
            print('Wrong password Try again')
        else:
            print('correct password')
            raise SystemExit

            break

def final():
    GPIO.output(BeepPin,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(BeepPin,GPIO.LOW)


# If run this script directly, do:


main()

id = int(input('final try what is password'))
if id != 12345:
    try:
        final()
    except KeyboardInterrupt:
        destroy()
    # When 'Ctrl+C' is pressed, the program
    # destroy() will be  executed.

