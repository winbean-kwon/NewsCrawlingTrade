from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('window-size=1920,1080')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.implicitly_wait(5)

driver.get(url='https://www.nasdaq.com/')
time.sleep(5)
# search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

search_box = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/article/div/div[2]/div[2]/aside/nsdq-right-rail-desktop/div/div[1]/div/div[1]/form/div/div[2]/input')
time.sleep(1)
search_box.send_keys('clinical success')
search_box.send_keys(Keys.RETURN)

driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/span[2]/select').click()
driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/span[2]/select/option[2]').click()
title_text = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[2]/a[1]/div/div[1]').text
print(title_text)



while(True):
    pass



# elements = driver.find_elements_by_xpath('//*[@id="rso"]/div[*]/div/div[1]/a/h3/span')

# for element in elements:
#   print(element.text)
#   print(element.text, file=open('gorio.txt', 'w', encoding='utf-8'))

# sleep(3)
# driver.close()

