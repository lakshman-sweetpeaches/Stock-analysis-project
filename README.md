# Stock analysis project
 Semester 2 Python project, This project is a small interactive web-app for stock analysis, using the [Streamlit library](https://github.com/streamlit/streamlit) for a simple frontend, fetching stock data using the [Yfinance library](https://github.com/ranaroussi/yfinance), analyzing the stock data using [pandas](https://github.com/pandas-dev/pandas) and plotting graphs using [Streamlit plots](https://docs.streamlit.io/library/api-reference/charts), [Matplotlib](https://github.com/matplotlib/matplotlib), and [Seaborn](https://github.com/mwaskom/seaborn).

## Functionality:
The stock analysis methods and visualizations are split into 9 tabs which display the visualized data after two stock codes are entered in the side bar and the time range is set:
- Dashboard:
  -Shows the adjusted closing prices for both stocks along with a metric widget to show the percentage change in the stock that is also color coded and changes based on the positive or negative delta.
  -Shows the volume weighted average price (VWAP) for both stocks with a simple uptrend or downtrend analysis on the parameters of close price being higher or lower than the volume weighted average price.
  -Shows the daily returns of both stocks as a bar chart.

- Closing price:
  -Adjusted closing price of both stocks are plotted seperately and also overlayed for comparison.

- Moving average:
  -The slider is used to selected the parameter for the moving average calculation and the moving average for both graphs is plotted overlayed with the closing price.
  -Checkbox below to calculate multiple moving averages for different time frames can also allow for the calculation and plotting of 3 moving averages with 3 sliders for changing the parameters.

- Stock volume:
  - Volume of both stocks are plotted seperately and also overlayed for comparison.

- Daily return:
  -Daily return of both stocks is calculated and plotted as a scatter plot along with two histograms with bell curves overlaid to check the sharpness of the peak.

- Volume weighted average price:
  -Volume weighted average price of both stocks is calculated and plotted along with the closing price for comparison.

- Correlation:
  -Correlation between two stocks is calculated and represented as Pearson Coefficient(R) along with a joint scatter plot to visualize the correlation.

- Volatility:
  -Stock volatility is calculated and plotted as a line chart seperately and together for comparison.

- Risk and return:
  -Risk and return of both stocks is calculated and plotted using a scatter plot with labels for the stocks. 
