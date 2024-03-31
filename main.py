import streamlit as st
from datetime import date
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Web app title and tabs initialization
st.set_page_config(layout="wide", page_title="Stock Analysis")
st.title("Stock Analysis")
st.caption("-Project by Lakshman Pentyala")
tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9=st.tabs(["Dashboard","Closing Prices","Moving average","Stock Volume","Daily Return","Volume Weighted Average Price","Correlation","Stock Volatility","Risk and Return"])

#Stock inputs
with st.sidebar:
    
    st.subheader("Stock data input")
    c1,c2=st.columns(2)
    stock1=c1.text_input('Stock 1:')
    stock2=c2.text_input('Stock 2:')
    stocknamelist=[stock1,stock2]#List of stock names
    start_date=date(2019, 3, 17)
    end_date=date.today()
    SELECTED_DATE=st.slider("Select a start date",start_date,end_date,format="YYYY/MM/DD")
    TODAY=date.today().strftime("%Y-%m-%d")
    
    #@st.cache_data, caching data does not allow values to update according to date change
    def load_stock_data(ticker):
        data=yf.download(ticker, SELECTED_DATE, TODAY)#Data is retrieved as a pandas Data Frame
        return data
    
    if stock1 and stock2:
        data_load_state=st.text("Loading data...")
        stockdata1=load_stock_data(stock1)
        stockdata2=load_stock_data(stock2)
        data_load_state.text("Data loaded successfully.")
        stockdatalist=[stockdata1,stockdata2]#List of stock dataframes
        
        
        with st.expander("See raw stock data"):
            st.subheader('Raw data stock1')
            st.write(stockdata1.head(10))#Streamlit can natively handle pandas dataframe
            st.subheader('Raw data stock2')
            st.write(stockdata2.head(10))

        st.divider()

        showmatplot=st.checkbox("Show matplotlib graphs instead")

if stock1 and stock2:
    
    with tab2:
        
        def plotting_closing_data():
            
            if not showmatplot:
                
                closingdf=pd.DataFrame({f"{stock1} Adj Close": stockdata1['Adj Close'],f"{stock2} Adj Close": stockdata2['Adj Close']})
                st.line_chart(closingdf, x=None, y=[f"{stock2} Adj Close",f"{stock1} Adj Close"], color=("#f55361","#7ecaed"))
            
            else:
                
                fig, axes = plt.subplots(nrows=1, ncols=1)
                fig.set_figheight(7)
                fig.set_figwidth(15)
                
                stockdata1['Adj Close'].plot()
                
                stockdata2['Adj Close'].plot()
                
                fig.legend([stock1,stock2],loc="upper center")
                fig.tight_layout()
                st.pyplot(plt.gcf())


        
        def plotting_closing_adjacent():
            
            if not showmatplot:
                
                adjcloseg1,adjcloseg2=st.columns(2)
                
                adjcloseg1.text(stock1)
                adjcloseg1.line_chart(stockdata1['Adj Close'],color="#f55361")
                
                adjcloseg2.text(stock2)
                adjcloseg2.line_chart(stockdata2['Adj Close'],color="#7ecaed")
            
            else:
                
                fig, axes = plt.subplots(nrows=2, ncols=1)
                fig.set_figheight(10)
                fig.set_figwidth(15)
                
                stockdata1['Adj Close'].plot(ax=axes[0],color="red")
                axes[0].set_title(stock1)
                
                stockdata2['Adj Close'].plot(ax=axes[1],color="blue")
                axes[1].set_title(stock2)
                
                fig.tight_layout()
                st.pyplot(plt.gcf()) #Get current figure function from matplotlib returns plotted graph as a figure

        
        st.subheader('Line graph of stocks')
        plotting_closing_data()
        
        st.subheader('Adjacent graphs of closing price')
        plotting_closing_adjacent()


    with tab3:
        
        #Plotting moving average of both stocks with one range slider
        st.subheader('Moving average')
        ma_timeperiod=st.slider("Time period:",1,365)
        
        def plotting_ma():
            
            for company in stockdatalist:
                column_name=f"MA for {ma_timeperiod} days"
                company[column_name]=company['Adj Close'].rolling(ma_timeperiod).mean()
            
            if not showmatplot:
                st.subheader(stock1)
                st.line_chart(stockdata1[['Adj Close',f"MA for {ma_timeperiod} days"]],color=["#f55361","#fc8f28"])
                
                st.subheader(stock2)
                st.line_chart(stockdata2[['Adj Close',f"MA for {ma_timeperiod} days"]],color=["#7ecaed","#fc8f28"])
            
            else:    
                
                fig, axes = plt.subplots(nrows=2, ncols=1)
                fig.set_figheight(10)
                fig.set_figwidth(15)
                
                stockdata1[['Adj Close', f'MA for {ma_timeperiod} days']].plot(ax=axes[0])
                axes[0].set_title(stock1)
                
                stockdata2[['Adj Close', f'MA for {ma_timeperiod} days']].plot(ax=axes[1])
                axes[1].set_title(stock2)
                
                fig.tight_layout()
                st.pyplot(plt.gcf())
        
        plotting_ma()
        
        #plotting multiple moving averages with 3 range sliders
        showcombined = st.checkbox('Show combined moving average for different timeframes')
        if showcombined:
            
            st.subheader("Combined graphs of moving average for different time periods")
            ma_timeperiod1=st.slider("Time period 1:",1,365)
            ma_timeperiod2=st.slider("Time period 2:",1,365)
            ma_timeperiod3=st.slider("Time period 3:",1,365)
            ma_list=[ma_timeperiod1, ma_timeperiod2, ma_timeperiod3]
            
            def plotting_multiple_ma():
                
                for ma in ma_list:
                    for company in stockdatalist:
                        column_name=f"MA for {ma} days"
                        company[column_name]=company['Adj Close'].rolling(ma).mean()
                
                if not showmatplot:
                    
                    st.subheader(stock1)
                    st.line_chart(stockdata1[['Adj Close', f'MA for {ma_timeperiod1} days',f'MA for {ma_timeperiod2} days',f'MA for {ma_timeperiod3} days']],color=["#f55361","#fc8f28","#12e091","#7e11d6"])
                    
                    st.subheader(stock2)
                    st.line_chart(stockdata2[['Adj Close', f'MA for {ma_timeperiod1} days',f'MA for {ma_timeperiod2} days',f'MA for {ma_timeperiod3} days']],color=["#7ecaed","#fc8f28","#12e091","#7e11d6"])
                
                else:
                    
                    fig, axes = plt.subplots(nrows=2, ncols=1)
                    fig.set_figheight(10)
                    fig.set_figwidth(15)
                    
                    stockdata1[['Adj Close', f'MA for {ma_timeperiod1} days',f'MA for {ma_timeperiod2} days',f'MA for {ma_timeperiod3} days']].plot(ax=axes[0])
                    axes[0].set_title(stock1)
                    
                    stockdata2[['Adj Close', f'MA for {ma_timeperiod1} days',f'MA for {ma_timeperiod2} days',f'MA for {ma_timeperiod3} days']].plot(ax=axes[1])
                    axes[1].set_title(stock2)
                    
                    fig.tight_layout()
                    st.pyplot(plt.gcf())
            
            plotting_multiple_ma()


    with tab4:
        
        def plotting_stock_volume_combined():
            
            if not showmatplot:
                
                volumedf=pd.DataFrame({f"{stock1} Volume": stockdata1['Volume'],f"{stock2} Volume": stockdata2['Volume']})
                st.line_chart(volumedf, x=None, y=[f"{stock2} Volume",f"{stock1} Volume"], color=("#f55361","#7ecaed"))
            
            else:
                
                fig, axes = plt.subplots(nrows=1, ncols=1)
                fig.set_figheight(7)
                fig.set_figwidth(15)
                
                stockdata1['Volume'].plot()
                
                stockdata2['Volume'].plot()
                
                fig.legend([stock1,stock2],loc="upper center")
                fig.tight_layout()
                st.pyplot(plt.gcf())
        
        st.subheader("Graph of stock volume")
        plotting_stock_volume_combined()
        
        showseparate=st.checkbox('Show stock volume graphs separately')
        if showseparate:
            
            st.subheader("Adjacent view of both stock volume graphs")
            
            def plotting_stock_volume_separate():
                
                if not showmatplot:
                    
                    volg1,volg2=st.columns(2)
                    
                    volg1.text(f"Volume of {stock1}")
                    volg1.line_chart(stockdata1['Volume'],color="#f55361")
                    
                    volg2.text(f"Volume of {stock2}")
                    volg2.line_chart(stockdata2['Volume'],color="#7ecaed")
                
                else:
                    
                    fig, axes = plt.subplots(nrows=2, ncols=1)
                    fig.set_figheight(10)
                    fig.set_figwidth(15)
                    
                    stockdata1['Volume'].plot(ax=axes[0],color="red")
                    axes[0].set_title(f'Volume of {stock1} stocks sold')
                    
                    stockdata2['Volume'].plot(ax=axes[1],color="blue")
                    axes[1].set_title(f'Volume of {stock2} stocks sold')
                    
                    fig.tight_layout()
                    st.pyplot(plt.gcf())
            
            plotting_stock_volume_separate()

    with tab5:
        
        def plotting_daily_return():
            
            for stock in stockdatalist:
                stock['Daily Return']=stock['Adj Close'].pct_change()
            
            if not showmatplot:
                
                st.scatter_chart(stockdata1['Daily Return'],color="#f55361")
                st.scatter_chart(stockdata2['Daily Return'],color="#7ecaed")
            
            else:
                
                fig, axes = plt.subplots(nrows=2, ncols=1)
                fig.set_figheight(15)
                fig.set_figwidth(15)
                
                stockdata1['Daily Return'].plot(ax=axes[0], legend=True,linestyle='-',marker='o').axhline(y = 0, color = 'red', linestyle = '-') 
                axes[0].set_title(stock1)
                
                stockdata2['Daily Return'].plot(ax=axes[1], legend=True, linestyle='--', marker='o',color='orange').axhline(y = 0, color = 'red', linestyle = '-') 
                axes[1].set_title(stock2)
                
                fig.tight_layout()
                st.pyplot(plt.gcf())
            
        
        st.subheader("Scatter plot of daily return of stocks")
        plotting_daily_return()
        
        def daily_return_hist():
            
            fig, axes = plt.subplots(nrows=2, ncols=1)
            fig.set_figheight(10)
            fig.set_figwidth(15)
            plt.style.use("dark_background")

            sns.histplot(data=stockdata1['Daily Return'], ax=axes[0], bins=50, color="tomato", kde=True)
            plt.xlabel('Daily Return')
            plt.ylabel('Counts')
            axes[0].set_title(stock1)
            fig.tight_layout()

            sns.histplot(data=stockdata2['Daily Return'], ax=axes[1], bins=50, color="turquoise", kde=True)
            plt.xlabel('Daily Return')
            plt.ylabel('Counts')
            axes[1].set_title(stock2)
            fig.tight_layout()
            
            st.pyplot(plt.gcf())
        
        st.subheader("Histogram of daily return of stocks")
        daily_return_hist()

    with tab6:
        
        def plotting_vwap():
            
            for stock in stockdatalist:
                stock['VWAP']=(((stock['High']+stock['Low']+stock['Close'])/3)*stock['Volume']).cumsum()/stock['Volume'].cumsum()
            
            if not showmatplot:
                
                st.subheader(stock1)
                st.line_chart(stockdata1[['VWAP','Close']],color=["#f55361","#fc8f28"])
                
                st.subheader(stock2)
                st.line_chart(stockdata2[['VWAP','Close']],color=["#7ecaed","#fc8f28"])
            
            else:
                
                fig, axes = plt.subplots(nrows=2, ncols=1)
                fig.set_figheight(10)
                fig.set_figwidth(15)
                
                stockdata1[['VWAP','Close']].plot(ax=axes[0],color=["red","orange"])
                axes[0].set_title(f'Volume Weighted Average Price pf {stock1}')
                
                stockdata2[['VWAP','Close']].plot(ax=axes[1],color=["blue","purple"])
                axes[1].set_title(f'Volume Weighted Average Price pf {stock2}')
                
                fig.tight_layout()
                st.pyplot(plt.gcf())
        
        plotting_vwap()

    with tab7:
        
        st.subheader(f"Stock correlation between {stock1} and {stock2}")
        
        stock1rename=stockdata1.rename(columns={'Adj Close':stock1})
        stock2rename=stockdata2.rename(columns={'Adj Close':stock2}) 
        pctchangedf=pd.concat([stock1rename[stock1].pct_change(),stock2rename[stock2].pct_change()],axis=1)
        
        pearsondf=pctchangedf.corr(method='pearson')
        st.caption("Pearson coefficient (R)")
        st.write(pearsondf[0:1][stock2])
        
        plot1,plot2=st.columns(2)
        plt.style.use("dark_background")
        
        plot1.caption("Complete correlation example")
        sns.jointplot(x=stock1, y=stock1, data=pctchangedf, kind='scatter')
        plot1.pyplot(plt.gcf())
        
        plot2.caption(f"correlation between {stock1} and {stock2}")
        sns.jointplot(x=stock1, y=stock2, data=pctchangedf, kind='scatter', color='seagreen')
        plot2.pyplot(plt.gcf())
    
    with tab8:
        
        volatilitydf=pd.DataFrame({f"{stock1} Volatility": pctchangedf[stock1].rolling(7).std()*np.sqrt(7),f"{stock2} Volatility": pctchangedf[stock2].rolling(7).std()*np.sqrt(7)})
        volatility1,volatility2=st.columns(2)
        
        volatility1.subheader(f"Volatility of {stock1}")
        volatility1.line_chart(volatilitydf[f'{stock1} Volatility'],color="#f55361")

        volatility2.subheader(f"Volatility of {stock2}")
        volatility2.line_chart(volatilitydf[f'{stock2} Volatility'],color="#7ecaed")

        st.divider()
        st.subheader("Overlay")
        
        st.line_chart(volatilitydf, x=None, y=[f"{stock2} Volatility",f"{stock1} Volatility"], color=("#f55361","#7ecaed"))

    with tab9:
        
        area = np.pi * 20
        plt.figure(figsize=(10, 8))
        plt.scatter(pctchangedf.mean(), pctchangedf.std(), s=area)
        plt.xlabel('Expected return')
        plt.ylabel('Risk')
        for label, x, y in zip(pctchangedf.columns, pctchangedf.mean(), pctchangedf.std()):
            plt.annotate(label, xy=(x, y), xytext=(50, 50), textcoords='offset points', ha='right', va='bottom', 
            arrowprops=dict(arrowstyle='-', color='blue', connectionstyle='arc3,rad=-0.3'))
        st.pyplot(plt.gcf())


    with tab1:
        st.header("Dashboard:")
        
        percent_change_stock1=round(((stockdata1['Daily Return'].iloc[-1])*100),2)
        percent_change_stock2=round(((stockdata2['Daily Return'].iloc[-1])*100),2)
        
        if(percent_change_stock1>=0):
            stock1colour="#5DBB63"
        else:
            stock1colour="#FF0000"
        
        if(percent_change_stock2>=0):
            stock2colour="#5DBB63"
        else:
            stock2colour="#FF0000"
        
        col1,col2=st.columns(2)
        
        col1.metric("Stock 1", stock1, f"{percent_change_stock1}%")
        col2.metric("Stock 2", stock2, f"{percent_change_stock2}%") 
        
        col1.line_chart(stockdata1['Adj Close'],color=stock1colour)
        col2.line_chart(stockdata2['Adj Close'],color=stock2colour)
        
        st.divider()

        column1,column2=st.columns(2)
        
        column1.subheader(f"Volume weighted Average Price of {stock1}")
        column1.line_chart(stockdata1[['Adj Close','VWAP']])

        column2.subheader(f"Volume weighted Average Price of {stock2}")
        column2.line_chart(stockdata2[['Adj Close','VWAP']])

        if (stockdata1['Adj Close'].iloc[-1]>stockdata1['VWAP'].iloc[-1]):
            column1.metric(stock1,"Close price below VWAP","+Probable uptrend")
        else:
            column1.metric(stock1,"Close price above VWAP","-Probable downtrend")

        if (stockdata2['Adj Close'].iloc[-1]>stockdata2['VWAP'].iloc[-1]):
            column2.metric(stock1,"Close price below VWAP","+Probable uptrend")
        else:
            column2.metric(stock2,"Close price above VWAP","-Probable downtrend")

        st.divider()

        column_1,column_2=st.columns(2)
        
        column_1.subheader(f"Daily returns of {stock1}")
        column_1.bar_chart(stockdata1['Daily Return'],color="#7ecaed")
        
        column_2.subheader(f"Daily returns of {stock2}")
        column_2.bar_chart(stockdata2['Daily Return'],color="#f55361")
else:
        st.warning('Stock input is empty', icon="⚠️")