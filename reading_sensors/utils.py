
from bme280pi import Sensor
from gpiozero import InputDevice
import datetime
from math import ceil


isRaining = InputDevice(18) # 1 if it's not raining, 0 if it's raining

sensor = Sensor(address=0x77) 

class Average_state_class : 
     def __init__(self,  temperature, humidity, pressure, rain, time):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
        self.time = time
    

def extractBME():
    try :
        result = []
        result.append(ceil(sensor.get_temperature()))
        result.append(ceil(sensor.get_humidity()))
        result.append(ceil(sensor.get_pressure()))
    except Exception as arg:
         print("Something's wrong with the BME sensor : \n", arg)
         result = [0, 0, 0]
    return result

def determineRainState(): 
    try:
        result = isRaining.value
        if (result == 1):
            return 0
        else: 
            return 1
    except Exception as arg : 
        print("Something's wrong with the rain sensor : \n", arg)
        return "unknown"
    
def extractTime(): 
    currentTime = datetime.datetime.now()
    result = currentTime.strftime("%Y-%m-%d %H:%M:%S")
    return result

def average_states(arr):

    current_average = {}

    current_sum_temp = 0
    current_sum_press = 0
    current_sum_hum = 0
    current_sum_rain = 0

    i = 0

    for obj in arr :

        if(obj == 0) :
            continue
        current_sum_temp += obj.temperature
        current_sum_press += obj.pressure
        current_sum_hum += obj.humidity
        current_sum_rain += obj.rain

        if(i  == 1) :
            count = len(arr)
            t = ceil(current_sum_temp / count)
            h =  ceil(current_sum_hum / count)
            p =  ceil(current_sum_press / count)
            r =  ceil(current_sum_rain / count)

            current_time = extractTime()
            current_average =  Average_state_class(t, h, p, r, current_time)

        else :
            i += 1

    return  current_average