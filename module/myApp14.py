
import streamlit as st
import time

cont = st.container()
cont.write('This is container.')

c1, c2, _, _ = st.columns([1,1,1,4])
start = c1.button('start', key=1) # 버튼을 누르면 true가 됨.
clear = c2.button('restart', key=2)


# start 버튼을 눌렀을 때 empty 공간에 카운트다운이 1초 간격으로 진행되는 코드
if start:
    with cont:
        for i in range(6):
            cnt = 5 - i
            cont.write(f'countdown {cnt}sec')
            time.sleep(1)
        cont.write('countdown inside an empty complete!')

# clear 버튼을 누르면 해당 공간에 있는 내용들을 비워주는 코드
if clear:
    cont.container() # container는 초기화를 시켜도 내부값을 완전히 다 없애지 못하고 초기 write문의 문자열은 남아있음.
