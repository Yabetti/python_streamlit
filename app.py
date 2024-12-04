import streamlit as st
import func as f

input_num = st.number_input('Input a number', value=0)

result = input_num ** 2
st.write('Result: ', result)


# テキストボックスの表示
user_input = st.text_input("文字を入力してください:", "")

# 入力された文字を表示
if user_input:
    st.write(f"入力された文字: {f.addInputStr(user_input)}")
