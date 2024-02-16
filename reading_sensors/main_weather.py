#!/usr/bin/env python3

# Raindrop sensor IS connected to GPIO18
# Bme280 sensor IS connected to SDA, SCL, GPIO17 (+) and GND

from time import sleep
import os
import sys
import datetime
from pprint import pprint
import logging

#logger setup
logging.basicConfig(filename="main_weather.log", encoding="utf-8", level=logging.DEBUG)

from utils import extract_BME, average_states, determine_rain_state, extract_time, restart_os
from api import insert_current_state
from cron_migrate_collection import main_migration

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
    current_time = datetime.datetime.now()
    flag = flags[len(flags) - 1]
    logging.info("The current flag is " + str(flag))
    if (current_time.hour == 0 and flag == False): 
        #it is midnight, perform migration
        logging.info("Calling main migration function")
        main_migration()
        flags.append(True)
        restart_os()
        
    logging.info("Main weather is running " + extract_time())
    weather_list = extract_BME()
    rain_flag = determine_rain_state()
    #write values in current object
    current_state = Current_state_class(weather_list[0], weather_list[1], weather_list[2], rain_flag)
    #Print object in readable format
    #res = vars(current_state)
    #pprint(res)
     
    #add state to the cache array
    weather_arr.append(current_state)

    if(len(weather_arr) == average_counter):
          logging.info("Averagazing 10 states" + extract_time())
          try :
              t = average_states(weather_arr, average_counter) #averagize the states
              weather_arr.clear()
              #pprint(vars(t))
              logging.info("Averagized done " + extract_time())
              insert_current_state(t.__dict__)
              logging.info("api finished " + extract_time())
          except Exception as arg:
              logging.error(extract_time(), arg)
              pass
    return 


#main loop 

while True:
    try:
        led_output("uploading")
        main()
    except Exception as argument: #Main error handling for any kind of error
        logging.info("Seems like error ocurred. Here's what happened : \n" + extract_time(), argument)
        os.execv(sys.argv[0], sys.argv) #restart the script
       
    sleep(timer)
