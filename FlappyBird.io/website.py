import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
from random import randint
import numpy as np
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
style.use("ggplot")
# Using Chrome to access web
print("hello")

driver = webdriver.Chrome()
driver.get('http://flappybird.io/')
timeout = 3
try:
    element_present = EC.presence_of_element_located((By.ID, 'main'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")


###### Selenium ENV ######
def rand():                  # random number
    random = randint(5,5)
    divided = random / 10
    return divided
def page_is_loading(driver): # loaded?
    while True:
        x = driver.execute_script("return document.readyState")
        if x == "complete":
            return True
        else:
            yield False
def restart():               # restart func
    element1 = driver.execute_script("return dead")
    print (element1)
    if element1 == True: 
        score = driver.execute_script("return counter.text")
        print(f"score is {score}")
        action = webdriver.common.action_chains.ActionChains(driver)
        action.move_to_element_with_offset(element, 120, 378)
        action.click()
        action.perform()







element = driver.find_element_by_id("testCanvas")

#######################################

# ENV loop

for i in range(0,100000):
    element.click()     # jump
    restart()           # restart func
    time.sleep(rand())  # interval

print("finished")

#####################################################   Q-learning 







