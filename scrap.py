#scrap stock screener from TradingView

import json
import requests
from bs4 import BeautifulSoup

class AppleJobsScraper(object):
    def __init__(self):
        self.search_request = {"filter":[{"left":"market_cap_basic","operation":"nempty"},{"left":"type","operation":"in_range","right":["stock","dr","fund"]},{"left":"subtype","operation":"in_range","right":["common","","etf","unit"]},{"left":"exchange","operation":"in_range","right":["NYSE","NASDAQ","AMEX"]}],"symbols":{"query":{"types":[]},"tickers":[]},"columns":["name","close","change","change_abs","Recommend.All","volume","market_cap_basic","price_earnings_ttm","earnings_per_share_basic_ttm","number_of_employees","sector","description","name","type","subtype","pricescale","minmov","fractional","minmove2"],"sort":{"sortBy":"market_cap_basic","sortOrder":"desc"},"options":{"lang":"en"},"range":[0,150]}

    def scrape(self):
        jobs = self.scrape_jobs()
        for job in jobs:
            print(job)

    #def scrape_jobs(self, max_pages=9553):
    def scrape_jobs(self):
        jobs = []
        #totalCount = 0
        #pageno = 0
        #self.search_request['totalCount'] = totalCount
        #self.search_request['pageNumber'] = pageno

        #while totalCount < max_pages:

        payload = json.dumps(self.search_request)
            #print(json.loads(payload))

        session = requests.Session()

        r = session.post(
            url='https://scanner.tradingview.com/america/scan',
            data=payload,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
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

            #print(totalCount + 1)

            #t = BeautifulSoup(r.content,features="lxml")
        s = BeautifulSoup(r.text,features="lxml")

            #print(totalCount + 2)

            #print(s)
            #print(t)
                #print(s.requisition)

            #if not s.requisition:
                #print(totalCount + 3)
                #break

            #print(totalCount + 4)

        with open("tview_scan.html", "w") as file:
            file.write(str(s))

        body = (s.find('p'))

        #content = body.findChildren()

        print(body)
        #print(content)

        #for r in s.find('body'):
            #job = {}
            #print(totalCount + 5)
            #job['data'] = r.data.text
                    #job['title'] = r.postingtitle and \
                    #r.postingtitle.text or r.retailpostingtitle.text
                    #job['location'] = r.location.text
            #jobs.append(job)

                # Next page
            #totalCount += 1
            #print(totalCount + 6)
            #self.search_request['totalCount'] = totalCount

        return jobs

if __name__ == '__main__':
    scraper = AppleJobsScraper()
    scraper.scrape()
