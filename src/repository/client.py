from pymongo import MongoClient

from src.config import config


async def get_db_client() -> MongoClient:
    client = MongoClient(
        "mongodb+srv://" + config.DB_USER + ":" +
        config.DB_PASSWORD + "@cluster.wbauf.mongodb.net/?retryWrites=true&w=majority"
    )
    return client
