from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import sys                        

def perform_test(url):
    # Open Google Chrome browser
    driver = webdriver.Chrome()  # Replace with Firefox or any other browser if needed
    time.sleep(3)

    print(f"The test case started")

    # Maximize the window size
    driver.maximize_window()
    time.sleep(5)

    # Delete the cookies
    driver.delete_all_cookies()

    # Navigate to the URL
    driver.get(url)
    title1 = driver.title
    print(f"Connecting to {title1} page of Geolocation app")

    # Identify the username box and enter the value
    elem1 = driver.find_element(By.NAME, "username")
    elem1.send_keys("root@utrains.test")
    time.sleep(2)

    # Identify the password box and enter the value
    elem2 = driver.find_element(By.NAME, "password")
    elem2.send_keys("root_pass")
    time.sleep(2)

    # Click on the Log in button
    submit_button = driver.find_element(By.CSS_SELECTOR, "button")
    submit_button.click()
    title2 = driver.title

    if title1 == title2:
        print("Wrong credentials please try again !!")
        driver.quit()
        sys.exit(99)
    else:
        print("Connected to website")

    time.sleep(5)

    # Navigate to About us page
    elem3 = driver.find_element(By.LINK_TEXT, "About")
    elem3.click()
    time.sleep(5)

    # Navigate to Departments' page
    elem4 = driver.find_element(By.LINK_TEXT, "Departments")
    elem4.click()
    time.sleep(5)

    # Navigate to Doctors' page
    elem5 = driver.find_element(By.LINK_TEXT, "Doctors")
    elem5.click()
    time.sleep(5)

    # Navigate to Blog page
    elem6 = driver.find_element(By.LINK_TEXT, "Blog")
    elem6.click()
    time.sleep(5)

    # Navigate to Contact page
    elem7 = driver.find_element(By.LINK_TEXT, "Contact")
    elem7.click()
    time.sleep(5)

    # Find and click on the "Make an Appointment" Button
    elem8 = driver.find_element(By.LINK_TEXT, "Make an Appointment")
    elem8.click()
    time.sleep(5)  # Wait for the appointment form to load

    # Close the driver
    driver.quit()
    print("Test to Geolocation app is completed please check the output")
    sys.exit()

# Call the function with your URL
perform_test("http://198.58.119.40:8087/showMyLoginPage")
