import json

dic = {"filter":
    [{"left":"market_cap_basic","operation":"nempty"},
    {"left":"type","operation":"in_range","right":["stock","dr","fund"]},
    {"left":"subtype","operation":"in_range","right":["common","","etf","unit"]},
    {"left":"exchange","operation":"in_range","right":["NYSE","NASDAQ","AMEX"]}],
    "symbols":
        {"query":{"types":[]},"tickers":[]},
        "columns":["name","close","change","change_abs","Recommend.All","volume","market_cap_basic","price_earnings_ttm","earnings_per_share_basic_ttm","number_of_employees","sector","description","name","type","subtype","pricescale","minmov","fractional","minmove2"],
        "sort":{"sortBy":"market_cap_basic","sortOrder":"desc"},
        "options":{"lang":"en"},"range":[0,150]
        }
