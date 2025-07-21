
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

st.map(data=data, zoom=10)
st.button('restart')
