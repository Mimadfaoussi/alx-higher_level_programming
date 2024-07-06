#!/usr/bin/python3
""" send POST request and decode the body of response """
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    encoded_data = urllib.parse.urlencode(email).encode('utf-8')

    request = urllib.request.Request(url, data=encoded_data, method='POST')

    with urllib.request.urlopen(request) as response:
        html = response.read()
    print(html.decode('utf-8'))
