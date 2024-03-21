# Selenium project:          
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys                        

#open Google Chrome browser  
driver=webdriver.Chrome() #replace with Firefox or any other browser if needed
time.sleep(3)

print(f"The test case started")

#maximize the window size #
driver.maximize_window() #
time.sleep(5)

#delete the cookies  
driver.delete_all_cookies()

#navigate to the url  
driver.get("http://198.58.119.40:8087/showMyLoginPage") #  replace the URL to your own page 

# get the browser's title
title1= driver.title
print(f"Connecting to {title1} page of Geolocation app")

# identify the username box and enter the value  
elem1 = driver.find_element(by=By.NAME, value="username") # find by name attribute and enter username
elem1.send_keys("root@utrains.test") # send keys is used for entering values in the field
time.sleep(2)

# identify the password box and enter the value  
elem2 = driver.find_element(by=By.NAME, value="password") # password box identified same as above but different name attribute
elem2.send_keys("root_pass")  # send keys  is used for entering password in the field
time.sleep(2)

# Click on the Log in button
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button") # Find by CSS selector - it will search by css
submit_button.click()  # click method is used to invoke a click event on an element
title2= driver.title # capture the new window’s title after clicking the submit button

if title1 == title2:
    print("Wrong credentials please try again !!")
    driver.quit()
    sys.exit(99)
else:
    print("Connected to website")

time.sleep(5)

# navigate to About us page
elem3= driver.find_element(By.LINK_TEXT, "About") # link text is used to locate links based on their text
elem3.click()   # click method is used to perform a mouse-click action on an element
time.sleep(5)

# navigate to Departments' page
elem4= driver.find_element(By.LINK_TEXT, "Departments") # same as above but this time we are using partial link text
elem4.click()
time.sleep(5)

# navigate to Doctors' page
elem5= driver.find_element(By.LINK_TEXT, "Doctors")
elem5.click()
time.sleep(5)

# navigate to Blog page
elem6= driver.find_element(By.LINK_TEXT, "Blog")
elem6.click()
time.sleep(5)

# navigate to Contact page
elem7= driver.find_element(By.LINK_TEXT, "Contact")
elem7.click()
time.sleep(5)

# Find and click on the "Make an Appointment" Button
elem8 = driver.find_element(By.LINK_TEXT, "Make an Appointment")
elem8.click()
time.sleep(5)  # Wait for the appointment form to load


# close the driver
driver.quit()
print("Test to Geolocation app is completed please check the output")
sys.exit()
 