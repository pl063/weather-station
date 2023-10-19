#Test functions without sensors and board
from pprint import pprint

from utils import extractBME

class Current_state_class : 
     def __init__(self, time,  temperature, humidity, pressure, rain):
        self.time = time
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
    
 
def main():
   #Get current time
   while True:

    try:

      time = extractTime()
      #print(time)
      #print(time.strftime("%X"))
      weatherList = extractBME(100, 200, 300)
      # rainFlag = determineRainState()
      rainFlag = True
      #write values in current object
      current_state = Current_state_class(time, weatherList[0], weatherList[1], weatherList[2], rainFlag)
      #Print object in readable format
      res = vars(current_state)
      pprint(res)

      break

    except Exception as Argument: #Write the type of error it's supposed to handle or leave () blank for any error

        print('Error is: \n', Argument)
    
    return 

main()