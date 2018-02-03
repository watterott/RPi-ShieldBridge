import time
import RPi.GPIO as GPIO
import pyfirmata

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)   # GPIO18 output
GPIO.output(12, GPIO.LOW)  # GPIO18 low -> Arduino reset off

# start connection to Arduino
#  USB: /dev/ttyUSB0 or /dev/ttyACM0
#  UART: /dev/ttyAMA0
board = pyfirmata.Arduino('/dev/ttyAMA0')

board.digital[13].write(1) # switch on LED
time.sleep(3)              # 3s delay
board.digital[13].write(0) # switch off LED
time.sleep(3)              # 3s delay
board.exit()
