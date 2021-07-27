from pymongo import MongoClient
import os

password = os.getenv('ADMIN_PASSWORD')
database = os.getenv('DATABASE')

defaultkeys = {
    'core': 'SeedyFiubaCore',
    'users': 'SeedyFiubaUsers',
    'sc': 'SeedyFiubaSC',
    'gateway': 'SeedyFiubaApigateway'
}

services = {'core', 'users', 'sc', 'gateway'}


def main():
    client: MongoClient = MongoClient(
        f"mongodb+srv://admin:{password}@cluster.wbauf.mongodb.net/?retryWrites=true&w=majority")

    values = [{'service': service, 'apikey': key} for service, key in defaultkeys.items()]

    db = client[database]

    default_col = db['defaultkeys']
    default_col.insert_many(values)

    service_keys = []
    for owner in services:
        for val in values:
            service_keys.append(
                {'owner': owner, 'service': val['service'], 'apikey': val['apikey']})

    keys = db['keys']
    keys.insert_many(service_keys)


if __name__ == '__main__':
    main()
