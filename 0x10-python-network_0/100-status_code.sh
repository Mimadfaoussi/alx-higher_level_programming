#!/bin/bash
# printing the status code only 
curl -s -o /dev/null -w "%{http_code}" "$1"
