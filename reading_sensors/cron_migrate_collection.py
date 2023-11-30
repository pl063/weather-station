#cron job to migrate all entries of col1 to col2 at midnight additional settings are required in OS

from pymongo import MongoClient

uri = "mongodb+srv://weather-station.lllcyel.mongodb.net/Weather?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"


def migrateToCol (col1, col2) :
        myList=list(col1.find({}))
        col2.insert_many(myList)


try:
        client = MongoClient(uri,
                        tls=True,
                        tlsCertificateKeyFile='/home/viper/weather-station/reading_sensors/cert.pem',
                        )
        print("You successfully connected to MongoDB!")

        mydb = client["Weather"]
        col1 = mydb["current_days"]
        col2 = mydb["current_weeks"]

        x = migrateToCol(col1, col2)
        #print(x)
        col1.delete_many({})
       
except Exception as e:
        print(e)