# Import libraries:
#raindrop sensor DO connected to GPIO18

from time import sleep
import time
from pprint import pprint

from utils import extractBME, average_states

#array with current state to cache
weather_arr = []
timer = 1 #sleep timer for main loop in seconds

class Current_state_class : 
     def __init__(self,  temperature, humidity, pressure, rain):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
    
  
def main():

    weatherList = extractBME()
    rainFlag = 0
    #write values in current object
    current_state = Current_state_class(weatherList[0], weatherList[1], weatherList[2], rainFlag)
    #Print object in readable format
    #res = vars(current_state)
    #pprint(res)
    #add state to the array
    weather_arr.append(current_state)

    if(len(weather_arr) == 10):
          print("We have 10 states now, let's find the average")
          try :
              t = average_states(weather_arr)
              weather_arr.clear()
              pprint(vars(t))
          except Exception as arg:
              print(arg)
    return 


#main loop 
while True:
    try:
        main()
    except Exception as argument: #Main error handling for any kind of error
        print("Seems like error ocurred. Here's what happened : \n", argument)
    sleep(timer)






#################################


    

    
