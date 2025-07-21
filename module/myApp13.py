
import streamlit as st
import time

emp = st.empty()
emp.write('This is empty.')

c1, c2, _, _ = st.columns([1,1,1,4])
start = c1.button('start', key=1) # 버튼을 누르면 true가 됨.
clear = c2.button('restart', key=2)


# start 버튼을 눌렀을 때 empty 공간에 카운트다운이 1초 간격으로 진행되는 코드
if start:
    with emp:
        for i in range(6):
            cnt = 5 - i
            emp.write(f'countdown {cnt}sec')
            time.sleep(1)
        emp.write('countdown inside an empty complete!') # with문에 종속된 상태로는 emp, st둘 다 사용가능

# clear 버튼을 누르면 해당 공간에 있는 내용들을 비워주는 코드
if clear:
    emp.empty() # empty 내용 초기화
    emp.write('This is empty.') # 맨 처음 출력문 그대로 재출력
