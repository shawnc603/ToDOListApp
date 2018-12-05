
from flask import Flask, request, render_template, session, flash, redirect, url_for, jsonify, Blueprint, json
from TODOLISTAPP.config import Config
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs4

scraping = Blueprint('scraping', __name__)

@scraping.route('/viewStockTicker', methods=['GET'])
def viewStockTicker():
    quote_page = 'https://money.cnn.com/data/markets/'
    r = requests.get(quote_page)
    soup = bs4(r.text, 'html.parser')
    results =  soup.find_all('div', attrs={'class':'module-body row tickers'})
    x = results[0].find_all('li', attrs={'class':'column'})

    records = []
    for item in x:
        name = item.find('span', attrs={'class':'ticker-name'})
        change1 = item.find('span', attrs={'class':'ticker-name-change'})
        tickerpoints = item.find('span', attrs={'class':'ticker-points'})
        change2  = item.find('span', attrs={'class':'ticker-points-change'})
        records.append((name.text,change1.text,tickerpoints.text,change2.text))

    df = pd.DataFrame(records, columns=['Market', 'ticker change', 'ticker points', 'ticker points change'])
    return render_template("stocks.html",data=df.to_json())
    #return df.to_html()