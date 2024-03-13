import requests

_url = input("Enter your url here: ")

try:
    response = requests.get(_url)
    _code = response.status_code
    if _code == 200:
        print("endpoint up and running")
    else: 
        print("End point down!!")
except:
    print("Your Url is not good")