#!/usr/bin/env python3
"""write a Python function that lists all documents in a collection:
"""
import pymongo


def list_all(mongo_collection):
    """Return an empty list if no document in the collection"""
    return list(mongo_collection.find()) if mongo_collection != None else []
