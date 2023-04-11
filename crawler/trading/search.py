import pprint
from object import broker

from news_crawler import Crawler

class Search:
    def __init__(self):
        self.crawler = Crawler()

    def get_daily_price(self): #일봉 조회
        daily_price = broker.fetch_ohlcv(
            symbol = self.crawler.crawl_company_symbol(),
            timeframe='D',
            adj_price=True
        )
        pprint.pprint(daily_price)

        return daily_price
    
    def get_now_price(self): #현재가 조회
        now_price = broker.fetch_price(self.crawler.crawl_company_symbol())
        pprint.pprint(now_price)

        return now_price

