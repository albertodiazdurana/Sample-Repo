import requests


r = requests.get("https://hedera.online")
print(r.status_code)
print (r.ok)
