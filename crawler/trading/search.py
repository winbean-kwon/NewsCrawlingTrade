from time import sleep
import pprint
from object import broker
from selenium import webdriver # module providing crawling
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from news_crawler import Crawler

class Search:
    def __init__(self):
        pass

    def search_symbol(crawl_company):
        crawl_company = Crawler.crawl_company()

    def search_daily_price(price):
        price = broker.fetch_ohlcv(
            symbol = "TSLA",
            timeframe='D',
            adj_price=True
        )

        #일봉 조회
        pprint.pprint(price)

        return price
    
    def search_now_price(price):
        #현재가 조회
        price = broker.fetch_price("TSLA")
        pprint.pprint(price)

        return price

