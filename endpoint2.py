
import requests

def urlCheck(url):
    isUp=True
    try:
        resp = requests.get(url)
    except:
        print("please double check your url")
    else:
        status = resp.status_code
        if status == 200:
            isUp=True
        else:
            isUp=False
    return isUp  
a=urlCheck('https://www.baidu.com')
print(a) 

#### OR
#a=urlCheck(input('Enter a URL to check: ')) # this will take the input from user and pass it in the function
#print(a)
  
