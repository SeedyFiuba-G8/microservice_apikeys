from pymongo import MongoClient
import os

password = os.getenv('ADMIN_PASSWORD')


def main():
    db_name = input('database: ')
    collection = input('collection: ')

    client: MongoClient = MongoClient(
        f"mongodb+srv://admin:{password}@cluster.wbauf.mongodb.net/?retryWrites=true&w=majority")

    db = client[db_name]

    if input(f"Are you sure you want to clear {db_name}.{collection}? [y/n] ").lower() != 'y':
        return

    db[collection].delete_many({})


if __name__ == '__main__':
    main()
