import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
from datetime import date
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
from plotly import graph_objs as go

# import cufflinks as cf
# App title
st.markdown('''
# Stock Price Prediction App
- Shown are the stock price prediction data for query companies
- Built in `Python` using `streamlit`,`yfinance`, `fbprophet`, `pandas` ,`plotly` and `datetime`
''')
st.write('---')

# START = "2000-01-01"
# TODAY = date.today().strftime("%Y/%m/%d")
# Sidebar
st.sidebar.subheader('Query parameters')
start_date = st.sidebar.date_input("Start date", datetime.datetime(2010, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.datetime(2021, 12, 31))

# Retrieving tickers data
ticker_list = pd.read_csv('ticker_symbol.csv')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list) # Select ticker symbol

n_years = st.slider("Years of prediction:", 1 , 3)
period = n_years * 365

tickerData = yf.Ticker(tickerSymbol) # Get ticker data
#tickerDf = tickerData.history(period='1d', start_date, end_date) # get the historical prices for this ticker

@st.cache
def load_data(ticker):
    data = yf.download(ticker, start_date, end_date)
    data.reset_index(inplace=True)
    return data

data_load_state = st.text("Load data...")
data = load_data(tickerSymbol)
data_load_state.text("Done!")

# Ticker information
string_logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

string_name = tickerData.info['longName']
st.header('**%s**' % string_name)

#string_summary = tickerData.info['longBusinessSummary','']
#st.info(string_summary)

# Ticker data
st.subheader('Ticker data')
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

plot_raw_data()

# Forecasting
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

st.subheader("Forecast data")
st.write(forecast.tail())

fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.write('Forecast component')
fig2 = m.plot_components(forecast)
st.write(fig2)
# Ticker data
#st.header('**Ticker data**')
#st.write(tickerDf)

# Bollinger bands
#st.header('**Bollinger Bands**')
#qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
#qf.add_bollinger_bands()
#fig = qf.iplot(asFigure=True)
#st.plotly_chart(fig)

####
#st.write('---')
#st.write(tickerData.info)
