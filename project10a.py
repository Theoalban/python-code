import requests

response = requests.get('https://www.wikipedia.org/')

_code = response.status_code

if _code == 200:
    print("endpoint up and running")
else:
    print("End point down!!")