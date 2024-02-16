#!/usr/bin/env python3

# Raindrop sensor IS connected to GPIO18
# Bme280 sensor IS connected to SDA, SCL, GPIO17 (+) and GND

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
flags = [False] #check if the collection is already migrated


class Current_state_class : 
     def __init__(self,  temperature, humidity, pressure, rain):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
    
  
def main():
    currentTime = datetime.datetime.now()
    flag = flags[len(flags) - 1]
    logging.info("The current flag is " + str(flag))
    if (currentTime.hour == 0 and flag == False): #check if the current day is over and if the collection is already migrated
        #it is midnight, perform migration
        logging.info("Callig mainMigration function")
        mainMigration()
        flags.append(True)
        
    logging.info("Main weather is running " + extractTime())
    weatherList = extractBME() #extract info from the bme sensor
    rainFlag = determineRainState() #extract info from the rain sensor
    #write values in current object
    current_state = Current_state_class(weatherList[0], weatherList[1], weatherList[2], rainFlag) #generate current state
    #Print object in readable format
    #res = vars(current_state)
    #pprint(res)
     
    #add state to the cache array
    weather_arr.append(current_state)

    if(len(weather_arr) == average_counter):
          logging.info("Averagazing 10 states" + extractTime())
          try :
              t = average_states(weather_arr, average_counter) #averagize the states
              weather_arr.clear()
              #pprint(vars(t))
              logging.info("Averagized done " + extractTime())
              insert_current_state(t.__dict__) #send to the database
              logging.info("api finished " + extractTime())
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
