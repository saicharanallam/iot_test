#!/usr/bin/env python

from mcp3208 import MCP3208
import time
import I2C_LCD_driver


adc = MCP3208()
mylcd = I2C_LCD_driver.lcd()


# below is taken from adafruit's MCP3008 10b ADC python driver
print('Reading MCP3208 values, press Ctrl-C to quit...')
# Print nice channel column headers.
# print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
# print('-' * 57)
# Main program loop.mc
while True:
    # Read all the ADC channel values in a list.
    buffer_reading = 0
        # The read_adc function will get the value of the specified channel (0-7).
    for j in range(4):
        buffer_reading += adc.read(1)
        time.sleep(0.2)
        print (adc.read(1))
    sensor_reading = buffer_reading / 4
    if sensor_reading <= 95:
        mylcd.lcd_clear()
        mylcd.lcd_display_string('Sound < 70dB', 1)
        print("Sound < 70dB")
    elif sensor_reading > 95:
        dB_reading = (((sensor_reading - 95) // 2) * .192) + 70
        mylcd.lcd_clear()
        mylcd.lcd_display_string('Sound = {}dB'.format(dB_reading), 1)
        print("Sound = {}dB".format(dB_reading))

    # Print the ADC values.
    # print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # print('| {0:>4} |'.format(dB_reading))
    # Pause for half a second.
    time.sleep(0.3)
