import requests

_url = input("Enter the endpoint to be checked: ")

response = requests.get(_url)

_code = response.status_code

if _code == 200:
    print("endpoint up and running")
else:
    print("End point down!!")