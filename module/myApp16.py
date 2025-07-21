
import streamlit as st
import numpy as np
import pandas as pd

# randn: 평균이 0이고 표준편차가 1인 정규분포 내에서 랜덤한 실수값 생성
data = np.random.randn(20,3) # (행, 열)
df = pd.DataFrame(data, columns = ['a', 'b', 'c'])

# df 출력
st.dataframe(df)

# 각종 차트로 출력(아래 차트들은 기본적으로 df로만 이용해서 만들 수 있음!!)
'line chart'
st.line_chart(df)

'area chart'
st.area_chart(df)

'bar chart'
st.bar_chart(df)
