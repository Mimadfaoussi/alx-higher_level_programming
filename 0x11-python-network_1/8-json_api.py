#!/usr/bin/python3
""" takes in a letter and sends a POST request with the letter"""
import requests
import sys

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    r = requests.post(url, data={"q": q})
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get('id'), response.get('name')))
    except ValueError:
        print("Not a valid JSON")
