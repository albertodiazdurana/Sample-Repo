import math
import os
import sys

import requests


def greet(who_to_greet):
    test_a = "Test"
    n = 3
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(sys.executable)
r = requests.get("https://hedera.online")
print(r.status_code)

# print (sys.version)
