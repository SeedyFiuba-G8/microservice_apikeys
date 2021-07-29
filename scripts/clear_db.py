from pymongo import MongoClient
import os

password = os.getenv('ADMIN_PASSWORD')
database = os.getenv('DATABASE')


def main():

    client: MongoClient = MongoClient(
        f"mongodb+srv://admin:{password}@cluster.wbauf.mongodb.net/?retryWrites=true&w=majority")

    db = client[database]

    if input(f"Are you sure you want to clear collections on {database}? [y/n] ").lower() != 'y':
        return

    db['keys'].delete_many({})
    db['defaultkeys'].delete_many({})


if __name__ == '__main__':
    main()
