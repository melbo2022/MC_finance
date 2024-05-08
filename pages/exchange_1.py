#USD.CNY.INRから通貨を選択し、グラフとデータフレームを表示する


import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

import pandas as pd

# Streamlitアプリのタイトルを設定
st.title('為替グラフとデータフレーム')
# セレクトボックスを作成し、ユーザーの選択を取得
currency_code = st.selectbox('Select currency', ('USD', 'CNY', 'INR'))
currency_display = currency_code 

# 選択された通貨に対する通貨ペアを作成
currency_pair = f'{currency_code}JPY=X' if currency_code != 'USD' else 'JPY=X'

# ユーザーが期間を選択できるようにする
start_date = st.date_input('Start date', value=pd.to_datetime('2023-12-01'))
end_date = st.date_input('End date', value=pd.to_datetime('2024-04-30'))    


# 通貨ペアの為替レートの履歴データを取得
data = yf.download(currency_pair, start=start_date, end=end_date)

# インデックスから時刻を削除
data.index = data.index.date

# Streamlitアプリのタイトルを設定
if currency_code == 'USD':
    st.subheader('USD to JPY Rate Over Time')
elif currency_code == 'CNY':
    st.subheader('CNY to JPY Rate Over Time')
elif currency_code == 'INR':
    st.subheader('INR to JPY Rate Over Time')

# 終値のグラフを描画
data['Close'].plot()
plt.title(f'{currency_display.encode("utf-8").decode("utf-8")} to JPY Rate Over Time')  
plt.xlabel('Date')
plt.ylabel('Rate')

# Streamlitでグラフを表示
st.pyplot(plt)

# データフレームとして表示（高さのスクロールバーあり、幅を広げる）
st.dataframe(data, height=600, width=800)

