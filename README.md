### What is Stock Market Portfolio Optimization?

There are many different theories about Stock Market Portfolio Optimization. So many so, that there are entire industries built on selling financial products that maximize returns while minimizing risk. 
The truth is that it impossible for the average US citizen to predict the markets direction. As a result, we can only hope to minimize risk and maximize return based on historical performance. Although historical performance does not indicate future returns, I think valuable insight could be provided by analyzing the historical returns of different balanced portfolios based on their past performance. Instead of informing me on which stocks are best to be purchased today, I can use it as an activity to see how diversification can protect the downside and still provide substantial returns. 


### How to implement in Python?

1. Use yfinance API to extract historical stock market performance of selected tickers.
2. Clean and rearrange the data
3. Plot the data in a human digestable and easy to understand fashion. 

### Roadblocks to cleaning the yfianance data

The yfinance dataframe was a multi-indexed data frame meaning it was difficult to distuinguisg between the different columns of data and plot meaningful trends, like price over time.

As a result.
Cleaning the data was difficult, but I learned a lot about manipulating dataframes. See my steps below: 

#### Mutli-Indexed Dataframe

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Original_DF.jpg">
    <img alt="Reset Index Dataframe" src="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Original_DF.jpg">
</picture>

#### Reset Index Dataframe

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Reset_DF.jpg">
    <img alt="Reset Index Dataframe" src="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Reset_DF.jpg">
</picture>



#### Flattened Dataframe

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Flattened_DF.jpg">
    <img alt="Reset Index Dataframe" src="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Flattened_DF.jpg">
</picture>


#### Melted Dataframe

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Melted_DF.jpg">
    <img alt="Reset Index Dataframe" src="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Melted_DF.jpg">
</picture>



#### Split Dataframe

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Split_DF.jpg">
    <img alt="Reset Index Dataframe" src="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Split_DF.jpg">
</picture>



#### Pivotted Dataframe

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Pivotted_DF.jpg">
    <img alt="Reset Index Dataframe" src="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Pivotted_DF.jpg">
</picture>


### Modern Portfoil Theory

    Calculate the expected returns and volatility for each stock.
    Generate a series of random portfolios to identify the efficient frontier.
    Optimize the portfolio to maximize the Sharpe ratio, which is a measure of risk-adjusted return.
    
### Visualizing the data to provide insights

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Top_Market_Cap_Portfolio.jpg">
    <img alt="Reset Index Dataframe" src="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Top_Market_Cap_Portfolio.jpg">
</picture>

<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Index_Portfolio.jpg">
    <img alt="Reset Index Dataframe" src="https://github.com/danielsbrown3/Pictures/blob/440544d94cbb2d7b2289f347860febcfcadd0c25/Index_Portfolio.jpg">
</picture>
