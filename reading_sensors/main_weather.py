# Import libraries:
#import bme280
#import smbus2
# raindrop sensor DO connected to GPIO18
#from gpiozero import InputDevice

import datetime
from time import sleep
from pprint import pprint

port = 1
address = 0x77 #! Adafruit BME280 address. Other BME280s may be different 
bus = smbus2.SMBus(port)
isRaining = InputDevice(18)

bme280.load_calibration_params(bus,address)

class Current_state_class : 
     def __init__(self, time,  temperature, humidity, pressure, rain):
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
    
    
#Function extractBME() to extract values from BME280
def extractBME():
    bme280_data = bme280.sample(bus,address)
    current_humidity  = bme280_data.humidity
    current_pressure  = bme280_data.pressure
    current_temperature = bme280_data.temperature
    #print(humidity, pressure, ambient_temperature)
    return [ current_temperature, current_humidity, current_pressure]

def determineRainState(): 
    if isRaining.is_active:
        print("It's raining")
        return True
    else :
        return False
    
def extractTime(): 
    currentTime = datetime.datetime.now()
    result = currentTime.strftime("%Y-%m-%d %H:%M:%S")
    return result

  
def main():
   #Get current time
    time = extractTime()
    print(time)
    weatherList = extractBME()
    rainFlag = determineRainState()
    #write values in current object
    current_state = Current_state_class(time, weatherList[0], weatherList[1], weatherList[2], rainFlag)
    #Print object in readable format
    #res = vars(current_state)
    #pprint(res)
    return current_state



while True:
    main()
    sleep(1)






#################################


    

    
