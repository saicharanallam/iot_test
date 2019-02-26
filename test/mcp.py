# from mcp3208 import MCP3208


# import time

# adc = MCP3208()

# while True:
#         for i in range(8):
#                 print('ADC[{}]: {:.2f}'.format(i, adc.read(i)))
#         print ("*******************************")
#         time.sleep(4)


# Imports from Python
import time, datetime
from multiprocessing import Process

# Imports for Raspberry Pi
from gpiozero import LED,Buzzer
from picamera import PiCamera, Color
import Adafruit_DHT
import RPi.GPIO as GPIO
from mcp3208 import MCP3208
import time

adc = MCP3208()
samp = []

buz = Buzzer(14) # Pin number for buzzer


def main():

        # buz.on()
    # below is taken from adafruit's MCP3008 10b ADC python driver
        print('Reading MCP3208 values, press Ctrl-C to quit...')
        # Print nice channel column headers.
        print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
        print('-' * 57)
        # Main program loop.
        while True:
        # Read all the ADC channel values in a list.
                values = [0]*8
                for i in range(8):
                        # The read_adc function will get the value of the specified channel (0-7).
                        values[i] = adc.read(i)
                        if i == 1 and values[1] > 120:
                                samp.append(values[1])
                                print(values[1])

                # Print the ADC values.
                # print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
                # Pause for half a second.
                time.sleep(0.2)




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        buz.off() # This will print the time program has elapsed
        c = 0
        print(samp, len(samp))
        for m in samp:
                c += m
        avg = c / len(samp)
        print ("avg reading ", avg)
