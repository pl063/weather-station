[![Maintainability](https://api.codeclimate.com/v1/badges/c1713fd96a5aaa62b9a5/maintainability)](https://codeclimate.com/github/pl063/weather-station/maintainability)

# Weather station
You can remotely monitor the state of temperature, humidity, air pressure in your home using this Weather station, built with Raspberry Pi 4 and sensors. Thanks to its GUI this system, you can always view the logs in the database. 

## Wiring up the stations components
<a href="url"><img src="/media/weather_station_beta_bb.png" align="center" height="450px" width="300px" ></a>

| Device | Device Pins    | Raspberry Pins    |
| :--   | :-- | :-- |
|BME280|   |   |
|  | VCC  | GPIO 17   |
|  | GND  | GND   |
|  | SDA  | SDA   |
|  | SCL  | SCL   |
|YL-83 control board|   |   |
|  | VCC  | +5V   |
|  | GND  | GND   |
|  | AO  | x   |
|  | DO  | GPIO 18   |
|RGB led|   |   |
|  | Cathode  | GND   |
|  | Red  | GPIO 13   |
|  | Blue  | GPIO 12   |
|  | Green  | GPIO 19   |
|RTC|   |   |
|  | VCC  | +3.3V   |
|  | GND  | GND   |
|  | SDA  | SDA   |
|  | SCL  | SCL   |
|  | NC  | x   |
|EEPROM|   |   |
|  | VCC  | +5V   |
|  | GND  | GND   |
|  | SDA  | ID_SC   |
|  | SCL  | ID_SD   |
|  | WP  | GND   |


# Database setup
For this project, I use the MongoDB cluster. It consists of several collections: "current-days", "current_weeks" and "current_months". 
The collection names follow Mongo convention for naming.

This current version of Viper - v.0.0 - uses only "current-days" for storing entries for the day and "current-weeks" for migrating data objects from "current-days" at 0.00hrs his every day.

The data schema has the following properties: 
- temperature - type Number, rounded up
- humidity  - type Number, rounded up
- pressure - as the above
- rain -  type Number 1 or 0. representing true or false 
- created_at - timestamp

# Reading sensors

BME280 uses the I^2C  protocol for communication. The default address may be 0x77 or 0x76. The protocol must to be enabled on the Raspberry Pi 4. To check the used addresses, run the terminal command tools "sudo i2cdetect -y 1". You may need to install  I^2C tools first.

I use the open-source Python library "bme280pi" to retrieve the sensors output.

Since this sensor sometimes may disappear from I²C addresses, it has to restart occasionally. That is why its power source is connected to a GPIO pin.

YL-83 control board returns digital output, it is connected to a GPIO pin.

Cron jobs are important for the station's functionality. To use them, add these to “crontab -e” (*WITHOUT* sudo):

@reboot python3 /path_to/main_weather.py 

0 1 * * * sudo reboot

# Web GUI 
It is based on ExpressJS and HandlebarsJS. It consists of server-side services and web client. You need to start the "index.js" file with node. For the best performance, use the "nodemon” package. The "Morgan" logger logs into the terminal each request to the server, the time for the response, and the response code.

The Web GUI is *not* ran on the microcontroller, only the code in the directory, named "reading-sensors".

# Viper HAT
I used utils (https://github.com/raspberrypi/utils) eeptools for flashing the eeprom image.

# This project comes with NO WARRANTY.
