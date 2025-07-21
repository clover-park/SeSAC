
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns # sns는 개발자 이름 줄인거임...
# 한글 설정
from matplotlib import rc
rc('font', family = 'Malgun Gothic')

# 지도 위에 서울 시청 좌표 표시(위도(latitude), 경도(longitude))
data = {'lat':[37.5519],'lon':[126.9918]}

# 랜덤으로 100개의 위치를 추가
data['lat'] = [data['lat'][0] + np.random.randn()/50 for _ in range(100)] # data['lat'][0] + np.random.randn()가 100번 반복
data['lon'] = [data['lon'][0] + np.random.randn()/50 for _ in range(100)]

st.map(data=data, zoom=10) # zoom값이 크면 확대가 많이 됨.
st.button('restart')
