#!/bin/bash
# we will send a request to the webserver and count the and displays the size of the body of the response
curl -s "$1" | wc -c
