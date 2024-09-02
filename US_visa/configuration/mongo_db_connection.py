import sys
from US_visa.exception import USvisaException
from US_visa.logger import logging
import os
from US_visa.constants import DATABASE_NAME
import pymongo
import certifi
import urllib.parse

ca = certifi.where()

class MongoDBClient:
    """
    Class Name :   export_data_into_feature_store
    Description :   This method exports the dataframe from mongodb feature store as dataframe 
    
    Output      :   connection to mongodb database
    On Failure  :   raises an exception
    """
    client = None

    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                username = urllib.parse.quote_plus("shashank")
                password = urllib.parse.quote_plus("jushank@2021")
                mongo_db_url = f"mongodb+srv://{username}:{password}@cluster0.toshy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
            logging.info("MongoDB connection successful")
        except Exception as e:
            raise USvisaException(e, sys)
