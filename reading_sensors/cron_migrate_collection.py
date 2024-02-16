#cron job to migrate all entries of col1 to col2 at midnight additional settings are required in OS

from pymongo import MongoClient
import logging
logging.basicConfig(filename="main_weather.log", encoding="utf-8", level=logging.DEBUG)

from utils import extract_time
uri = "mongodb+srv://weather-station.lllcyel.mongodb.net/Weather?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"


def migrate_to_col (col1, col2) :
        my_list = list(col1.find({}))
        col2.insert_many(my_list)

def main_migration () :
        try:
                client = MongoClient(uri,
                                tls=True,
                                tlsCertificateKeyFile='/home/viper/weather-station/reading_sensors/cert.pem',
                                )
                #logging.info("Pinged your deployment. You successfully connected to MongoDB!" + "<<cron" + extract_time())
                logging.info("Migrating tool is running" + extract_time())
                db = client["Weather"]
                col1 = db["current_days"]
                col2 = db["current_weeks"]

                x = migrate_to_col(col1, col2)
                #print(x)
                col1.delete_many({})
                logging.info("Migrated" + extract_time())
        except Exception as e:
                logging.info(e)
                pass