import pprint
import mojito

from crawler.trading.login import login_stock


class TradeBot:
    def __init__(self):
        print('테스트')
    
    def login(self):
        #증권사 로그인
        f = open("crawler/trading/koreainvestment.key")
        lines = f.readlines()
        key = lines[0].strip()
        secret = lines[1].strip()
        acc_no = lines[2].strip()
        f.close()

        broker = mojito.KoreaInvestment(
            api_key = key,
            api_secret = secret,
            acc_no = acc_no,
            exchange='나스닥'
        )

        print(broker)
        
        return broker

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

            return True

        except Exception as error:
            print("매도 실패: ", error)

            return False
