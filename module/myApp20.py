
import streamlit as st
import time
import pandas as pd

st.title('Streamlit cache test')

# 사용자 정의 함수에 캐시 선언(데코레이션)
@st.cache_data
def cal_sum(a,b):
    time.sleep(5)
    return a+b

# 숫자 2개 입력 받기
a = st.number_input('첫번째 숫자 입력', min_value = 0, max_value = 10, step = 1)
b = st.number_input('두번째 숫자 입력', min_value = 0, max_value = 10, step = 1)

# 버튼으로 함수 계산 실행
button_start = st.button('start calculate', key = 1)
if button_start:
    result = cal_sum(a,b)
    st.write(f'result: {result}')


# 캐시 삭제 버튼 추가
# 캐시가 있는 모든 정보 삭제됨;;;;
button_clear = st.button('캐시 삭제', key=2)
if button_clear:
    st.cache_data.clear() # 전체 캐시 삭제
    st.write('cache deleted complete!')

@st.cache_data
def get_data(age):
    my_info = {'name':'Clover','age':age,'gender':'female'}
    df = pd.DataFrame(my_info, index=['member info'])
    time.sleep(3)
    return df
""
myAge = st.slider('input age', 20, 40, 30)
""
button_age = st.button('input and run!', key = 3)
if button_age:
    result = get_data(myAge)
    st.write(result)

# 특정 함수만 캐시 초기화를 하고 싶다면? @st.cache_data가 쓰인 함수의 캐시만 삭제
# 위의 cache_data.clear()가 적용된 버튼을 한번 누르면 웹 페이지 내의 모든 캐시가 초기화되기 때문에 불편함.
# 버튼 함수 내에 사용자 정의 함수명.clear로 지정 후 아래 조건문에서 .clear()로 실행
button_clear2 = st.button('캐시 삭제', key=4, on_click = get_data.clear)
if button_clear2:
    get_data.clear()
    st.write('cache deleted complete!')
