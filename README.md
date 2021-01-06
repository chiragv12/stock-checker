# stock-checker
Python program that reads from a csv of tickers and gives the latest price of each

## To run the program
Create a virtual environment named *venv*  
Then run
```
pip install requirements.txt
python3 checker.py <filename>
```
The program will create a csv called UpdatedPrices.csv in the root folder.

## CSV Formatting
For the program to work the csv will need a column called *Symbol* that contains the ticker, and a column named *Last Price*  
### An example csv can be as follows:
```
Symbol,Last Price
aapl, 50
amzn, 50
goog, 35
tsla, 9
nio, 1
```
