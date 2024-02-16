#Post sensor data to Mongo database

from pymongo import MongoClient
import logging
logging.basicConfig(filename="main_weather.log", encoding="utf-8", level=logging.DEBUG)


from led_output import led_output
from utils import extract_time


uri = "mongodb+srv://weather-station.lllcyel.mongodb.net/Weather?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
#connect with Mongo

try:
        client = MongoClient(uri,
                        tls=True,
                        tlsCertificateKeyFile='/home/viper/weather-station/reading_sensors/cert.pem',
                        )
        logging.info("Pinged your deployment. You successfully connected to MongoDB!" + "<<api" + extract_time())

        db = client["Weather"]
        
       
except Exception as e:
        logging.error( "<<api" + extract_time(), e)
        pass


def insert_current_state(state):
    try:
           led_output("uploading")
           logging.info( "<<api RUNNING" + extract_time())
           col = db["current_days"]
           x = col.insert_one(state)
          # print(state)
           logging.info( "<<api Uploading" + extract_time())
           led_output("success")
           print(x.inserted_id)
           logging.info( "<<api Uploaded" + extract_time())
    except Exception as err:
           logging.error( "<<api" + extract_time(), err)
           pass

