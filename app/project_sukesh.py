# Imports from Python
import time, datetime
from multiprocessing import Process

# Imports for Raspberry Pi
from gpiozero import LED,Buzzer
from picamera import PiCamera, Color
import Adafruit_DHT
import RPi.GPIO as GPIO

# Local file imports
import pressure_sensor
import I2C_LCD_driver


t1 = datetime.datetime.now()

def main():
    dht_pin = 23 # Pin number for DHT sensor
    audio_pin = 11 # Pin number for sound sensor
    buz = Buzzer(14) # Pin number for buzzer
    led = LED(17) # Pin number for LED
    mylcd = I2C_LCD_driver.lcd()
    sensor = Adafruit_DHT.DHT22
    camera = PiCamera()
    camera.rotation = 90
    camera.annotate_background = Color("black")
    camera.resolution = (800, 600) # Max resolution for a picture is (2592, 1944), for video (1920, 1080)
    img_cnt = 0 # Counter for image capture loop
    max_img_cnt = 10 # Maximum count for number of images need to be captured
    path = "/home/pi/iot_test/pic_feed/pic%s.jpg" # Path where pics are saved


    cnt = 1 # Counter for number of readings taken
    temp_limit = 28 # maximum temperature allowed in the room
    humid_limit = 60 # Maximum humidity allowed in the room

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(audio_pin, GPIO.IN)

    def callback(self):
        print("Sound detected @ "+str(time.ctime()))

    def beeper():
        buz.on()
        led.on()
        time.sleep(1)
        buz.off()
        led.off()

    GPIO.add_event_detect(audio_pin, GPIO.BOTH , bouncetime=300)
    GPIO.add_event_callback(audio_pin, callback)

    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, dht_pin)
        pressure = pressure_sensor.pressure_fun() # Function call for pressure
        if humidity is not None and temperature is not None and humidity <= 100:
            mylcd.lcd_clear()
            mylcd.lcd_display_string('Temp = {0:0.1f} C'.format(temperature), 1)
            mylcd.lcd_display_string('Humid = {0:0.1f} %'.format(humidity), 2)
            print(str(cnt)+'. Temp={0:0.1f}*C  Humidity={1:0.1f}% Pressure={2:0.2f}hPa'.format(temperature, humidity, pressure))
            cnt += 1
            camera.annotate_text = time.ctime()
            camera.capture(path%img_cnt)
            img_cnt += 1
            if img_cnt == max_img_cnt:
                img_cnt = 0

            if humidity >= humid_limit:
                print("Humidity is more!!")
                Process(target=beeper).start()
                mylcd.lcd_display_string("Humid is more!!", 2)

            if temperature >= temp_limit:
                print("Temperature is more!!")
                Process(target=beeper).start()
                mylcd.lcd_display_string("Temp is more!!", 1)

        time.sleep(3)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        t2 = datetime.datetime.now()
        td =  t2-t1
        print("Time elapsed: ", td) # This will print the time program has elapsed
