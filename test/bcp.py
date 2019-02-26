from mcp3208 import MCP3208
import spidev


import time

adc = MCP3208()
cn = 1
while True:
    print (str(cn)+"adc env",adc.read(5))
    time.sleep(.1)
    cn += 1
