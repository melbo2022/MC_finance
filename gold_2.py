#金の価格と豪ドルをplotlyで描画する

import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# ユーザーが期間を選択
start_date = st.date_input('Start date', value=pd.to_datetime('2023-12-01'))
end_date =  st.date_input('End date', value=pd.to_datetime('2024-02-14'))

if start_date < end_date:  

    # Yahoo Financeから金の価格データを取得
    gold_data = yf.download('GC=F', start=start_date, end=end_date)

    #タイトルを表示
    st.title('Gold Price')
    
    # Plotlyでグラフを描画
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=gold_data.index, y=gold_data['Close'], mode='lines', name='Gold Price'))
    fig.update_layout(xaxis_title='Date', yaxis_title='Price ($)', title='Gold Price')
    st.plotly_chart(fig)

    # Yahoo Financeからドル/円の為替レートを取得
    exchange_rate = yf.download('JPY=X', start=start_date, end=end_date)

    #タイトルを表示
    st.title('USD/JPY Exchange Rate')
    
    # Plotlyでグラフを描画
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=exchange_rate.index, y=exchange_rate['Close'], mode='lines', name='USD/JPY Exchange Rate'))
    fig.update_layout(xaxis_title='Date', yaxis_title='Exchange Rate', title='USD/JPY Exchange Rate')
    st.plotly_chart(fig)

    # 金の価格を円換算
    gold_data_jpy = gold_data['Close'] * exchange_rate['Close']

    #タイトルを表示
    st.title('Gold Price in JPY')
    
    # Plotlyでグラフを描画
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=gold_data_jpy.index, y=gold_data_jpy, mode='lines', name='Gold Price in JPY'))
    fig.update_layout(xaxis_title='Date', yaxis_title='Price (JPY)', title='Gold Price in JPY')
    st.plotly_chart(fig)

    # Yahoo Financeから豪ドル/円の為替レートを取得
    exchange_rate_aud_jpy = yf.download('AUDJPY=X', start=start_date, end=end_date)

    #タイトルを表示
    st.title('AUD/JPY Exchange Rate')
    
    # Plotlyでグラフを描画
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=exchange_rate_aud_jpy.index, y=exchange_rate_aud_jpy['Close'], mode='lines', name='AUD/JPY Exchange Rate'))
    fig.update_layout(xaxis_title='Date', yaxis_title='Exchange Rate', title='AUD/JPY Exchange Rate')
    st.plotly_chart(fig)

else:
    st.write('Error: End date must be greater than start date.')
