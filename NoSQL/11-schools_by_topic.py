#!/usr/bin/env python3
"""returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that searches for schools in a MongoDB collection that have a specific topic.

    Parameters:
    mongo_collection: pymongo collection object
    topic (str): The topic to search for within the documents of the collection

    Returns:
    list: A list of schools that have the specified topic
    """
    schools_list = []
    # Query the collection for documents where the 'topics' field contains the topic
    results = mongo_collection.find({"topics": topic})
    for school in results:
        # Assuming the school name is stored under the 'name' key
        schools_list.append(school.get('name', 'No name available'))

    return schools_list
