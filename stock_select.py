# Description: 会社名を選択してyahoo financeから株価データを取得し、表示するアプリケーション

import streamlit as st
import yfinance as yf
import pandas as pd

# 候補となる要素のリスト（漢字で表記された会社名とそのティッカーシンボル）
options = {
    'トヨタ自動車': '7203.T',
    'ソニー': '6758.T',
    'パナソニック': '6752.T',
    '任天堂': '7974.T',
    '日産自動車': '7201.T',
    '本田技研工業': '7267.T',
    '東京電力': '9501.T',
    '日本電気': '6701.T',
    '三菱電機': '6503.T',
    '富士通': '6702.T'
}

# ユーザーが会社を選択
selected_company = st.selectbox('Select a company', list(options.keys()))

# ユーザーが期間を選択
start_date = st.date_input('Start date')
end_date = st.date_input('End date')

if start_date < end_date:
    # 選択された会社のティッカーシンボルを取得
    ticker_symbol = options[selected_company]

    # Yahoo Financeから株価データを取得
    data = yf.download(ticker_symbol, start=start_date, end=end_date)

    # 株価データを表示
    st.line_chart(data['Close'])

    
else:
    st.write('Error: End date must be greater than start date.')