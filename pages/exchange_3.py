#3つの通貨のグラフを横並びに表示する

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

import pandas as pd


# Streamlitアプリのタイトルを設定
st.title('為替グラフ')
# ユーザーが期間を選択できるようにする
start_date = st.date_input('Start date', value=pd.to_datetime('2023-12-01'))
end_date = st.date_input('End date', value=pd.to_datetime('2024-04-30'))

currency_list=['USD', 'CNY', 'INR']

currency_pair_list=[]
for currency_code in currency_list:
    # 通貨に対する通貨ペアを作成
    currency_pair = f'{currency_code}JPY=X' 
    currency_pair_list.append(currency_pair)

#グラフを格納するリスト
fig_list = []
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

    #grafをリストに追加
    fig_list.append(fig)


# グラフを横に並べて表示
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

#fig_listの中身を確認
print(fig_list)

#fig_listの中のグラフを横並びに表示
for i in range(len(fig_list)):
    axs[i].plot(fig_list[i].axes[0].get_lines()[0].get_xdata(), fig_list[i].axes[0].get_lines()[0].get_ydata())
    axs[i].set_title(f'Graph {i+1}')

st.pyplot(fig)
