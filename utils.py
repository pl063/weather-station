
import datetime



def extractBME( current_humidity, current_pressure, current_temperature ):
    #bme280_data = bme280.sample(bus,address)
    #current_humidity  = bme280_data.humidity
    #current_pressure  = bme280_data.pressure
    #current_temperature = bme280_data.temperature
    #print(humidity, pressure, ambient_temperature)
    return [ current_temperature, current_humidity, current_pressure]

def extractTime(): 
    currentTime = datetime.datetime.now()
    result = currentTime.strftime("%Y-%m-%d %H:%M:%S")
    return result