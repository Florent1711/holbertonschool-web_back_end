#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""

from bson import ObjectId


def insert_school(mongo_collection, **kwargs):
    # insert the new document and get the insert id
    insert_result = mongo_collection.insert_one(kwargs)

    # Return the new id
    return insert_result.inserted_id

# Example usage:
# Assuming 'school_collection' is a valid PyMongo collection object
# new_id = insert_school(school_collection, name="Copilot Academy", level="High School")
# print("New document ID:", new_id)
