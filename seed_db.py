import pymongo
import datetime


# to seed the database, insert into collections
def seedDatabase():
    seedUsers()
    seedNotes()

# to insert into collections, create the collectio
def seedUsers():
    users = getCollections('users')
    users.insert_one(
            { 'email': 'foo@bar.io',
              'pw': 'youshallnotpassword',
              'notes': [],})

def seedNotes():
    notes = getCollections('notes')
    notes.insert_one(
            {'title': 'null',
            'content': 'this is a null note that belongs to no one',
            'ts': datetime.datetime.utcnow()},
            )

# to create collections, call on db
def getCollections(name):
    db = getDb()
    return pymongo.collection.Collection(db, name)

# to call on db, create db.

def getDb(name='znote'):
    client = createClient()
    return pymongo.database.Database(client, name)

def createClient(uri='localhost', port=27017):
    return pymongo.MongoClient(uri, port)


if __name__ == '__main__':
    seedDatabase()
