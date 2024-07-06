#!/usr/bin/python3
""" takes a url and print the value X-Request-Id from the header  response """
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        headers = response.info()
    x_request_id = headers.get('X-Request-Id')
    print(x_request_id)
