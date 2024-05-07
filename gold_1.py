#金の価格と豪ドルをmatplotlibで描画する

import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# ユーザーが期間を選択
start_date = st.date_input('Start date', value=pd.to_datetime('2023-12-01'))
end_date =  st.date_input('End date', value=pd.to_datetime('2024-02-14'))

if start_date < end_date:  

    # Yahoo Financeから金の価格データを取得
    gold_data = yf.download('GC=F', start=start_date, end=end_date)

    #タイトルを表示
    st.title('Gold Price')
    
    # Matplotlibでグラフを描画
    plt.figure(figsize=(10, 6))
    plt.plot(gold_data.index, gold_data['Close'], label='Gold Price')
    plt.xlabel('Date')
    plt.ylabel('Price ($)')
    plt.title('Gold Price')
    plt.legend()
    st.pyplot(plt)

    # Yahoo Financeからドル/円の為替レートを取得
    exchange_rate = yf.download('JPY=X', start=start_date, end=end_date)

    #タイトルを表示
    st.title('USD/JPY Exchange Rate')
    
    # Matplotlibでグラフを描画
    plt.figure(figsize=(10, 6))
    plt.plot(exchange_rate.index, exchange_rate['Close'], label='USD/JPY Exchange Rate')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.title('USD/JPY Exchange Rate')
    plt.legend()
    st.pyplot(plt)

    # 金の価格を円換算
    gold_data_jpy = gold_data['Close'] * exchange_rate['Close']

    #タイトルを表示
    st.title('Gold Price in JPY')
    
    # Matplotlibでグラフを描画
    plt.figure(figsize=(10, 6))
    plt.plot(gold_data_jpy.index, gold_data_jpy, label='Gold Price in JPY')
    plt.xlabel('Date')
    plt.ylabel('Price (JPY)')
    plt.title('Gold Price in JPY')
    plt.legend()
    st.pyplot(plt)

    # Yahoo Financeから豪ドル/円の為替レートを取得
    exchange_rate_aud_jpy = yf.download('AUDJPY=X', start=start_date, end=end_date)

    #タイトルを表示
    st.title('AUD/JPY Exchange Rate')
    
    # Matplotlibでグラフを描画
    plt.figure(figsize=(10, 6))
    plt.plot(exchange_rate_aud_jpy.index, exchange_rate_aud_jpy['Close'], label='AUD/JPY Exchange Rate')
    plt.xlabel('Date')
    plt.ylabel('Exchange Rate')
    plt.title('AUD/JPY Exchange Rate')
    plt.legend()
    st.pyplot(plt)

else:
    st.write('Error: End date must be greater than start date.')





