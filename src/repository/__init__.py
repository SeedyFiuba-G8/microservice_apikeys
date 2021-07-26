from pymongo import MongoClient

from config import config


def get_db_client() -> MongoClient:
    client = MongoClient(
        "mongodb+srv://" + config.DB_USER + ":" +
        config.DB_PASSWORD + "@cluster.wbauf.mongodb.net/" +
        config.DB_DATABASE + "?retryWrites=true&w=majority"
    )
    return client
