from pymongo import MongoClient
import os
from passlib.context import CryptContext

password = os.getenv('ADMIN_PASSWORD')
database = os.getenv('DATABASE')

pwd = CryptContext(schemes='ldap_salted_md5')

services = ['core', 'users', 'sc', 'gateway', 'apikeys']


def main():
    client: MongoClient = MongoClient(
        f"mongodb+srv://admin:{password}@cluster.wbauf.mongodb.net/?retryWrites=true&w=majority")

    values = [{'service': service, 'apikey': pwd.hash(service+'default')[6:-1]}
              for service in services if service != 'apikeys']

    db = client[database]

    default_col = db['defaultkeys']
    default_col.insert_many(values)

    service_keys = []
    for owner in services:
        if owner == 'apikeys':
            continue
        for service in services:
            if service == owner:
                continue
            service_keys.append({
                'owner': owner,
                'service': service,
                'apikey': pwd.hash(owner+service)[6:-1]
            })

    keys = db['keys']
    keys.insert_many(service_keys)


if __name__ == '__main__':
    main()
