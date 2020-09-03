from selenium import webdriver
import time
views = int(input("Made By Stealth Enter Ammount Of Views: "))
view_time = int(input("Enter view time: "))

browser = webdriver.Firefox()

for i in range(views):
    browser.get('#yourlink')
    time.sleep(view_time)

browser.close()
#made By Stealth Dont Skid Please!!
