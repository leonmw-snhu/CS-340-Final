from pymongo import MongoClient
import sys
import ast
from packaging import version
import unittest
from ipdb import set_trace

MIN_VERSION = "3.9.12"

# Check minimum python version for compatibility
print("Checking python version")
if version.Version(MIN_VERSION) <= version.Version(sys.version.split(" ")[0]):
    print("Python version passed")
else:
    print(f"""Python version {sys.version.split()[0]} is < {
          MIN_VERSION}\nUse at own risk""")


class AnimalShelter():
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,
                 username: str = 'root',
                 password: str = 'vvEepTf069',
                 host: str = 'nv-desktop-services.apporto.com',
                 port: int = 32253,
                 db: str = 'AAC',
                 col: str = 'animals') -> None:
        """_summary_

        Args:
            username (str, optional): The user you wish to access the database with. Defaults to 'root'.
            password (str, optional): The password for the user you wish to access the database with. Defaults to 'vvEepTf069'.
            host (str, optional): The host of the database you're connecting to. Defaults to 'nv-desktop-services.apporto.com'.
            port (int, optional): The port of the host to use to connect to the database. Defaults to 32253.
            db (str, optional): The database to connect to. Defaults to 'AAC'.
            col (str, optional): The collection to connect to. Defaults to 'animals'.
        """
        USER = username
        PASS = password
        HOST = host
        PORT = port
        DB = db
        COL = col

        #
        # Initialize Connection
        #
        self.client = MongoClient(f"mongodb://{USER}:{PASS}@{HOST}:{PORT}")
        self.database = self.client[f"{DB}"]
        self.collection = self.database[f"{COL}"]

# Complete this create method to implement the C in CRUD.

    def create(self, data) -> bool:
        """_summary_

        Args:
            data (_type_): _description_

        Raises:
            Exception: _description_
            Exception: _description_

        Returns:
            bool: _description_
        """
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

    def find_one(self, query=None) -> MongoClient:
        """_summary_

        Args:
            query (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        return self.database.animals.find_one(query)

    def find(self, query: dict = None) -> list:
        """_summary_

        Args:
            query (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        results = []
        for queryResult in self.database.animals.find(query):
            results.append(queryResult)
        return results
    
    read = find

# Method to implement the U in CRUD.

    def update(self, search_params: dict, update_params: dict, update_all: bool) -> None:
        if update_all:
            result = self.update_all(search_params, update_params)
        else:
            result = self.update_one(search_params, update_params)
        return result

    def update_one(self, search_params: dict, update_params: dict) -> int:
        updatedResults = self.collection.update_one(
            search_params, {'$set': update_params})
        return updatedResults.modified_count

    def update_all(self, search_params: dict, update_params: dict) -> int:
        updatedResults = self.collection.update_many(
            search_params, {'$set': update_params})
        return updatedResults.modified_count


# Method to implement the D in CRUD.


    def delete_one(self, search_params: dict) -> int:
        if self.collection.animals.delete_one(search_params):
            return 1
        else:
            print("No records found")
            return 0

    def delete_many(self, search_params: dict) -> int:
        deletedResults = self.collection.delete_many(search_params)
        return deletedResults.deleted_count


class TestAnimalShelterClass(unittest.TestCase):

    def setUp(self) -> None:
        username: str = 'root'
        password: str = 'vvEepTf069'
        host: str = 'nv-desktop-services.apporto.com'
        port: int = 32253
        db: str = 'AAC'
        col: str = 'animals'
        self.client = MongoClient(
            f"mongodb://{username}:{password}@{host}:{port}")
        self.database = self.client(f"{db}")
        self.collection = self.database(f"{col}")

    def test_basic_search():
        search = "{'breed':'Pit Bull Mix'}"
        if type(search) != dict:
            search = ast.literal_eval(search)

    def test_find():
        search = "{'breed':'Pit Bull Mix'}"
        if type(search) != dict:
            search = ast.literal_eval(search)

    def test_update():
        pass


def print_menu():
    pass


def helpMe():
    print("""
        For either option 1 or option 2, the query should be entered as follows:
            {'key':'value'} 
        Both options can also be left empty
            Option 1 - Find will return 1 record
            Option 2 - Find all will return all records
        """)


if __name__ == "__main__":
    AS = AnimalShelter()

    while True:
        testOptions = {
            "find_one": "Find single record",
            "find": "Find all records",
            "create": "Create new record",
            "update": "Update record",
            "delete": "Delete record"
        }
        for v, t in enumerate(testOptions, start=1):
            print(f"{v} - {t}")
        if not [v for v in enumerate(testOptions)]:
            print("Option not valid, please reenter")
        answer = input("""
        1. Find single record
        2. Find all records
        3. Create new record 
        4. Update record
        5. Delete record
        h. Help
        q. quit
        """)
        if answer.lower() == "q":
            sys.exit()
        elif answer.lower() == "h":
            helpMe()
            continue
        runMethod = globals(
        )[f"{[v for i, v in enumerate(testOptions)][answer-1]}"]
        runMethod()
