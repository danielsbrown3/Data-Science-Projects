import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
from datetime import date, timedelta\

# Define the time period for the data
end_date = date.today().strftime("%Y-%m-%d") # End date is today
start_date = (date.today() - timedelta(days=7200)).strftime("%Y-%m-%d") # Start date is 20 years prior to today

# List of stock tickers
tickers_individual = ['BRK-B', 'MSFT','AAPL','AMZN','GOOG','NVDA']
tickers_indexes = ['^SPX','^MID','^SP600','^NSEI']


def stockOptimization(tickers, end_date, start_date):
    data = yf.download(tickers, start=start_date, end=end_date, progress=True)
    data = data.reset_index()

    # Rename columns
    data.columns = ['_'.join(col).strip() if isinstance(col, tuple) else col for col in data.columns]

    # Melt the DataFrame
    data_melted = data.melt(id_vars=['Date_'], var_name='Attribute_Ticker', value_name='Value')

    # Split the combined column into Attribute and Ticker
    data_melted[['Attribute', 'Ticker']] = data_melted['Attribute_Ticker'].str.split('_', expand=True)

    # Drop the combined column if it's no longer needed
    data_melted = data_melted.drop(columns=['Attribute_Ticker'])

    # Pivot the melted DataFrame to have the attributes (Open, High, Low, etc.) as columns
    data_pivoted = data_melted.pivot_table(index=['Date_', 'Ticker'], columns='Attribute', values='Value', aggfunc='first')

    # Reset index to turn multi-index into columns
    stock_data = data_pivoted.reset_index()
    stock_data['Date_'] = pd.to_datetime(stock_data['Date_'])

    stock_data.set_index('Date_', inplace=True)
    stock_data.reset_index(inplace=True)

    # Prepare the subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("Stock Optimization Analysis")

    sns.set(style='whitegrid')

    # Ensure axes is flattened and contains individual axes objects
    axes = axes.ravel()

    # Price History Plot
    sns.lineplot(ax=axes[0], data=stock_data, x='Date_', y='Adj Close', hue='Ticker')
    axes[0].set_title("Price History")
    axes[0].set_xlabel('Date')
    axes[0].set_ylabel('Adjusted Close Price')
    axes[0].grid(True)
    axes[0].tick_params(axis='x', rotation=45)

    # Daily Returns
    stock_data.set_index('Date_', inplace=True)
    stock_data['Daily Return'] = stock_data.groupby('Ticker')['Adj Close'].pct_change()

    daily_returns = stock_data.pivot_table(index='Date_', columns='Ticker', values='Daily Return')
    correlation_matrix = daily_returns.corr()

    # Correlation Plot
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5, fmt='.2f', annot_kws={"size": 10}, ax=axes[1])
    axes[1].set_title("Correlation")
    axes[1].tick_params(axis='x', rotation=90)
    axes[1].tick_params(axis='y', rotation=0)

    # Efficient Frontier Plot
    expected_returns = daily_returns.mean() * 252  # annualize the returns
    volatility = daily_returns.std() * np.sqrt(252)  # annualize the volatility

    num_portfolios = 50000
    results = np.zeros((3, num_portfolios))
    cov_matrix = daily_returns.cov() * 252

    np.random.seed(42)
    for i in range(num_portfolios):
        weights = np.random.random(len(tickers))
        weights /= np.sum(weights)

        portfolio_return, portfolio_volatility = np.dot(weights, expected_returns), np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        results[0, i] = portfolio_return
        results[1, i] = portfolio_volatility
        results[2, i] = portfolio_return / portfolio_volatility  # Sharpe Ratio

    axes[2].scatter(results[1, :], results[0, :], c=results[2, :], cmap='YlGnBu', marker='o')
    axes[2].set_title("Efficient Frontier")
    axes[2].set_xlabel('Volatility (Standard Deviation)')
    axes[2].set_ylabel('Expected Return')
    axes[2].grid(True)

    max_sharpe_idx = np.argmax(results[2])
    max_sharpe_weights = np.zeros(len(tickers))

    for i in range(num_portfolios):
        weights = np.random.random(len(tickers))
        weights /= np.sum(weights)

        portfolio_return, portfolio_volatility = np.dot(weights, expected_returns), np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))

        if results[2, i] == results[2, max_sharpe_idx]:
            max_sharpe_weights = weights
            break

    portfolio_weights_df = pd.DataFrame({
        'Ticker': tickers,
        'Weight': max_sharpe_weights
    })

    # Portfolio Allocation Plot
    axes[3].pie(portfolio_weights_df['Weight'], labels=portfolio_weights_df['Ticker'], autopct='%1.1f%%')
    axes[3].set_title("Portfolio Allocation")

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    
    return fig, max_sharpe_idx, results[0, max_sharpe_idx], results[1, max_sharpe_idx]

fig_individual, max_sharpe_individual, volatility_individual, return_individual = stockOptimization(tickers_individual,end_date,start_date)
plt.show()
fig_index, max_sharpe_index, volatility_index, return_index = stockOptimization(tickers_indexes,end_date,start_date)
plt.show()

print(f"Individual portolio: Max Return {return_individual:.2%} Max Volatility: {volatility_individual:.2%}.\nIndex portolio:      Max Return {return_index:.2%} Max Volatility: {volatility_index:.2%}.")