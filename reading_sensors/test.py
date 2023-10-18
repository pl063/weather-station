#Test functions without sensors and board
from pprint import pprint

from utils import extractBME, extractTime

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
    print(time)
    #print(time.strftime("%X"))
    weatherList = extractBME(100, 200, 300)
   # rainFlag = determineRainState()
    rainFlag = True
    #write values in current object
    current_state = Current_state_class(time, weatherList[0], weatherList[1], weatherList[2], rainFlag)
    #Print object in readable format
    res = vars(current_state)
    pprint(res)
    return 

main()