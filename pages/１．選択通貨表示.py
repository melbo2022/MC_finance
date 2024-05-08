#USD,CNY,INRにつき、選択をしてグラフとデータフレームを表示する

import streamlit as st
import yfinance as yf
import plotly.express as px
import pandas as pd

# Streamlitアプリのタイトルを設定
st.header('Currency Graph and Dataframe by selection ')

# セレクトボックスを作成し、ユーザーの選択を取得
currency_code = st.selectbox('Select currency', ('USD', 'CNY', 'INR'))
currency_display = currency_code

# 選択された通貨に対する通貨ペアを作成
currency_pair = f'{currency_code}JPY=X' if currency_code != 'USD' else 'JPY=X'

# ユーザーが期間を選択できるようにする（数値入力形式）
# ユーザーが日付を入力する形式にする
start_date = st.text_input('Start date', '2024/04/01')
end_date = st.text_input('End date', '2024/04/30')

# 入力された日付を datetime オブジェクトに変換
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# 通貨ペアの為替レートの履歴データを取得
data = yf.download(currency_pair, start=start_date, end=end_date)

# Streamlitアプリのタイトルを設定
if currency_code == 'USD':
    st.subheader('USD to JPY Rate')
elif currency_code == 'CNY':
    st.subheader('CNY to JPY Rate')
elif currency_code == 'INR':
    st.subheader('INR to JPY Rate')

# Plotly Expressを使って為替レートの時系列グラフを作成
fig = px.line(data, x=data.index, y='Close')
fig.update_xaxes(title='Date')
fig.update_yaxes(title='Rate')
st.plotly_chart(fig)

# データフレームとして表示（高さのスクロールバーあり、幅を広げる）
st.dataframe(data, height=600, width=800)
