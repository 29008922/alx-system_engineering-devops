#!/usr/bin/python3
"""getting user data using api"""

import requests as req
import sys

user_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/users/{}".format

resp = req.get(url).json()
print(resp)

