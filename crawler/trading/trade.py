from object import broker
import pprint

class trBot: # -> TrBot
    def __init__(self):
        print('테스트')
    
    def orderMarketPrice(self, code, q):
        #시장가 매수
        try:
            buy = broker.create_market_buy_order(
            symbol = code,
            quantity = q
            )
            pprint.pprint(buy)

            return True
        
        except:
            print("매수 실패")

            return False
        
    def sellMarketPrice(self, code, q):
        #시장가 매도
        try:
            sell = broker.create_market_sell_order(
                symbol = code,
                quantity = q
            )
            pprint.pprint(sell)

            return True
        
        except:
            print("매도 실패")
            
            return False
