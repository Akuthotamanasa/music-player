import pymongo
import certifi
from dotenv import load_dotenv
import os
load_dotenv()

class Connection :
    def __init__(self) -> None:
        pass
    
    def _connection():
        url = os.getenv("connection_url")
        Client = pymongo.MongoClient(url, tls=True, tlsCAFile=certifi.where())
        db = Client["musicplayer"]
        collection = db['musicplayer']
        
        return collection

if __name__ == "__main__" :
      Connection()