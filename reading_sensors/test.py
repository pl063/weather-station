#Test functions without sensors and board
from pprint import pprint

from utils import average_states
timer = 60


class Current_state_class : 
     def __init__(self,  temperature, humidity, pressure, rain):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.rain = rain
    
 
def main(arr):
 
   weather_arr = [0] #default arr[0] = 0 to calculate length 
   #Get current time
   while True:

    try:
      for el in arr:
        current_state = Current_state_class(el[0], el[1], el[2], el[3])

        weather_arr.append(current_state)

        if(len(weather_arr) == 11):
          print("We have 10 states now, let's find the average")
          try :
              t = average_states(weather_arr)
              weather_arr = []
              pprint(vars(t))
          except Exception as arg:
              print(arg)


    except Exception as Argument: #Write the type of error it's supposed to handle or leave () blank for any error

        print('Error is: \n', Argument)
    


    return 



main([
[10, 20, 30, 0],
[30, 25, 40, 1],
[36, 21, 20, 0],
[33, 22, 14, 1],
[12, 32, 20, 1],
[2, 0, 1, 0],
[5, 15, 26, 0],
[15, 90, 25, 1],
[27, 34, 22, 0],
[39, 90, 100, 0],
[25, 18, 30, 0],
[10, 20, 30, 0],
[30, 25, 40, 1],
[36, 21, 20, 0],
[33, 22, 14, 1],
[12, 32, 20, 1],
[2, 0, 1, 0],
[5, 15, 26, 0],
[15, 90, 25, 1],
[27, 34, 22, 0],

])
