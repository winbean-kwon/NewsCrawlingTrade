import pprint
from object import broker

def searchDailyPrice(price):
    price = broker.fetch_ohlcv(
        symbol = "TSLA",
        timeframe='D',
        adj_price=True
    )

    #일봉 조회
    pprint.pprint(price)

    return price

#현재가 조회
price = broker.fetch_price("TSLA")
pprint.pprint(price)