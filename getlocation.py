from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import reverse_geocoder as rg
import pprint
import pandas as pd

def getLocation():


    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path = './chromedriver.exe', options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    return (latitude,longitude)


print(getLocation())
"""
def reversegeocode(coordinates):
    result = rg.search(coordinates)
    pprint.pprint(coordinates)
    result=[{
              'name': 'Chennai'
            }]
if __name__=="__main__":
    coordinates = (latitude, longitude)
    reversegeocode(coordinates)
"""
print('Chennai')

