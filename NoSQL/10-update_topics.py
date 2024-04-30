#!/usr/bin/env python3
"""changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Update the topics of a school document based on the school name.

    Parameters:
    mongo_collection: pymongo collection object
    name (str): the school name to update
    topics (list of str): the list of topics approached in the school
    """

    # Update the document
    updated_document = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
