
import streamlit as st
import time
import numpy as np
import pandas as pd

@st.cache_data
def get_data(name, age, gender):
    my_info = {'name':name,'age':age,'gender': gender}
    df = pd.DataFrame(my_info, index=['member info'])
    time.sleep(3)
    return df

st.subheader('with form')
with st.form(key = 'form1', clear_on_submit=True): # clear_on_submit=True: 제출 버튼을 누르면 위젯에 들어있는 값들이 다시 초기값으로 돌아옴.
   name2 = st.text_input("What's your name?")
   age2 = st.slider('How old r you?', 20, 40, 30)
   gender2 = st.radio('What is you gender?',['M', 'F'])
   submit_button = st.form_submit_button('submit!!')

   if submit_button:
       st.write(get_data(name2, age2, gender2))
