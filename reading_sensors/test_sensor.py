#Test sensors functionality
#Test BME280 functionality; address may be 0x76 or 0x77
from time import sleep
from bme280pi import Sensor

sensor = Sensor(address=0x76)

while True:
    bme280_data = sensor.get_data()

    print (bme280_data)
    sleep(1)