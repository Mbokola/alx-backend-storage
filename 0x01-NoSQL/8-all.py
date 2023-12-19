#!/usr/bin/env python3
""" 8-all module """


def list_all(mongo_collection):
    """ This function lists all documents in a collection """
    result = mongo_collection.find()
    return result if result else []
