#!/usr/bin/env python3
"""Return list of schools that have a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns schools where the 'topics' field contains the given topic.
    """
    return list(mongo_collection.find({ "topics": topic }))
