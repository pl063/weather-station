#Post sensor data to Mongo database

from pymongo import MongoClient

#connect with Mongo
from pymongo_get_database import get_database

dbname = get_database()
collection_name = dbname["user_1_items"]
