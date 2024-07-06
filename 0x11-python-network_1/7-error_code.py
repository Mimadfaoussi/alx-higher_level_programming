#!/usr/bin/python3
"""
send a request to the url and display body
response or error if its >= 400
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    if(r.status_code >= 400):
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
