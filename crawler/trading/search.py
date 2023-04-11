import pprint
from object import broker

from news_crawler import Crawler

class Search:
    def __init__(self):
        pass

    def get_symbol(crawl_company):
        crawl_company = Crawler.crawl_company_symbol()

    def get_daily_price(price):
        company_symbol = Crawler.crawl_company_symbol()
        print(company_symbol)
        price = broker.fetch_ohlcv(
            symbol = company_symbol,
            timeframe='D',
            adj_price=True
        )

        #일봉 조회
        pprint.pprint(price)

        return price
    
    def get_now_price(price):
        #현재가 조회
        price = broker.fetch_price("TSLA")
        pprint.pprint(price)

        return price

  