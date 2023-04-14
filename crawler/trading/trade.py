import mojito
import pprint


from crawler.trading.login import login_stock


class TradeBot:
    def __init__(self):
        print('테스트')

    def order_market_price(self, code, order_quantity):
        #시장가 매수
        try:
            buy = login_stock.create_market_buy_order(
            symbol = code,
            quantity = order_quantity
            )
            pprint.pprint(buy)
            print("매수 성공")

        except Exception as error:
            print("매수 실패: ", error)

    def sell_market_price(self, code, sell_quantity):
        #시장가 매도
        try:
            sell = login_stock.create_market_sell_order(
                symbol = code,
                quantity = sell_quantity
            )
            pprint.pprint(sell)
            print("매도 성공")

            return True

        except Exception as error:
            print("매도 실패: ", error)

            return False
