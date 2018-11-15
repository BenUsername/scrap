import os
os.system('cls') # clear terminal

#scrap stock screener from TradingView

import json
import requests
from bs4 import BeautifulSoup

class AppleJobsScraper(object):
    def __init__(self):
        self.search_request = {"filter":[{"left":"market_cap_basic","operation":"nempty"},{"left":"type","operation":"in_range","right":["stock","dr","fund"]},{"left":"subtype","operation":"in_range","right":["common","","etf","unit"]},{"left":"exchange","operation":"in_range","right":["NYSE","NASDAQ","AMEX"]}],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["name","close","change","change_abs","Recommend.All","volume","market_cap_basic","price_earnings_ttm","earnings_per_share_basic_ttm","number_of_employees","sector","description","name","type","subtype","pricescale","minmov","fractional","minmove2"],"sort":{"sortBy":"market_cap_basic","sortOrder":"desc"},"options":{"lang":"en"},"range":[0,150]}

    #def scrape(self):
        #jobs = self.scrape_jobs()
        #for job in jobs:
            #print(job)

    def scrape_jobs(self):

        payload = json.dumps(self.search_request)
        session = requests.Session()

        r = session.post(
            url='https://scanner.tradingview.com/america/scan',
            data=payload,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70x.0.3538.77 Safari/537.36',
                'Accept': 'text/plain, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6',
                'Connection': 'keep-alive',
                'Content-Length': '685',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    #'Host': 'scanner.tradingview.com',
                'Origin': 'https://www.tradingview.com',
                'Referer': 'https://www.tradingview.com/screener/',
                }
                        )

        print(r)

        s = BeautifulSoup(r.text,features="lxml")

        print("hello world")

        with open("tview_scan.html", "w") as file:
            file.write(str(s))

        body = (s.find('p'))
        print(body)

if __name__ == '__main__':
    scraper = AppleJobsScraper()
    scraper.scrape_jobs()
