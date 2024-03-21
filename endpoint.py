import requests #for  making HTTP requests
def url_check(url):
    try:
        resp = requests.get(url) #to hit an endpoint  and get a response from it.

        #print(dir(resp)) #list all available methods for the  object resp
        status = resp.status_code #accessing attributes of the response object, status code is one such attribute

        if status == 200:        #Response [200] means that the request was successful.
            return True    
        else:
            return False   
    except Exception as e:      #A generic exception handler.
        print("An error occurred:", type(e).__name__)   #Printing the name of the exception raised.
        print("Error description:", e.args)             #Prints any associated information with the exception.
        print("Please double check  your URL.")         #Giving some context to what went wrong.
        return  False                     
#url_check()                       #Calling the function to execute it.
def main():
    website_url = "http://cnn.com"  # URL to check
    if url_check(website_url):
        print(f"The website {website_url} is up and running.")
    else:
        print(f"The website {website_url} is down.")
    # Call the url_check function
    url_check(website_url)

if __name__ == "__main__":
    main()

'''
#Accessing the content of the response in different ways
content = resp.text         #returns the content in text format (string), default encoding is UTF-8
html = resp.content        #returns the content in binary format, can be decoded to string using specified encoding
html = resp.content        #returns the content in bytes, can be decoded to string using specific encoding

#To access headers sent by the server along with the response
headers = resp.headers       #Returns a dictionary containing the header information

#Checking whether a certain header exists or not
if 'Content-Type' in headers:
    print("The Content-Type header is present.")
else:
    print("The Content-Type header is missing.")    
    
#To access the actual data/content of the web page, we use .text 
    webpage = resp.text
    print(webpage[:50]) #this will show us the first 50 characters of the content.
    
   

status = resp.status_code #accessing response status code, e.g., 200 means that everything is OK

isUp=True  if status==200 else False #checking whether server responded and returned a success status code

#the following lines are equivalent:


#Accessing and printing out the content
'''