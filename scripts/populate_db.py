from pymongo import MongoClient
import os

password = os.getenv('ADMIN_PASSWORD')

defaultkeys = {
    'core': 'SeedyFiubaCore',
    'users': 'SeedyFiubaUsers',
    'sc': 'SeedyFiubaSC',
}

services = {'core', 'users', 'sc', 'gateway'}


def main():
    client: MongoClient = MongoClient(
        f"mongodb+srv://admin:{password}@cluster.wbauf.mongodb.net/main?retryWrites=true&w=majority")

    values = [{'service': service, 'apikey': key} for service, key in defaultkeys.items()]

    dev_db = client['dev']
    main_db = client['main']

    # dev_defaultkeys = dev_db['defaultkeys']
    # dev_defaultkeys.insert_many(values)
    # main_defaultkeys = main_db['defaultkeys']
    # main_defaultkeys.insert_many(values)

    service_keys = []
    for owner in services:
        for val in values:
            service_keys.append(
                {'owner': owner, 'service': val['service'], 'apikey': val['apikey']})

    dev_keys = dev_db['keys']
    dev_keys.insert_many(service_keys)
    main_keys = main_db['keys']
    main_keys.insert_many(service_keys)


if __name__ == '__main__':
    main()
