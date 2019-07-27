import RPi.GPIO as GPIO
import time
import signal
import sys
import numpy as np

# use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BCM)

# set GPIO Pins
pinTrigger = 18
pinEcho = 24

def close(signal, frame):
    print("\nTurning off ultrasonic distance detection...\n")
    GPIO.cleanup() 
    sys.exit(0)

def get_Distance():
     # set Trigger to HIGH
    GPIO.output(pinTrigger, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)

    startTime = time.time()
    stopTime = time.time()

    # save start time
    while 0 == GPIO.input(pinEcho):
        startTime = time.time()

    # save time of arrival
    while 1 == GPIO.input(pinEcho):
        stopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = stopTime - startTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance

def getMeanHeight():
    signal.signal(signal.SIGINT, close)

# set GPIO input and output channels
    GPIO.setup(pinTrigger, GPIO.OUT)
    GPIO.setup(pinEcho, GPIO.IN)

    print("Initializing Height scanner")

    heights = []

    for i in range(3):
        get_Distance()
        time.sleep(0.3)

    print("Try to hold the scanner at a level and wait for 5 seconds \n")
    for i in range(5):
        print("Analysing... \n ")
        height = get_Distance()
        heights.append(height)
        time.sleep(1)

    mean_height = np.mean(height)

    print("Scan successful")
    print("Calculated height is : ", mean_height)

    return mean_height