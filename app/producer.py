import socket

HOST = "0.0.0.0"
PORT = 65432





import Adafruit_DHT
import time, datetime
from threading import Thread
from multiprocessing import Process
from gpiozero import LED,Buzzer
import I2C_LCD_driver


buz = Buzzer(14)
led = LED(17)
mylcd = I2C_LCD_driver.lcd()
sensor = Adafruit_DHT.DHT22


#mylcd.lcd_display_string("Hello World!", 1)
#mylcd.lcd_display_string("this is cool!", 2)


# gp.setwarnings(False)
# gp.setmode(gp.BOARD)
# gp.setup(7,gp.OUT)
# gp.output(7,1)

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.

# Example using a Beaglebone Black with DHT sensor
# connected to pin P8_11.
#pin = 'P8_11'

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
pin = 23

temp_limit = 28
humid_limit = 60

def beeper(humidiy,temperature):
    buz.on()
    led.on()
    time.sleep(1)
    buz.off()
    led.off()
    # if humidity >= humid_limit:
    #     print("Humidity is more!!")
    #     mylcd.lcd_display_string("Humid is more!!", 2)

    # if temperature >= temp_limit:
    #     print("Temperature is more!!")
    #     mylcd.lcd_display_string("Temp is more!!  ", 1)


# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
tick = False

value1 = {"_time":datetime.datetime.now(), "temp":0, "humidity":0}
value2 = {"_time":datetime.datetime.now(), "temp":0, "humidity":0}

while True:
    tick = False if tick == True else True
    print(tick)
    time1 = datetime.datetime.now(); humidity, temperature = Adafruit_DHT.read_retry(sensor, pin); time2 = datetime.datetime.now()
    #print(time.ctime())
    data = {"_time":time1 + ((time2-time1)/2), "temp":round(temperature,2), "humidity":round(humidity,2)}
    value1 = data if tick == True else value1
    value2 = data if tick == False else value2
    if value1['temp'] != value2['temp'] or value1['humidity'] != value2['humidity']:
        print("Not same")
    else:
        print("Same")
    if humidity is not None and temperature is not None:
        print(data)#mylcd.lcd_clear()
        #mylcd.lcd_display_string('Temp = {0:0.1f} C'.format(temperature), 1)
        #mylcd.lcd_display_string('Humid = {0:0.1f} %'.format(humidity), 2)

        #if humidity >= humid_limit:
            #print("Humidity is more!!")
            #mylcd.lcd_display_string("Humid is more!!", 2)

        #if temperature >= temp_limit:
            #print(Temperature is more!!")
            #mylcd.lcd_display_string("Temp is more!!  ", 1)


        #print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        #if (humidity >= humid_limit) | (temperature >= temp_limit):
            #Process(target=beeper,args=(humidity,temperature)).start()
        # if temperature >= 25:
        #     Thread(target=beeper).start()
    else:
    		print('Failed to get reading. Try again!')
    time.sleep(1)

