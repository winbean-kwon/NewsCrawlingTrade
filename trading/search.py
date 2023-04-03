import pprint
from object import broker

ohlcv = broker.fetch_ohlcv(
    symbol = "TSLA",
    timeframe='D',
    adj_price=True
)

#일봉 조회
pprint.pprint(ohlcv)

#현재가 조회
price = broker.fetch_price("TSLA")
pprint.pprint(price)