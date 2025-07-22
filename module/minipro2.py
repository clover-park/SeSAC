
import streamlit as st
import folium
import geopandas as gpd
import streamlit_folium as sf
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

df1 = pd.read_csv('data/서울시 무더위쉼터.csv')
population = pd.read_csv('data/고령자현황_20250720105739.csv')
gu = []
for i in df1['지번주소']:
    i = i.split(' ')[1]
    gu.append(i)
df1['자치구'] = gu
df1.drop('지번주소', axis = 1 ,inplace=True)

gu_count = df1['자치구'].value_counts()
gu_count = gu_count.sort_values()
population.drop(population.index[0:4], inplace = True)

population['2025 1/4.3'] = pd.to_numeric(population['2025 1/4.3'], errors='coerce')
over65_population = population.groupby('동별(2)')['2025 1/4.3'].sum()
sort_over65_population = over65_population.sort_values()

df_plot1 = sort_over65_population.reset_index()
df_plot1.columns = ['자치구', '65세 이상 인구 수'] # 컬럼 이름 예시로 바꿔줌

# 시각화
fig, ax1 = plt.subplots(figsize=(8,6))
sns.barplot(
    data=df_plot1,
    x='자치구',
    y='65세 이상 인구 수',
    hue='자치구', 
    palette = 'magma',
    ax=ax1,
    legend=False
)
plt.xticks(rotation=45)

# Series를 DataFrame으로 변환
gu_count = gu_count.reset_index()
gu_count.columns = ['자치구', '무더위쉼터 개수']  # 컬럼 이름 바꿔줌

ax2 = ax1.twinx()
sns.lineplot(
    data = gu_count,
    x = '자치구',
    y = '무더위쉼터 개수',
    color = 'blue',
    ax = ax2
)

ax2.tick_params(axis='y', labelcolor='blue')
plt.tight_layout()
st.pyplot()
