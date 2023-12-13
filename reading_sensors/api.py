#Post sensor data to Mongo database

from pymongo import MongoClient
import logging


from led_output import led_output
from utils import extractTime


uri = "mongodb+srv://weather-station.lllcyel.mongodb.net/Weather?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
#connect with Mongo

try:
        client = MongoClient(uri,
                        tls=True,
                        tlsCertificateKeyFile='/home/viper/weather-station/reading_sensors/cert.pem',
                        )
        logging.info("Pinged your deployment. You successfully connected to MongoDB!" + "<<api" + extractTime())

        mydb = client["Weather"]
        
       
except Exception as e:
        logging.error( "<<api" + extractTime(), e)
        pass


def insert_current_state(state):
    try:
           led_output("uploading")
           mycol = mydb["current_days"]
           x = mycol.insert_one(state)
          # print(state)
           logging.info( "<<api Uploading" + extractTime())
           led_output("success")
           print(x.inserted_id)
           logging.info( "<<api Uploaded" + extractTime())
    except Exception as err:
           logging.error( "<<api" + extractTime(), err)
           pass

