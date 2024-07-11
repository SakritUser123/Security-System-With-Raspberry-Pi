import RPi.GPIO as GPIO
import time
import pyttsx3

engine = pyttsx3.init()
volume = engine.getProperty('volume')
engine.setProperty('volume',volume + 2)
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
        engine.say('what is the password it is five digits')
        engine.runAndWait()
        id = int(input(''))
     
        if id != 12345:
            engine.say('wrong password')
            engine.runAndWait()
        else:
            engine.say('correct password')
            engine.runAndWait()
            raise SystemExit
            break

def final():
    
    GPIO.output(BeepPin,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(BeepPin,GPIO.LOW)


# If run this script directly, do:


main()
engine.say('final try what is password')
engine.runAndWait()
id = int(input(''))
if id != 12345:
    try:
        final()
    except KeyboardInterrupt:
        destroy()
    # When 'Ctrl+C' is pressed, the program
    # destroy() will be  executed.
