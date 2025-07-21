
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

# form 미적용
# 값을 변경할 때마다 웹사이트가 새로 로딩됨...
st.subheader('no form')
name1 = st.text_input("What's your name?")
age1 = st.slider('How old r you?', 20, 40, 30)
gender1 = st.radio('What is you gender?',['M', 'F'])
st.write(get_data(name1, age1, gender1))

# 버튼을 눌러 폼을 보는 경우에 아래처럼 코드를 작성하면 제출하기 버튼을 누를 때 폼이 사라짐.
# 제출 버튼을 누를 때 웹 통신이 발생하면서 기존 변수 값들이 초기화되고 유지되지 않게 됨.
# st.subheader('with form')
# with st.form(key = 'form1', clear_on_submit=True):
#    name2 = st.text_input("What's your name?")
#    age2 = st.slider('How old r you?', 20, 40, 30)
#    gender2 = st.radio('What is you gender?',['M', 'F'])
#    submit_button = st.form_submit_button('submit!!')

#    if submit_button:
#        st.write(get_data(name2, age2, gender2))

# form과 버튼을 같이 활용하기 위해 세션을 사용하는 사용자 정의 함수
# True, False와 같은 논리값들을 세션으로 유지시켜줌으로써 버튼과 폼을 함께 사용하게 구성할 수 있음.
def doClicked():
    # get: 파이썬 기초의 get을 본따 만든 함수
    # session_state에서 key값을 검색하는 함수(key명칭, 해당 key가 없을 때 반환되는 값)
    return st.session_state.get('clicked', False)

# doClicked의 return값이 True라면
# 처음에는 session에 clicked 키 값이 없어서 False가 반환되므로 if문 대신 else문이 실행됨.
if doClicked():
    with st.form(key = 'form1', clear_on_submit=True):
       name2 = st.text_input("What's your name?")
       age2 = st.slider('How old r you?', 20, 40, 30)
       gender2 = st.radio('What is you gender?',['M', 'F'])
       submit_button = st.form_submit_button('submit!!')
    
       if submit_button:
           st.write(get_data(name2, age2, gender2))
# doClicked의 return값이 False라면
else:
    # 폼 보이기 버튼을 누르면 if문이 동작함.
    if st.button('show form'):
        st.session_state['clicked'] = True # session에 clicked가 없다가 True로 저장됨.
        # rerun: app 재실행(웹 브라우저를 끈 것이 아니므로 세션 상태는 유지됨.)
        st.rerun()
