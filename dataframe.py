import pandas as pd
from datetime import datetime, timedelta

from pandas._libs.tslibs import Timestamp

def main():
    df = pd.read_csv('VTSMX.csv')
    trx_df = pd.read_csv('transactions.csv')
    df['Date_Val'] = df.Date.apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))
    trx_df['Date_Val'] = trx_df.Date.apply(lambda x: datetime.strptime(x, '%Y-%m-%d'))

    trx_df['Shares'] = trx_df.apply(lambda x: get_number_of_shares(get_price_on_date(x.Date_Val, df), x.Amount), axis=1)
    total_shares = trx_df.Shares.sum()
    print(get_total_funds(total_shares, df))

def get_price_on_date(trx_date: Timestamp, data_frame: pd.DataFrame) -> float:
    if trx_date.weekday() == 5:
        trx_date += timedelta(2)
    elif trx_date.weekday() == 6:
        trx_date += timedelta(1)
    

    adj_close = data_frame[data_frame.Date_Val == trx_date]['Adj Close']

    if len(adj_close) > 0:
        return adj_close.values[0]
    return None

def get_number_of_shares(price: float, money: float) -> float:
    return money / price

def get_total_funds(num_shares: float, data_frame: pd.DataFrame) -> float:
    latest_price = data_frame.tail(1)['Adj Close'].values[0]
    return num_shares * latest_price

if __name__ == '__main__':
    main()