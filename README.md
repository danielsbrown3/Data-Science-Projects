What is Stock Market Portfolio Optimization?

After reading Capital by Thomas Picketty, a book which 
There are many different theories about Stock Market Portfolio Optimization. So many so that there are entire industries built on selling financial products that maximize returns while minimizing risk. 
The truth is that it impossible for the average US citizen to predict the markets direction. As a result, we can only hope to minimize risk and maximize return based on historical performance. 


How to implement implementation in Python?


Roadblocks to cleaning the yfianance data

Mutli-Indexed Dataframe

|   Date     | Adj Close (AAPL)\  Open (AAPL)    | Adj Close (MSFT) Open (MSFT) | Adj Close (VOO) Open (VOO)   |
|             High (AAPL)         High (MSFT)       | High (VOO)        |
|             Low (AAPL)          Low (MSFT)        | Low (VOO)         |
|             Volume (AAPL)      Volume (MSFT)     | Volume (VOO)      |
|------------|--------------------|-------------------|-------------------|
| 2023-08-10 | 177.029846         | 320.423401        | 458.8300          |
| 2023-08-11 | 177.089615         | 318.518341        | 291.7900          |
| ...        | ...                | ...               | ...               |


Reset Index Dataframe

|   Date     |   (AAPL, Open)     |   (MSFT, Open)    |   (VOO, Open)     |
|            |   (AAPL, High)     |   (MSFT, High)    |   (VOO, High)     |
|            |   (AAPL, Low)      |   (MSFT, Low)     |   (VOO, Low)      |
|            |   (AAPL, Volume)   |   (MSFT, Volume)  |   (VOO, Volume)   |
--------------------------------------------------------------------------
| 2023-08-10 | 177.029846         | 320.423401        | 458.8300          |
| 2023-08-11 | 177.089615         | 318.518341        | 291.7900          |


Flattened Dataframe

|   Date     | AAPL_Open  | MSFT_Open  | VOO_Open   |
|            | AAPL_High  | MSFT_High  | VOO_High   |
|            | AAPL_Low   | MSFT_Low   | VOO_Low    |
|            | AAPL_Volume| MSFT_Volume| VOO_Volume |
-----------------------------------------------------
| 2023-08-10 | 177.029846 | 320.423401 | 458.8300   |
| 2023-08-11 | 177.089615 | 318.518341 | 291.7900   |

Melted Dataframe

|   Date     | Attribute_Ticker    |  Value |
---------------------------------------------
| 2023-08-10 | AAPL_Open           | 177.03 |
| 2023-08-10 | MSFT_Open           | 320.42 |
| 2023-08-10 | VOO_Open            | 458.83 |
| 2023-08-10 | AAPL_High           | 177.09 |
| ...        | ...                 | ...    |


Split Dataframe

|   Date     | Ticker  | Attribute | Value |
--------------------------------------------
| 2023-08-10 | AAPL    | Open    | 177.03 |
| 2023-08-10 | MSFT    | Open    | 320.42 |
| 2023-08-10 | VOO     | Open    | 458.83 |
| 2023-08-10 | AAPL    | High    | 177.09 |
| ...        | ...     | ...     | ...    |


Pivotted Dataframe


|   Date     | Ticker  |  Open   |  High   |  Low    | Volume  |
----------------------------------------------------------------
| 2023-08-10 | AAPL    | 177.03  | 177.09  | 176.50  | 54686900|
| 2023-08-10 | MSFT    | 320.42  | 321.50  | 319.00  | 20113700|
| 2023-08-10 | VOO     | 458.83  | 460.50  | 457.00  | 4588300 |
| ...        | ...     | ...     | ...     | ...     | ...     |



Modern Portfoil Theory

    Calculate the expected returns and volatility for each stock.
    Generate a series of random portfolios to identify the efficient frontier.
    Optimize the portfolio to maximize the Sharpe ratio, which is a measure of risk-adjusted return.
    
Visualizing the data to provide insights


