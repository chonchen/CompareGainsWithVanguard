import yfinance as yf
import pandas as pd
from dateutil import parser
from datetime import date, timedelta

def main():
    all = pd.read_csv('VTSMX.csv')
    start_date = parser.parse(all.tail(1).Date.values[0]) + timedelta(1)
    end_date = date.today() + timedelta(1)
    print(start_date)
    print(end_date)
    data = yf.download('VTSMX', start=start_date, end=end_date)
    data.to_csv('VTSMX.csv', mode='a', header=False)

if __name__ == '__main__':
    main()

