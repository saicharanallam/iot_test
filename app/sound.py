import time
import random
from gpiozero import LED,Buzzer
import RPi.GPIO as GPIO


led = LED(17)
channel = 11
led.on()
time.sleep(1)
led.off()

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

# def callback(self):
#     if GPIO.input(channel):
#         print("sound detected")
#     else:
#         print("Sound detected")

# GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)
# GPIO.add_event_callback(channel, callback)

while True:
    if GPIO.input(channel):
        print("sound detected")
    else:
        print("Sound  not detected")
    time.sleep(2)
# while True:
	
# 	for i in range (10):
# 		led.on()
# 		buz.off()
# 		time.sleep(random.choice(foo))
# 		led.off()
# 		buz.on()
# 		time.sleep(random.choice(foo))
# 	led.off()
# 	time.sleep(random.choice(foo))

