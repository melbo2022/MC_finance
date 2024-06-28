#4つのペアのうち、2つづつの比較を行う

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go

# Streamlitアプリのタイトルを設定
st.header('Two Currency comparison')

# 開始日と終了日の入力欄を設定
# start_date = st.date_input('Start date', value=pd.to_datetime('2023-12-01'))
# end_date =  st.date_input('End date', value=pd.to_datetime('2024-02-14'))

# ユーザーが日付を入力する形式にする
start_date = st.text_input('Start date', '2023/12/01')
end_date = st.text_input('End date', '2024/05/31')

# 入力された日付を datetime オブジェクトに変換
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# データの取得とグラフの作成
@st.cache_resource
def get_currency_data(start, end):
    usd_data = yf.download('USDJPY=X', start=start, end=end)
    cny_data = yf.download('CNYJPY=X', start=start, end=end)
    inr_data = yf.download('INRJPY=X', start=start, end=end)
    ngn_data = yf.download('NGNJPY=X', start=start, end=end)
    return usd_data, cny_data, inr_data, ngn_data

usd_data, cny_data, inr_data,ngn_data = get_currency_data(start_date, end_date)

# NGNJPYのデータから3月14日のデータを除外
ngn_data = ngn_data[ngn_data.index != '2024-03-14']
#--------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------
fig4 = go.Figure()

# USDJPYとNGNJPYのデータを追加
fig4.add_trace(go.Scatter(x=usd_data.index, y=usd_data['Close'], mode='lines', name='USDJPY', yaxis='y'))
fig4.add_trace(go.Scatter(x=cny_data.index, y=ngn_data['Close'], mode='lines', name='NGNJPY', yaxis='y2'))

# レイアウトの設定
fig4.update_layout(
    title="USDJPYとNGNJPYの比較",
    yaxis=dict(title="USDJPY", side="left", position=0.05),
    yaxis2=dict(title="NGNJPY", side="right", overlaying="y", position=0.95),
    xaxis=dict(title="Date")
)

# グラフを表示
st.plotly_chart(fig4)

#-----------------------------------------------------------------------------------------------------




