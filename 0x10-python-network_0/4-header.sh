#!/bin/bash
# get request and send a header variable X-School-User-Id with value 98
curl -s -H "X-School-User-Id: 98" "$1"
 