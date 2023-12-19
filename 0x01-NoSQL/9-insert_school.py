#!/usr/bin/env ptyhon3
""" 9-insert_school module """


def insert_school(mongo_collection, **kwargs):
    """
    This function inserts a new document in a collection based on kwargs
    """
    collection = mongo_collection.insert_one(kwargs)
    return collection.inserted_id
