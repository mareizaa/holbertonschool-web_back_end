#!/usr/bin/env python3
""" Inserts a new document in a
    collection based on kwarg
"""


def insert_school(mongo_collection, **kwargs):
    """
        Returns the new _id
    """
    document_id = mongo_collection.insert(kwargs)
    return document_id
