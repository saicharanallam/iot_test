import Adafruit_DHT
import time, datetime
from threading import Thread
from multiprocessing import Process
from gpiozero import LED,Buzzer
import I2C_LCD_driver
from  multiprocessing import Process
from threading import Thread
import sys
import asyncio
import websockets
import time
import json

sensor = Adafruit_DHT.DHT22

pin = 23

IP = '0.0.0.0'
PORT = 8765
li = []

#!/usr/bin/env python

# WS server example for old Python versions

@asyncio.coroutine
def hello(websocket, path):
    try:
        time1 = datetime.datetime.now()
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        time2 = datetime.datetime.now()
        data = {"_time":str(time1 + ((time2-time1)/2)), "temp":\
            round(temperature,2), "humidity":round(humidity,2),\
            "error":None}
        li.append(data)
        if len(li) == 50:
            li.pop(0)
        if humidity is not None and temperature is not None and len(li) != 0:
            yield from websocket.send(li[-1])
            print("Sending Data")
        else:
            print("No data")
    except Exception as error:
        data = {"_time":str(datetime.datetime.now()), "temp":None,\
                    "humidity":None, "error":str(e)}
        yield from websocket.send(data)

@asyncio.coroutine
def send_data(x):
    #websocket = yield from websockets.connect(
        #'ws://' + IP + ':' + str(PORT) + '/')
    try:
        data = json.dumps(x)
        yield from websocket.send(data)
        print(data)

        #echo = yield from websocket.recv()
        #print("< {}".format(echo))
    finally:
        yield from websocket.close()

def run():
    start_server = websockets.serve(hello, IP, PORT)

    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__=='__main__':
    run()
