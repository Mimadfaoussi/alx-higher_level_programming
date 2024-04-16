#!/usr/bin/python3
import json
"""  From JSON string to Object """


def from_json_string(my_str):
    """ we're converting JSON string to python data structure """
    return (json.loads(my_str))
