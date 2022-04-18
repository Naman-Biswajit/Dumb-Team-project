import os
import dotenv
import hashlib

from pymongo import MongoClient

dotenv.load_dotenv('../.env')

cluster = MongoClient(os.getenv('MONGO_URL'))
main_db = cluster['main']
users = main_db['users']


def insert_user(username, password):
    password = b'{password}'
    username = b'{username}'
    user_id = hash(username)
    password = hashlib.sha256(password).hexdigest()

    print('finding users')
    searched_users = users.find_one({'_id': str(user_id)})
    print(searched_users)

    if searched_users is None:
        print('inserting user')
        users.insert_one(
            {'_id': str(user_id), 'password': password})
        print("User added")
        return True

    else:
        return False
