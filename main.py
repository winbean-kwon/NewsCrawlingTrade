from crawler import Crawler, login


login.login_stock()
crawler = Crawler()
crawler.crawl_news()
