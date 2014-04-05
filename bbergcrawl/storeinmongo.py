from pymongo import MongoClient

"""
class responsible for storing the documents
into the respective db/collection of MongoDB
"""
class storeinmongo:
    """
    By default the host and port are this.
    """
    host = 'localhost'
    port = 27017
    db = ""
    collection = ""
    client = "No Client"

    def __init__(self, dbname, collection):
	try:
	    self.client = MongoClient(self.host, self.port)
	    self.db = self.client[dbname]
	    self.collection = self.db[collection]
	except:
	    print "Could not connect to MongoClient"

    """
    Inserts the document into the collection of the db,
    ie the current client, db and collection
    """
    def store(self, document):
	try:
	    self.collection.insert(document)
	except:
	    print "The Document could not be inserted in the DB"