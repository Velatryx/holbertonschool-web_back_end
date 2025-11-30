#!/usr/bin/env python3
"""Update topics of school documents by name"""


def update_topics(mongo_collection, name, topics):
    """
    Updates all documents where 'name' matches the given name.
    Sets the 'topics' field to the provided list.
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
