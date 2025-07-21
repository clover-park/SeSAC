
import streamlit as st
import folium
import geopandas as gpd
import streamlit_folium as sf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')

df1 = pd.read_csv('data/서울시 무더위쉼터.csv')

gu = []
for i in df1['지번주소']:
    i = i.split(' ')[1]
    gu.append(i)
df1['자치구'] = gu
df1.drop('지번주소', axis = 1 ,inplace=True)

gu_count = df1['자치구'].value_counts()

# ==========================세션 설정============================

if 'gu' not in st.session_state:
    st.session_state['gu'] = ''


# ==========================사이드바 제작============================
st.header('자치구별 무더위쉼터 개수')

with st.sidebar.form(key = 'form1', clear_on_submit = True):
    st.subheader('자치구 선택')
    gu = st.selectbox('자치구',gu_count.index)

    if st.form_submit_button('submit'):
        st.session_state['gu'] = gu
        st.rerun()
# ==================자치구별 정보 출력====================

st.write(gu)
# ===========================지도에 표시=====================
# 서울 자치구 GeoJSON 파일 읽기
geo_path = "https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json"  # GeoJSON 파일 경로
geo_data = gpd.read_file(geo_path)
gu_count_df = df1['자치구'].value_counts().reset_index()
gu_count_df.columns = ['자치구', '무더위쉼터 개수']
data = gu_count_df.copy()

# 서울의 위도, 경도: 37.5665, 126.9780
seoul_map = folium.Map(location=[37.5665, 126.9780], zoom_start=10, tiles='CartoDB positron')

# 3. 데이터 병합 (GeoJSON + 거치대 개수 데이터)
geo_data = geo_data.merge(data, left_on='name', right_on='자치구') 
# 'name' 컬럼은 GeoJSON 파일의 자치구 이름 컬럼

# folium.Choropleth 클래스를 사용
# Choropleth 맵: 지역별로 색상을 다르게 하여 데이터를 시각화하는 지도
folium.Choropleth(
    geo_data=geo_data,
    name="choropleth",
    data=gu_count,
    columns=['자치구', '무더위쉼터 개수'],
    key_on='feature.properties.name', # GeoJSON 데이터와 data의 자치구 정보를 연결
    fill_color='YlGnBu',  # 색상 스케일
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='무더위쉼터 개수'
).add_to(seoul_map)

for _, row in geo_data.iterrows(): # geo_data 순회하면서 각 행(row)을 반복적으로 
    folium.GeoJson(
        row['geometry'],  # GeoJSON 형식의 geometry 데이터
        name=row['name'],
        tooltip=folium.Tooltip(f"{row['name']}: {row['무더위쉼터 개수']}개"),  # Tooltip에 표시되는 내용
        popup=folium.Popup(f"{row['name']}<br>거치대 개수: {row['무더위쉼터 개수']}개")  # Popup 추가
    ).add_to(seoul_map)
    
sf.st_folium(seoul_map, width = 500, height=500)
