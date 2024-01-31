# Weather station
You can remotely monitor the state of temperature, humidity, air pressure in your home using this Weather station, built with Raspberry Pi 4 and sensors. Thanks to its GUI this system, you can always view the logs in the database. 

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
@reboot python main weather.py 
1.0.0.0 python cron_migration. py

# Web GUI 
It is based on ExpressJS and HandlebarsJS. It consists of server-side services and web client. You need to start the "index.js" file with node. For the best performance, use the "nodemon” package. The "Morgan" logger logs into the terminal each request to the server, the time for the response, and the response code.

The Web GUI is *not* ran on the microcontroller, only the code in the directory, named "reading-sensors".

# This project comes with NO WARRANTY.
