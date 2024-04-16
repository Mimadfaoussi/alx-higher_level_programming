#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """ load creates  Object from  “JSON-file """
    with open(filename) as file:
        return json.load(file)
