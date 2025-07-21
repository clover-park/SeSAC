
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rc
rc('font', family = 'Malgun Gothic')

# main title(streamlit에는 중앙 정렬 기능이 따로 없어서 컬럼 레이아웃을 만들고 비율을 조정해서 넣어야함.)
_, col, _ = st.columns([1,3,1])
col.header('Iris Data Visualization')
''
df_iris = sns.load_dataset('iris')
st.dataframe(df_iris)

# 데이터를 필터링할 수 있는 사이드바 설정
with st.sidebar:
    sel_x = st.selectbox('x축 특성 선택:', df_iris.columns[:-1], key=1)
    sel_y = st.selectbox('y축 특성 선택:', df_iris.columns[:-1], key=2)
    sel_species = st.multiselect('품종 선택 (:blue[**다중선택 가능**])', df_iris['species'].unique())

    # 투명도 설정은 0~1사이의 실수값으로 그래픽의 투명도를 지정 가능(0:투명, 1: 불투명)
    sel_alpha = st.slider('투명도(alpha)값 설정: ', 0.1, 1.0, 1.0) # 최소값, 최대값, 초기값

# 선택된 붓꽃 품종별 산점도(scatter)차트로 시각화
# 품종별로 차트에 표시될 색상 지정
colors = {'setosa':'red','versicolor':'blue','virginica':'green'}

# 사용자가 사이드바에서 품종 선택을 함.(리스트에 값이 들어가면)
if sel_species:
    fig = plt.figure(figsize=(7,5))
    plt.title('Iris scatter plot')
    # 사용자가 선택한 품종에 따라 산점도 그래프 출력(scatter함수 내 color 속성에 colors, alpha속성에 sel_alpha로 지정할 것!)
    for i in sel_species:
        df = df_iris[df_iris['species'] == i]
        plt.scatter(df[sel_x], df[sel_y], color = colors[i],alpha = sel_alpha, label = i)
    plt.xlabel(sel_x)
    plt.ylabel(sel_y)
    plt.legend()
    st.pyplot(fig)

# 품종이 선택되지 않은 경우
else:
    st.warning('please choose species', icon = '🙄')
    
