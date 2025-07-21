
import streamlit as st
import time
import pandas as pd

'How to use Session2'
''

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
           st.write(f'my name is {name2}, i am {age2}years old, and i am a {gender2}')
# doClicked의 return값이 False라면
else:
    # 폼 보이기 버튼을 누르면 if문이 동작함.
    if st.button('show form'):
        st.session_state['clicked'] = True # session에 clicked가 없다가 True로 저장됨.
        # rerun: app 재실행(웹 브라우저를 끈 것이 아니므로 세션 상태는 유지됨.)
        st.rerun() # 다시 실행되어서 if문을 실행
