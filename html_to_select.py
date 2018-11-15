import os
os.system('cls') # clear terminal

#turns bs object into s-sheet panda dataframe
from sys import argv
import pandas as pd
import html5lib
from bs4 import BeautifulSoup

def html_to_select(html,threshold,sector):
    with open(html, "r") as file:
        soup = BeautifulSoup(file,'lxml')
        table = soup.find('p').get_text()
        df = pd.read_json(table)

        data = df['data']

        clean = []

        for i in range(len(data)):
            cell = data.ix[i]['d']
            clean.append(cell)

        clean_data = pd.DataFrame.from_records(clean)

        clean_data_map = clean_data.iloc[:, [0,6,10]]

        #select stock below market cap threshold
        select_mkt_cap = clean_data_map[clean_data_map.iloc[:,1] < threshold]

        #select stock of given sector
        select_sector = select_mkt_cap[clean_data_map.iloc[:,2] == sector]

        print(select_sector)

html_to_select("tview_scan.html",300e10,"Healthcare")
