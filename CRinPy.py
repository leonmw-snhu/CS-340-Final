from pymongo import MongoClient
from bson.objectid import ObjectId
import sys
from pdb import set_trace
import ast
import json
from pprint import pprint


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,
                 username='root',
                 password='vvEepTf069',
                 host='nv-desktop-services.apporto.com',
                 port=32253,
                 db='AAC',
                 col='animals'):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # USER = 'aacuser'
        USER = username
        PASS = password
        HOST = host
        PORT = port
        DB = db
        COL = col
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' %
                                  (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.

    def create(self, data):
        if data is not None and type(data) == dict:
            if self.database.animals.insert_one(
                    data).inserted_id:  # data should be dictionary
                return True
            else:
                return False
        elif type(data) != dict:
            raise Exception("Data not in correct format")
        else:
            raise Exception("Nothing to save, because data parameter is empty")


# Create method to implement the R in CRUD.

    def find_one(self, query=None):
        return self.database.animals.find_one(query)

    def find(self, query=None):
        results = []
        for queryResult in self.database.animals.find(query):
            results.append(queryResult)
        return results

if __name__ == "__main__":
    AS = AnimalShelter()

    while True:
        answer = input("""
        1. Find single record
        2. Find all records
        3. Create record
        h. Help
        q. quit
        """)

        if answer == "1":
            search = input("What do you want to find? ")
            set_trace()
            if type(search) != dict:
                search = ast.literal_eval(search)
            pprint(AS.find_one(search))
        elif answer == "2":
            search = input("What do you want to find all the records of? ")
            set_trace()
            if type(search) != dict:
                search = ast.literal_eval(search)
            results = AS.find(search)
            if len(results) >= 1:
                pprint(results)
            else:
                pprint("No records found")
        elif answer == "3":
            profile = input(
                "What's the information for the record you want to create? ")
            if type(profile) != dict:
                profile = ast.literal_eval(profile)
            if AS.create(profile):
                pprint('Sucessfully created record')
            else:
                pprint('Failed to create record')
        elif answer.lower() == "h":
            print("""
            For either option 1 or option 2, the query should be entered as follows:
                {'key':'value'} 
            Both options can also be left empty
                Option 1 - Find will return 1 record
                Option 2 - Find all will return all records
            """)
        elif answer.lower() == 't':
            print("******Testing find_one")
            search = "{'breed':'Pit Bull Mix'}"
            if type(search) != dict:
                search = ast.literal_eval(search)
            pprint(AS.find_one(search))
            print("**********Test complete***********")
            print("******Testing find")
            search = "{'breed':'Pit Bull Mix'}"
            if type(search) != dict:
                search = ast.literal_eval(search)
            pprint(AS.find(search))
            print("**********Test complete***********")
        elif answer == "q":
            sys.exit()
        else:
            print("Command not recognized, please reenter")
