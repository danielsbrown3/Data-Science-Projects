import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
from datetime import date, timedelta\

# Define the time period for the data
end_date = date.today().strftime("%Y-%m-%d") # End date is today
start_date = (date.today() - timedelta(days=7200)).strftime("%Y-%m-%d") # Start date is 1 year prior to today

# List of stock tickers
tickers = ['BRK-B', 'MSFT', 'NFTY', 'VOO', '^SP600','AMZN','GOOG']

# The data frame provided from Yfinance is Multi-indexed data meaning that we must clean it before we can analyze, optimize, and plot our data. 
# Multi-indexed means that each column will have more than one variable:
# For example -> Adj Close (MSFT) There are two key points of data in this one column, that 
# the data is the adjusted close and more specifically it is for the company Microsoft. 

# Download data from YFinance
data = yf.download(tickers, start=start_date, end=end_date, progress=True)


# Data indexes by the Date instead of having the Date as its own column
# Resetting the index will index each row linearly and set Date as a column
# resetting will also seperate the two variables in each column Adj Close (MSFT) will become (MSFT,Adj Close)
data = data.reset_index()


# Flatten the 
data.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in data.columns]

# Melt the DataFrame
data_melted = data.melt(id_vars=['Date_'], var_name='Attribute_Ticker', value_name='Value')

# Split the combined column into Attribute and Ticker
data_melted[['Attribute', 'Ticker']] = data_melted['Attribute_Ticker'].str.split('_', expand=True)

# Drop the combined column if it's no longer needed
data_melted = data_melted.drop(columns=['Attribute_Ticker'])


# pivot the melted DataFrame to have the attributes (Open, High, Low, etc.) as columns
data_pivoted = data_melted.pivot_table(index=['Date_', 'Ticker'], columns='Attribute', values='Value', aggfunc='first')

# reset index to turn multi-index into columns
stock_data = data_pivoted.reset_index()

print(stock_data.head())


stock_data['Date_'] = pd.to_datetime(stock_data['Date_'])

stock_data.set_index('Date_',inplace=True)
stock_data.reset_index(inplace=True)

plt.figure(figsize=(14,7))
sns.set(style='whitegrid')

sns.lineplot(data=stock_data,x='Date_',y='Adj Close',hue ='Ticker',marker='o')

plt.title('Adjusted Close Price Over Time', fontsize = 16)
plt.xlabel('Date',fontsize = 14)
plt.ylabel('Adjusted Close Price', fontsize =14)
plt.legend(title='Ticker',title_fontsize='13',fontsize='11')
plt.grid(True)

plt.xticks(rotation=45)

plt.show()

short_window = 50
long_window = 200

stock_data.set_index('Date_', inplace=True)
unique_tickers = stock_data['Ticker'].unique()

for ticker in unique_tickers:
    ticker_data = stock_data[stock_data['Ticker'] == ticker].copy()
    

stock_data['Daily Return'] = stock_data.groupby('Ticker')['Adj Close'].pct_change()


daily_returns = stock_data.pivot_table(index='Date_', columns='Ticker', values='Daily Return')
correlation_matrix = daily_returns.corr()

plt.figure(figsize=(12, 10))
sns.set(style='whitegrid')

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5, fmt='.2f', annot_kws={"size": 10})
plt.title('Correlation Matrix of Daily Returns', fontsize=16)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()


expected_returns = daily_returns.mean() * 252  # annualize the returns
volatility = daily_returns.std() * np.sqrt(252)  # annualize the volatility

stock_stats = pd.DataFrame({
    'Expected Return': expected_returns,
    'Volatility': volatility
})

print(stock_stats)


def portfolio_performance(weights, returns, cov_matrix):
    portfolio_return = np.dot(weights, returns)
    portfolio_volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return portfolio_return, portfolio_volatility

# number of portfolios to simulate
num_portfolios = 50000

# arrays to store the results
results = np.zeros((3, num_portfolios))

# annualized covariance matrix
cov_matrix = daily_returns.cov() * 252

np.random.seed(42)

for i in range(num_portfolios):
    weights = np.random.random(len(unique_tickers))
    weights /= np.sum(weights)

    portfolio_return, portfolio_volatility = portfolio_performance(weights, expected_returns, cov_matrix)

    results[0,i] = portfolio_return
    results[1,i] = portfolio_volatility
    results[2,i] = portfolio_return / portfolio_volatility  # Sharpe Ratio

plt.figure(figsize=(10, 7))
plt.scatter(results[1,:], results[0,:], c=results[2,:], cmap='YlGnBu', marker='o')
plt.title('Efficient Frontier')
plt.xlabel('Volatility (Standard Deviation)')
plt.ylabel('Expected Return')
plt.colorbar(label='Sharpe Ratio')
plt.grid(True)
plt.show()

max_sharpe_idx = np.argmax(results[2])
max_sharpe_return = results[0, max_sharpe_idx]
max_sharpe_volatility = results[1, max_sharpe_idx]
max_sharpe_ratio = results[2, max_sharpe_idx]

print(max_sharpe_return, max_sharpe_volatility, max_sharpe_ratio)

max_sharpe_weights = np.zeros(len(unique_tickers))

for i in range(num_portfolios):
    weights = np.random.random(len(unique_tickers))
    weights /= np.sum(weights)

    portfolio_return, portfolio_volatility = portfolio_performance(weights, expected_returns, cov_matrix)

    if results[2, i] == max_sharpe_ratio:
        max_sharpe_weights = weights
        break

portfolio_weights_df = pd.DataFrame({
    'Ticker': unique_tickers,
    'Weight': max_sharpe_weights
})

plt.pie(portfolio_weights_df['Weight'],labels = portfolio_weights_df['Ticker'])
plt.show()
print(portfolio_weights_df)