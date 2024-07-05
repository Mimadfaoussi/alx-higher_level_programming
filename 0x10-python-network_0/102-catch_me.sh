#!/bin/bash
# making a request to the server and making it respond with you got me!
curl -s -o /dev/null -w "You got me!" "$1"
