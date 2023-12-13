from pymongo import MongoClient
import logging
from utils import extractTime

def connect_database():
    try:
        client = MongoClient(
                        tls=True,
                        tlsCertificateKeyFile='/home/viper/weather-station/reading_sensors/cert.pem',
                            )
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        logging.critical("<<db" + extractTime(), e)
        pass
