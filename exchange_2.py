#USD,CNY,INRにつき、グラフとデータフレームを表示する

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

import pandas as pd

# Streamlitアプリのタイトルを設定
st.title('為替グラフとデータフレーム')
# ユーザーが期間を選択できるようにする
start_date = st.date_input('Start date', value=pd.to_datetime('2023-12-01'))
end_date = st.date_input('End date', value=pd.to_datetime('2024-04-30'))

currency_list=['USD', 'CNY', 'INR']

if st.button('Show exchange rates'):
    currency_pair_list=[]
    for currency_code in currency_list:
        # 通貨に対する通貨ペアを作成
        currency_pair = f'{currency_code}JPY=X' 
        currency_pair_list.append(currency_pair)

    for currency_pair in currency_pair_list:
        # 新しい図を作成(これがないとグラフが重なってしまう)
        fig = plt.figure()

        # 通貨ペアの為替レートの履歴データを取得
        data = yf.download(currency_pair, start=start_date, end=end_date)

        # インデックスから時刻を削除
        data.index = data.index.date

        # 終値のグラフを描画
        plt.plot(data.index, data['Close'])
        plt.title(f'{currency_pair} Rate Over Time')  
        plt.xlabel('Date')
        plt.ylabel('Rate')

        # Streamlitでグラフを表示
        st.pyplot(fig)

        # データフレームとして表示（高さのスクロールバーあり、幅を広げる）
        st.dataframe(data, height=600, width=800)
