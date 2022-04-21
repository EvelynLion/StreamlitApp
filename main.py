import streamlit as st
import datetime as dt
import pandas_datareader.data as web

tuple_currency = ("USD", "CAD", "EUR")
dict_currency = {"USD": "BTC-USD", "CAD": "BTC-CAD", "EUR": "BTC-EUR"}
param_days = (0, 255, 60)

def getData(opt, n_d):
    dt_end = dt.date.today()
    dt_bgn = dt_end - dt.timedelta(days=n_d)
    df = web.get_data_yahoo(dict_currency[opt], start=dt_bgn, end=dt_end)
    df.drop(["Volume", "Adj Close"], axis=1, inplace=True)
    return df

st.title("Bitcoin Price Trend")

if st.button("REFRESH"):
    now = dt.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    st.write(f"Market Data Updated at{now}")

currency = st.sidebar.selectbox(
    "Currency",
    tuple_currency)
st.sidebar.write('You selected:', currency)

n_days = st.slider('Number of Days', param_days[0], param_days[1], param_days[2])

df_plot = getData(currency, n_days)
st.line_chart(df_plot)