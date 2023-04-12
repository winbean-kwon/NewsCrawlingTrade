from time import sleep
import csv
import re

from selenium import webdriver # module providing crawling
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from crawler.trading.trade import TradeBot



class Crawler: # class providing company name & news title
    def __init__(self):
        self.driver = None

    def crawl_settings(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('window-size=1920,1080')
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.implicitly_wait(5)

        return self.driver

    def crawl_news(self): # function providing news title
        self.crawl_settings()
        self.driver.get(url='https://www.nasdaq.com/')
        sleep(5)
        search_box = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/article/div/div[2]/div[2]/aside/nsdq-right-rail-desktop/div/div[1]/div/div[1]/form/div/div[2]/input')
        search_box.send_keys('direct offer')
        search_box.send_keys(Keys.RETURN)
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/span[2]/select').click()
        self.driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/span[2]/select/option[2]').click()

        i=1

        while True:
            title_text = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[2]/a[1]/div/div[1]').text
            duplicate_check = []
            with open('check_list.csv', 'r', encoding = "utf8") as to_read:
                reader = csv.reader(to_read)
                for row in reader:
                    duplicate_check.append(row[0])

            if title_text not in duplicate_check:
                with open('check_list.csv', 'a', newline='', encoding = "utf8") as to_write:
                    writer = csv.writer(to_write)
                    writer.writerow([title_text])
                print(f'new news: {title_text}')
                self.crawl_company_symbol(title_text)

            else:
                print('same news', i)
                i += 1

            sleep(3)
            self.driver.get(url='https://www.nasdaq.com/')
            sleep(5)
            search_box = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div[2]/article/div/div[2]/div[2]/aside/nsdq-right-rail-desktop/div/div[1]/div/div[1]/form/div/div[2]/input')
            sleep(1)
            search_box.send_keys('direct offer')
            sleep(1)
            search_box.send_keys(Keys.RETURN)
            sleep(1)
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/span[2]/select').click()
            sleep(1)
            self.driver.find_element(By.XPATH, '/html/body/div[2]/div/main/div[2]/div[3]/div/section/div[2]/div[3]/div[3]/div[1]/span[2]/select/option[2]').click()
            sleep(1)

    def crawl_company_symbol(self, title_text): # function providing company symbol
        company = title_text.split('Announces')[0]
        self.crawl_settings()
        self.driver.get(url='https://finance.yahoo.com/')
        sleep(5)
        search_box = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/div[1]/div/div/div/div[1]/div/div[2]/div/form/input[1]')
        search_box.send_keys(company)
        sleep(3)
        search_box.send_keys(Keys.RETURN)
        company_symbol = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[2]/div/div/div[6]/div/div/div/div[2]/div[1]/div[1]/h1').text
        symbol = re.search(r"\((.*?)\)", company_symbol).group(1)

        print(symbol)
        TradeBot.order_market_price(self, symbol, 5)

        return symbol
