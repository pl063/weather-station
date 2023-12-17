# Import libraries:
#raindrop sensor DO connected to GPIO18

from time import sleep
import datetime
from pprint import pprint
import logging

#logger setup
logging.basicConfig(filename="main_weather.log", encoding="utf-8", level=logging.DEBUG)

from utils import extractBME, average_states, determineRainState, extractTime
from api import insert_current_state
from cron_migrate_collection import mainMigration

from led_output import led_output

#array with current state to cache
weather_arr = []
timer = 60 #sleep timer for main loop in seconds
average_counter = 10 #how many objects should be averaged

class Current_state_class : 
     def __init__(self,  temperature, humidity, pressure, rain):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
    
  
def main():
    currentTime = datetime.datetime.now()
    print(currentTime.strftime("%H:%M"))
    if (currentTime.strftime("%H:%M") ==  "00:00"): 
        #it is midnight, perform migration
        mainMigration
        
    logging.info("Main weather is running " + extractTime())
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
          logging.info("Averagazing 10 states" + extractTime())
          try :
              t = average_states(weather_arr, average_counter)
              weather_arr.clear()
              #pprint(vars(t))
              insert_current_state(t.__dict__)
          except Exception as arg:
              logging.error(extractTime(), arg)
              pass
    return 


#main loop 
while True:
    try:
        led_output("uploading")
        main()
    except Exception as argument: #Main error handling for any kind of error
        logging.error("Seems like error ocurred. Here's what happened : \n" + extractTime(), argument)
        pass
    sleep(timer)
