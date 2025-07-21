
import streamlit as st
import time

# progress: 진행 상태 바
st.write('processing...50%')
st.progress(50) # 0~100 사이 정수값

# balloons
st.balloons()

# snow
st.snow()

# error
st.error('error occurred', icon = '⚠️') # icon은 오직 하나만

# warning
st.warning('Watch out!', icon = '⚠️')

# info
st.info("Today's class is cancelled!", icon = '🤩')

# success
st.success('landed successfully!',icon='👍')

#spinner
# with 문은 특정 코드 블록의 시작과 끝을 정의하고 그 사이에 원하는 작업 및 리소스 관리를 지원함.
# 특정 단위의 코드 블록을 내부 로직에 상관없이 반드시 마무리 해야할 때 사용
# spinner는 실행 중인 상태를 표시한 후에 완료가 되면 없어져야 하기 때문에 with문과 함께 사용하여 마무리까지 할 수 있게 작업함.
with st.spinner('loading...'):
    time.sleep(5)
    st.success('shutting down', icon='✅')
