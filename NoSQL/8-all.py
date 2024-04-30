#!/usr/bin/env python3
"""List all documents in a collection"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents in a MongoDB collection.

    :param mongo_collection: Pymongo collection object
    :return: List of documents in the collection, empty list if no documents
    """
    return list(mongo_collection.find())


# Example usage:
# Assuming 'client' is a MongoClient object connected to the MongoDB server
# db = client['my_database']
# collection = db['my_collection']
# print(list_all(collection))
