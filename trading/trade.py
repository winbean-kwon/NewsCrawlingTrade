from object import broker
import pprint

buy = broker.create_limit_buy_order(
    symbol = "TSLA",
    price = 30,
    quantity = 5
)

sell = broker.create_limit_sell_order(
    symbol = "TSLA",
    price = 30,
    quantity = 5
)

print(buy)
print(sell)