
from bme280pi import Sensor
from gpiozero import InputDevice
import datetime
import time
from bson.timestamp import Timestamp
from math import ceil
import RPi.GPIO as GPIO
import os
import sys
import logging
#logging.basicConfig(filename="utils.log", encoding="utf-8", level=logging.DEBUG)

from led_output import led_output

def extract_time(): 
    current_time = datetime.datetime.now()
    result = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return result


is_raining = InputDevice(18) # 1 if it's not raining, 0 if it's raining
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.HIGH)
try:
    sensor = Sensor(address=0x76) 

except Exception as arg:
   logging.critical("Something's wrong with the BME sensor : \n" + extract_time(), arg)
   logging.info('restarting sensor... changing address' + extract_time())
   GPIO.output(17, GPIO.LOW)
   time.sleep(3)
   GPIO.output(17, GPIO.HIGH)
   time.sleep(5)
   try:
        sensor = Sensor(address=0x77) 
   except Exception as arg:
        logging.info("Restarting didn't help :( \n" + extract_time(), arg)
        os.execv(sys.argv[0], sys.argv) #restart the script
#led_output("uploading")

class Average_state_class : 
     def __init__(self,  temperature, humidity, pressure, rain, created_at):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
        self.created_at = created_at

def extract_BME():
    try :
        result = []
        result.append(ceil(sensor.get_temperature()))
        result.append(ceil(sensor.get_humidity()))
        result.append(ceil(sensor.get_pressure()))
    except Exception as arg:
         logging.info("Something's wrong with the BME sensor : \n" + extract_time(), arg)
         logging.info('restarting sensor...' + extract_time())
         GPIO.output(17, GPIO.LOW)
         time.sleep(3)
         GPIO.output(17, GPIO.HIGH)
         time.sleep(5)
         result = [0, 0, 0]
    return result

def determine_rain_state(): 
    try:
        result = is_raining.value
        if (result == 1):
            return 0
        else: 
            return 1
    except Exception as arg : 
        logging.error("Something's wrong with the rain sensor : \n" + extract_time(), arg)
        return "unknown"
    

def average_states(arr, counter):

    current_average = {}

    current_sum_temp = 0
    current_sum_press = 0
    current_sum_hum = 0
    current_sum_rain = 0

    i = 0

    try:
        for obj in arr :

            if(obj == 0) :
                continue
            current_sum_temp += obj.temperature
            current_sum_press += obj.pressure
            current_sum_hum += obj.humidity
            current_sum_rain += obj.rain

            if(i + 1  == counter) :
                count = len(arr)
                t = ceil(current_sum_temp / count)
                h =  ceil(current_sum_hum / count)
                p =  ceil(current_sum_press / count)
                r =  ceil(current_sum_rain / count)
                timestamp = Timestamp(int(datetime.datetime.today().timestamp()), 1)
                current_average =  Average_state_class(t, h, p, r, timestamp.time)

            else :
                i += 1

        return  current_average
    except Exception as err:
        logging.critical( "<<utils" + extract_time(), err)
        pass

def restart_os() :
    logging.info("Restarting OS" + extract_time())
    os.system("shutdown /r /t 0")
    
