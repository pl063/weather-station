from gpiozero import InputDevice

import datetime

isRaining = InputDevice(18)

def extractBME():
    result = []
    try :
        bme280_data = bme280.sample(bus,address)
        current_humidity  = bme280_data.humidity
        current_pressure  = bme280_data.pressure
        current_temperature = bme280_data.temperature
        result = [ current_temperature, current_humidity, current_pressure]
    except Exception as arg:
         print("Something's wrong with the BME sensor : \n", arg)
         result = ["unknown", "unknown", "unknown"]
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