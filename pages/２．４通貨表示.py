#USD,CNY,INRにつき、３つのグラフとデータフレームを表示する

import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import pandas as pd

# Streamlitアプリのタイトルを設定
st.header('Four Currency Graphs and Dataframes')

# ユーザーが日付を入力する形式にする
start_date = st.text_input('Start date', '2023/12/01')
end_date = st.text_input('End date', '2024/05/31')

# 入力された日付を datetime オブジェクトに変換
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

currency_list = ['USD', 'CNY', 'INR','NGN']

currency_pair_list = []
for currency_code in currency_list:
    # 通貨に対する通貨ペアを作成
    currency_pair = f'{currency_code}JPY=X'
    currency_pair_list.append(currency_pair)

for currency_pair in currency_pair_list:
    # 通貨ペアの為替レートの履歴データを取得
    data = yf.download(currency_pair, start=start_date, end=end_date)

    # 3月14日のデータを除外
    if currency_pair == 'NGNJPY=X':
        data = data[data.index != '2024-03-14']

    # インデックスから時刻を削除
    data.index = data.index.date

    # Plotlyの図を作成
    fig = go.Figure()

    # 終値のグラフを追加
    fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close'))

    # レイアウトを設定
    fig.update_layout(title=f'{currency_pair} Rate Over Time',
                      xaxis_title='Date',
                      yaxis_title='Rate')

    # StreamlitでPlotlyのグラフを表示
    st.plotly_chart(fig)

    # データフレームとして表示（高さのスクロールバーあり、幅を広げる）
    st.dataframe(data, height=600, width=800)
