# 入力した文字に基づいて候補となる要素をフィルタリングし、ドロップダウンボックスで選択する

import streamlit as st

# 候補となる要素のリスト（漢字で表記された会社名）
options = ['トヨタ自動車', 'ソニー', 'パナソニック', '任天堂', '日産自動車', '本田技研工業', '東京電力', '日本電気', '三菱電機', '富士通']

# ユーザーの入力を受け取るテキストボックス
input_text = st.text_input('Enter a letter or word')

# 入力された文字に基づいて候補となる要素をフィルタリング
filtered_options = [option for option in options if input_text in option]

# ドロップダウンボックスで候補となる要素を表示
selected_option = st.selectbox('Select an option', filtered_options)

# 選択された要素を表示
st.write('You selected:', selected_option)