
from bme280pi import Sensor
import datetime
from math import ceil


#isRaining = InputDevice(18)

sensor = Sensor(address=0x76) 

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

            current_average =  Average_state_class(t, h, p, r)

        else :
            i += 1

    return  current_average