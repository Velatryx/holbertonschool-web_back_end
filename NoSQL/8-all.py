#!/usr/bin/python3
"""Function that lists all documents in a MongoDB collection"""


def list_all(mongo_collection):
    """
    Returns all documents in the given collection.
    If the collection is empty, returns an empty list.
    """
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
