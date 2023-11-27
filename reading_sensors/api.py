#Post sensor data to Mongo database

from pymongo import MongoClient

from led_output import led_output

uri = "mongodb+srv://weather-station.lllcyel.mongodb.net/Weather?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
#connect with Mongo

try:
        client = MongoClient(uri,
                        tls=True,
                        tlsCertificateKeyFile='/home/viper/weather-station/reading_sensors/cert.pem',
                        )
        print("Pinged your deployment. You successfully connected to MongoDB!")

        mydb = client["Weather"]
        
       
except Exception as e:
        print(e)


def insert_current_state(state):
    try:
           led_output("uploading")
           mycol = mydb["current_days"]
           x = mycol.insert_one(state)
          # print(state)
           led_output("success")
           print(x.inserted_id)
    except Exception as err:
           print(err)
