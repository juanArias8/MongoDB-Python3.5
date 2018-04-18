from pymongo import MongoClient
from User import User

# Create the mongoDB client
mongo_client = MongoClient("localhost", 27017)

# Connect to the data base
db_test = mongo_client.TestPymongo

# Get the connection
collection_users = db_test.users

# CRUD with mongo
# Read      -> collection.find()
# Insert    -> collection.insert({})
# update    -> collection.update({})
# delete    -> collection.delete({})


def print_all_users():
    data = collection_users.find()
    print("---------------------------------------------------------")
    print("%-20s %-10s %-5s %-20s" % ("Name", "id", "age", "email"))
    print("---------------------------------------------------------")
    for user in data:
        print("%-20s  %-10s  %-5s  %-20s" % (user['name'], user['id'], user['age'], user['email']))


def insert_new_user():
    name = input("What is your name?  ==>  ")
    id_user = input("What is your id?  ==>  ")
    age = input("What is your age?  ==>  ")
    email = input("What is your email?  ==>  ")
    user = User(name, id_user, age, email)
    collection_users.insert(user.user_to_collection())


def update_user_name():
    id_user = input("What is the user id number?  ==>  ")
    new_name = input("What is the new user name?  ==>  ")
    collection_users.update({"id": id_user}, {"$set": {"name": new_name}}, upsert=False, multi=False)


def update_user_id():
    old_id = input("What is the old id number?  ==>  ")
    new_id = input("What is the new id number?  ==>  ")
    collection_users.update({"id": old_id}, {"$set": {"id": new_id}}, upsert=False, multi=False)


def update_user_age():
    id_user = input("What is the user id?  ==>  ")
    new_age = input("What is the new user age?  ==>  ")
    collection_users.update({"id": id_user}, {"$set": {"age": new_age}}, upsert=False, multi=False)


def update_user_email():
    id_user = input("What is the user id?  ==>  ")
    new_email = input("What is the new user email?  ==>  ")
    collection_users.update({"id": id_user}, {"$set": {"email": new_email}}, upsert=False, multi=False)


def delete_user_by_id():
    id_user = input("What is the user id?  ==>  ")
    collection_users.remove({"id": id_user})


def show_options():
    print("---------------------------------------------------------")
    option = int(input("Select an option \n 1.show users \n 2.insert user \n 3.update user name \n 4.update user id \n"
                       " 5.update user age \n 6.update user email \n 7.delete user \n 0.exit  ==>  "))
    print("---------------------------------------------------------")
    return option


while True:
    result = show_options()
    if result == 0:
        break
    elif result == 1:
        print_all_users()
    elif result == 2:
        insert_new_user()
    elif result == 3:
        update_user_name()
    elif result == 4:
        update_user_id()
    elif result == 5:
        update_user_age()
    elif result == 6:
        update_user_email()
    elif result == 7:
        delete_user_by_id()
    else:
        print("Invalid option")
