# Stock analysis project
Semester-2 project for course CSEN1021, This project is a small interactive web-app for stock analysis, using the [Streamlit library](https://github.com/streamlit/streamlit) for a simple frontend, fetching stock data using the [Yfinance library](https://github.com/ranaroussi/yfinance), analyzing the stock data using [pandas](https://github.com/pandas-dev/pandas) and plotting graphs using [Streamlit plots](https://docs.streamlit.io/library/api-reference/charts), [Matplotlib](https://github.com/matplotlib/matplotlib), and [Seaborn](https://github.com/mwaskom/seaborn).

## Functionality:

- Sidebar used to input stocks and select a time frame along with type of plots (streamlit plots or matplotlib plots).

### The stock analysis methods and visualizations are split into 9 tabs which display the visualized data:

- Dashboard:

  - Shows the adjusted closing prices for both stocks along with a metric widget to show the percentage change in the stock that is also color coded and changes based on the positive or negative delta.

  - Shows the volume weighted average price (VWAP) for both stocks with a simple uptrend or downtrend analysis on the parameters of close price being higher or lower than the volume weighted average price.

  - Shows the daily returns of both stocks as a bar chart.

- Closing price:

  - Adjusted closing price of both stocks are plotted seperately and also overlayed for comparison.

- Moving average:

  - The slider is used to selected the parameter for the moving average calculation and the moving average for both graphs is plotted overlayed with the closing price.

  - Checkbox below to calculate multiple moving averages for different time frames can also allow for the calculation and plotting of 3 moving averages with 3 sliders for changing the parameters.


- Stock volume:

  - Volume of both stocks are plotted seperately and also overlayed for comparison.

- Daily return:

  - Daily return of both stocks is calculated and plotted as a scatter plot along with two histograms with bell curves overlaid to check the sharpness of the peak.

- Volume weighted average price:

  - Volume weighted average price of both stocks is calculated and plotted along with the closing price for comparison.

- Correlation:

  - Correlation between two stocks is calculated and represented as Pearson Coefficient(R) along with a joint scatter plot to visualize the correlation.

- Volatility:

  - Stock volatility is calculated and plotted as a line chart seperately and together for comparison.

- Risk and return:

  - Risk and return of both stocks is calculated and plotted using a scatter plot with labels for the stocks. 

### Project snapshots:
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/eb2eecfc-6f3d-4238-a578-d88563e96eef)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/c0715078-1708-40bc-a337-d6ae8bb74231)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/d543028d-3130-43d3-959d-0901b35ed38d)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/709c8fd1-9e04-45b5-891c-a90dcdd248f8)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/3ed4f954-ec75-4777-8684-47793bfee60d)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/0c00ca62-ee6f-4b3a-97c6-0b194c35fc07)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/4c3f3c02-7b22-4596-8f21-b759a3e37d83)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/50fc6c9e-f1e1-4791-9ce9-fa9182e333b9)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/0cb8620b-6fbf-4069-b176-49f9425deb79)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/89f81ad3-bf8c-4d1f-bd36-03a0abc618cd)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/08c5c759-3bff-4636-9279-856775232b03)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/73a30a19-2eda-487f-9896-e0dfe3fbe925)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/6e089b54-24ea-493b-88c9-37039629d95f)
![image](https://github.com/lakshman-sweetpeaches/Stock-analysis-project/assets/142110475/b8a10d40-bdde-4c73-9cb5-8e2fc240e648)
