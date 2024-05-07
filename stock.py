#

import streamlit as st
import pandas as pd
import numpy as np
import datetime
import pandas_datareader.data as web
import yfinance as yf
import matplotlib.pyplot as plt

# アプリケーションのタイトルを設定
st.title('日本株価アプリ')
#日本株の銘柄コードと会社名をセットにした辞書を作成
stock_dict = {
    'トヨタ自動車': '7203.T',
    '日産自動車': '7201.T',
    'ホンダ': '7267.T',
    'スズキ': '7269.T',
    'マツダ': '7261.T',
    'SUBARU': '7270.T',
    '三菱自動車': '7211.T',
    'いすゞ自動車': '7202.T',
    'ダイハツ工業': '7262.T',
    '日野自動車': '7205.T',
    'トヨタ紡織': '3116.T',
    'トヨタ車体': '7206.T',
    'デンソー': '6902.T',
    'アイシン精機': '7259.T',
    'ジェイテクト': '6473.T',
    '新明和工業': '7222.T',
    '新日本製鐵': '5401.T',
    '神戸製鋼所': '5406.T',
    '日本製鋼所': '5631.T',
    '住友金属工業': '5405.T',
    '日本軽金属': '5706.T',
    '三井金属鉱業': '5706.T',
    '古河電気工業': '5801.T',
    '住友電気工業': '6501.T',
    '東芝': '6502.T',
    '日立製作所': '6501.T',
    'パナソニック': '6752.T',
    'シャープ': '6753.T',
    '日本電気': '6701.T',
    '富士通': '6702.T',
    'NECネッツエスアイ': '6701.T',
    '東京エレクトロン': '8035.T',
    '京セラ': '6971.T'}

#日本株を取得しデータフレームを作成
yf.pdr_override()
start = datetime.datetime(2019, 1, 1)
end = datetime.datetime(2023, 12, 31)
#日本株のデータを取得
#stock_dictのキーをリスト化し、セレクトボックスを作成
selected_stock = st.selectbox('銘柄を選択してください', list(stock_dict.keys()))
#選択した銘柄のコードを取得
stock = stock_dict[selected_stock]
#データを取得
df = web.get_data_yahoo(stock, start, end)

#データフレームを表示
#st.write(df)

#取得した株の名前を取得し変数へ代入
stock_name = yf.Ticker(stock)
#株の名前を表示
st.write(stock_name.info['longName'])

#データフレームを折れ線グラフで表示
plt.plot(df['Close'])
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Stock Price')
plt.xticks(rotation=45)

#stock_nameをグラフのタイトルに設定
plt.title(stock_name.info['longName'])
#グラフを表示
st.pyplot(plt)











