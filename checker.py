import pandas
import sys
import yahoo_fin.stock_info as si

def main():
    if(len(sys.argv) != 2):
        sys.exit("Please provide csv file name")
    csv = sys.argv[1]

    df = pandas.read_csv(csv)
    for i in range(len(df['Symbol'])):
        #update last price for each ticker in this loop
        ticker = df['Symbol'][i]
        # print(f"{ticker} = {si.get_live_price(ticker)}")
        df['Last Price'][i] = si.get_live_price(ticker)
        
    df.to_csv("UpdatedPrices.csv")

if __name__ == "__main__":
    main()