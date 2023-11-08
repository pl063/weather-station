from pymongo import MongoClient
def get_database():
try:
    client = MongoClient(uri,
                     tls=True,
                        tlsCertificateKeyFile='./cert.pem',
                        )
    print("Pinged your deployment. You successfully connected to MongoDB!")
    mydb = client["weather-station"]
    mydb.createCollection("entries")

    collist = mydb.list_collection_names()
if "entries" in collist:
        print("The collection exists.")
except Exception as e:
    print(e)
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()