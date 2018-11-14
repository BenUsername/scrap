import os
os.system('cls') # clear terminal

#turns bs object into s-sheet panda dataframe
from sys import argv
import pandas as pd
import html5lib
from bs4 import BeautifulSoup

with open("tview_scan.html", "r") as file:
        soup = BeautifulSoup(file,'lxml')
        table = soup.find('p').get_text()
        df = pd.read_json(table)
        data = df.ix[:, 'data']
        row = df.ix[0, 'data']['d']

        print(type(row))
