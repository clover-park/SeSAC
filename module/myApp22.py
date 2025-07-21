
import streamlit as st
import time
import pandas as pd

'How to use Session'
''

st.write('세션에 아무것도 없는 초기 상태:', st.session_state)
# session_state 내에 값을 카운트할 수 있는 cnt가 없으면 cnt 값을 새로 만들고 value를 0으로 초기화
# 조건문과 not in을 사용한 이유:
# 페이지(코드)를 재실행할 때마다 cnt가 0으로 초기화되어 이전 상태나 사용자의 상호작용을 무시하게 될 수 있어 그런 부분을 방지하기 위함
# 세션 사용하는 이유가 이전 입력값들을 유지시키기 위함인데, 코드 재실행시 다시 초기값으로 되는 걸 막아야함.
# 브라우저를 꺼야 없어짐.
if 'cnt' not in st.session_state:
    st.session_state['cnt'] = 0

st.write('조건문이 실행된 이후: ', st.session_state)

# 버튼이 들어갈 컬럼 설정
col1, col2, col3, _ = st.columns([1,1,1,4])

# 증가, 감소, 초기화 버튼
# 해당 버튼을 클릭하면 button함수를 설정할 때 지정한 key값이 세션의 key로, value가 True로 변경되어 업데이트 됨.
if col1.button('1 증가', key = 'first key'):
    st.session_state['cnt'] += 1

if col2.button('1감소', key = 'second key'):
    st.session_state['cnt'] -= 1

if col3.button('reset', key = 'third key'):
    st.session_state['cnt'] = 0

st.write(f'cnt = {st.session_state['cnt']}') # 출력시에도 session_state를 하나의 딕셔너리로 보고 그 값에 접근하는 코드로 출력
