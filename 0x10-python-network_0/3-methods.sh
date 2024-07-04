#!/bin/bash
# displaying allowed methods 
curl -s -X OPTIONS -D - "$1" | grep 'Allow:' | cut -d " " -f2-
