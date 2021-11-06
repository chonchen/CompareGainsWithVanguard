import yfinance as yf

def main():
    data = yf.download('VTSMX', period='max')
    data.to_csv('VTSMX.csv')

if __name__ == '__main__':
    main()
