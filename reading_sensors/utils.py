
#from bme280pi import Sensor
import datetime
from math import ceil

import time

#isRaining = InputDevice(18)

#sensor = Sensor(address=0x76) !or 0x77

class Average_state_class : 
     def __init__(self,  temperature, humidity, pressure, rain, time):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
        self.time = time
    

def extractBME():
    try :
        sensor_data = sensor.get_data()
        result = sensor_data
    except Exception as arg:
         print("Something's wrong with the BME sensor : \n", arg)
         result = [0, 0, 0]
    return result

def determineRainState(): 
    try:
        if isRaining.is_active:
            print("It's raining")
            return True
        else :
            return False
    except Exception as arg : 
        print("Something's wrong with the rain sensor : \n", arg)
        return "unknown"
    
def extractTime(): 
    currentTime = datetime.datetime.now()
    result = currentTime.strftime("%Y-%m-%d %H:%M:%S")
    return result

def average_states(arr):
    #it takes 1 second
    print(time.time())
    current_average = {}

    current_sum_temp = 0
    current_sum_press = 0
    current_sum_hum = 0
    current_sum_rain = 0

    i = 0

    for obj in arr :

        if(obj == 0) :
            continue
        current_sum_temp += int(obj.temperature)
        current_sum_press += int(obj.pressure)
        current_sum_hum += int(obj.humidity)
        current_sum_rain += int(obj.rain)

        if(i  == 9) :
            count = len(arr) - 1
            t = ceil(current_sum_temp / count)
            h =  ceil(current_sum_hum / count)
            p =  ceil(current_sum_press / count)
            r =  ceil(current_sum_rain / count)

            current_time = extractTime()
            current_average =  Average_state_class(t, h, p, r, current_time)

        else :
            i += 1
    print(time.time())
    return  current_average