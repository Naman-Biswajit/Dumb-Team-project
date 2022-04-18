import os
import dotenv
import hashlib

from pymongo import MongoClient

dotenv.load_dotenv('../.env')

cluster = MongoClient(os.getenv('MONGO_URL'))
main_db = cluster['main']
users = main_db['users']


def insert_user(user_id, password):
    password = b'{password}'
    password = hashlib.sha256(password).hexdigest()

    searched_user = users.find_one({'_id': str(user_id)})

    if searched_user is None:
        users.insert_one({'_id': str(user_id), 'password': password})
        return True

    elif not (searched_user['_id'] == str(user_id)):
        users.insert_one({'_id': str(user_id), 'password': password})
        return True

    else:
        return False
