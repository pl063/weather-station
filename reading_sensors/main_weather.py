# Import libraries:
import bme280
import smbus2
#raindrop sensor DO connected to GPIO18


import datetime
from time import sleep
from pprint import pprint

from utils import extractBME, determineRainState, extractTime

port = 1
address = 0x77 #! Adafruit BME280 address. Other BME280s may be different 
bus = smbus2.SMBus(port)



bme280.load_calibration_params(bus,address)

class Current_state_class : 
     def __init__(self, time,  temperature, humidity, pressure, rain):
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
    
  
def main():
   #Get current time
    time = extractTime()
    #print(time)
    weatherList = extractBME()
    rainFlag = determineRainState()
    current_state = Current_state_class(time, weatherList[0], weatherList[1], weatherList[2], rainFlag)
    res = vars(current_state)
    pprint(res)
    #write values in current object
    current_state = Current_state_class(time, weatherList[0], weatherList[1], weatherList[2], rainFlag)
    #Print object in readable format
    res = vars(current_state)
    pprint(res)
    return current_state



while True:
    try:
        main()
    except Exception as argument: #Main error handling for any kind of error
        print("Seems like error ocurred. Here's what happened : \n", argument)
    sleep(1)






#################################


    

    
