#!/usr/bin/env python3
# 
# Inspired by Selenium Documentation, found at:
# https://www.selenium.dev/selenium/docs/api/py/#example-0
# 

import getpass
import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.firefox.options
import time

### Setup ###
my_email = input("email: ")
my_passwd = getpass.getpass("password: ")

configuration = selenium.webdriver.firefox.options.Options()

# Uncomment this in order to run it HEADLESS, i.e. run
# the browser in the background and hide the GUI!
# This may be helpful if you want to run it from the terminal
# as a background process and do data processing, etc.
#configuration.headless = True

### Test ###
browser_obj = selenium.webdriver.Firefox(options=configuration)
browser_obj.get("https://www.discord.com/login")

# SELECT the right elements to log in.
# we can do this by invoking their `name` attributes from HTML
email_src = browser_obj.find_element(By.NAME, "email")
assert email_src!=None,"FATAL ERR: User email HTML element not found!"
passwd_src = browser_obj.find_element(By.NAME, "password")
assert passwd_src!=None,"FATAL ERR: PASSWORD HTML element not found!"
email_src.send_keys(my_email)
passwd_src.send_keys(my_passwd)

time.sleep(2)
passwd_src.submit()
time.sleep(12)

browser_obj.quit()

### Verify ###
# TODO we can add tests here, but for now,
# if the assert statements passed, then we have a success.
print("Success")

