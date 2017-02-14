#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=chrome_options)

username = **ANY_USERNAME**
##page = 1
url = "https://xhams***.com/user/video/" + username + "/new-1.html"

driver.implicitly_wait(10)
driver.get(url)

links = [];
links = driver.find_elements_by_class_name('hRotator')
#nextPage = driver.find_elements_by_class_name('colR')

## TRYING TO READ THE NEXT PAGE HERE
print driver.find_element_by_class_name('last').get_attribute('href')

noOfLinks = len(links)
count = 0

file = open('x--' + username + '.txt','w')
while count < noOfLinks:
    #print links[count].get_attribute('href')
    file.write(links[count].get_attribute('href') + '\n');
    count += 1

file.close()
driver.close()