#３つのペアのうち、2つづつの比較を行う

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# Streamlitアプリのタイトルを設定
st.title('為替変動比較')

# 開始日と終了日の入力欄を設定
start_date = st.date_input('Start date', value=pd.to_datetime('2023-12-01'))
end_date =  st.date_input('End date', value=pd.to_datetime('2024-02-14'))

# データの取得とグラフの作成
@st.cache_resource
def get_currency_data(start, end):
    usd_data = yf.download('USDJPY=X', start=start, end=end)
    cny_data = yf.download('CNYJPY=X', start=start, end=end)
    inr_data = yf.download('INRJPY=X', start=start, end=end)
    return usd_data, cny_data, inr_data

usd_data, cny_data, inr_data = get_currency_data(start_date, end_date)

fig1 = go.Figure()

# USDJPYとCNYJPYのデータを追加
fig1.add_trace(go.Scatter(x=usd_data.index, y=usd_data['Close'], mode='lines', name='USDJPY', yaxis='y'))
fig1.add_trace(go.Scatter(x=cny_data.index, y=cny_data['Close'], mode='lines', name='CNYJPY', yaxis='y2'))

# レイアウトの設定
fig1.update_layout(
    title="USDJPYとCNYJPYの比較",
    yaxis=dict(title="USDJPY", side="left", position=0.05),
    yaxis2=dict(title="CNYJPY", side="right", overlaying="y", position=0.95),
    xaxis=dict(title="Date")
)

# グラフを表示
st.plotly_chart(fig1)

fig2 = go.Figure()

# USDJPYとINRJPYのデータを追加
fig2.add_trace(go.Scatter(x=usd_data.index, y=usd_data['Close'], mode='lines', name='USDJPY', yaxis='y'))
fig2.add_trace(go.Scatter(x=inr_data.index, y=inr_data['Close'], mode='lines', name='INRJPY', yaxis='y2'))

# レイアウトの設定
fig2.update_layout(
    title="USDJPYとINRJPYの比較",
    yaxis=dict(title="USDJPY", side="left", position=0.05),
    yaxis2=dict(title="INRJPY", side="right", overlaying="y", position=0.95),
    xaxis=dict(title="Date")
)

# グラフを表示
st.plotly_chart(fig2)

fig3 = go.Figure()

# CNYJPYとINRJPYのデータを追加
fig3.add_trace(go.Scatter(x=cny_data.index, y=cny_data['Close'], mode='lines', name='CNYJPY', yaxis='y'))
fig3.add_trace(go.Scatter(x=inr_data.index, y=inr_data['Close'], mode='lines', name='INRJPY', yaxis='y2'))

# レイアウトの設定
fig3.update_layout(
    title="CNYJPYとINRJPYの比較",
    yaxis=dict(title="CNYJPY", side="left", position=0.05),
    yaxis2=dict(title="INRJPY", side="right", overlaying="y", position=0.95),
    xaxis=dict(title="Date")
)

# グラフを表示
st.plotly_chart(fig3)
