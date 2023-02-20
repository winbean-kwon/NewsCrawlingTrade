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

driver.get(url='https://www.google.com/')

# search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

search_box = driver.find_element(By.CLASS_NAME, 'gLFyf') #검색창 className
search_box.send_keys('계약 체결')
search_box.send_keys(Keys.RETURN)

driver.find_element(By.ID, 'hdtb-tls').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[4]/div/div[2]/div/span[2]').click()
driver.find_element(By.XPATH, '//*[@id="lb"]/div/g-menu/g-menu-item[2]/div/a').click() 
driver.find_element(By.XPATH, '/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/a/h3').click()

while(True):
    pass

# elements = driver.find_elements_by_xpath('//*[@id="rso"]/div[*]/div/div[1]/a/h3/span')

# for element in elements:
#   print(element.text)
#   print(element.text, file=open('gorio.txt', 'w', encoding='utf-8'))

# sleep(3)
# driver.close()

