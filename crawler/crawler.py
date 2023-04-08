from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import csv

from .trading import search_test

class Crawler:
    def __init__(self):
        search_test()

    def crawle(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('window-size=1920,1080')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.implicitly_wait(5)

        driver.get(url='https://www.nasdaq.com/')
        sleep(5)
        # search_box = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')

        search_box = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/article/div/div[2]/div[2]/aside/nsdq-right-rail-desktop/div/div[1]/div/div[1]/form/div/div[2]/input')
        search_box.send_keys('direct offer')
        search_box.send_keys(Keys.RETURN)
        driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/span[2]/select').click()
        driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/span[2]/select/option[2]').click()

        i=1
        while True : 
            title_text = driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[2]/a[1]/div/div[1]').text
            company = title_text.split('Announces')[0]
            
            duplicate_check = []

            with open('check_list.csv', 'r') as to_read:
                reader = csv.reader(to_read)
                for row in reader:
                    duplicate_check.append(row[0])

            if title_text not in duplicate_check:
                with open('check_list.csv', 'a', newline='') as to_write:
                    writer = csv.writer(to_write)
                    writer.writerow([title_text])
                print(f'new news: {title_text}')
            else:
                print('same news', i)
                i += 1
            
            sleep(3) 
            driver.get(url='https://www.nasdaq.com/')
            sleep(5)
            search_box = driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/article/div/div[2]/div[2]/aside/nsdq-right-rail-desktop/div/div[1]/div/div[1]/form/div/div[2]/input')
            sleep(1)
            search_box.send_keys('direct offer')
            sleep(1)
            search_box.send_keys(Keys.RETURN)
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/span[2]/select').click()
            sleep(1)
            driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/span[2]/select/option[2]').click()
            sleep(1)

            print(check)
