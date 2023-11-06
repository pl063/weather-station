#Post sensor data to Mongo database

from pymongo import MongoClient

#connect with Mongo
uri = "mongodb+srv://weather-station.lllcyel.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
try:
    client = MongoClient(uri,
                        tls=True,
                        tlsCertificateKeyFile='./cert.pem',
                        )
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)