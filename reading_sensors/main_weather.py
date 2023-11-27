# Import libraries:
#raindrop sensor DO connected to GPIO18

from time import sleep
from pprint import pprint

from utils import extractBME, average_states, determineRainState
from api import insert_current_state

#array with current state to cache
weather_arr = []
timer = 10 #sleep timer for main loop in seconds
average_counter = 2 #how many objects should be averaged

class Current_state_class : 
     def __init__(self,  temperature, humidity, pressure, rain):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
    
  
def main():

    weatherList = extractBME()
    rainFlag = determineRainState()
    #write values in current object
    current_state = Current_state_class(weatherList[0], weatherList[1], weatherList[2], rainFlag)
    #Print object in readable format
    #res = vars(current_state)
    #pprint(res)
    #add state to the array
    weather_arr.append(current_state)

    if(len(weather_arr) == average_counter):
          print("We have 10 states now, let's find the average")
          try :
              t = average_states(weather_arr)
              weather_arr.clear()
              #pprint(vars(t))
              insert_current_state(t.__dict__)
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


    

    
