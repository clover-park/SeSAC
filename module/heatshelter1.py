
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

st.header('프로젝트 제목')
# ==========================세션 설정============================

if 'gu' not in st.session_state:
    st.session_state['gu'] = ''

# ====================================탭 제작===============================
tab1, tab2, tab3,tab4, tab5 = st.tabs(['가설 1','가설2','가설3','가설4','가설5'])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader('자치구별로 무더위쉼터 개수가 비등비등할 것이다.', divider = 'orange')
        plt.figure(figsize=(10,10))
        plt.bar(gu_count.index, gu_count)
        plt.ylim(0,300)
        plt.xticks(rotation = 45)
        plt.xlabel('자치구')
        plt.ylabel('무더위쉼터 개수')
        st.pyplot(plt)
    with col2:
# ===========================지도에 표시===============================
# 서울 자치구 GeoJSON 파일 읽기
        st.subheader('자치구별로 무더위쉼터 개수 지도', divider = 'orange')
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
                popup=folium.Popup(f"{row['name']}<br>쉼터 개수: {row['무더위쉼터 개수']}개", 
                                  max_width=300)  # Popup 추가
            ).add_to(seoul_map)
            
        sf.st_folium(seoul_map, width = 300, height=300)

with tab2:
    st.subheader('고령자수가 많은 자치구일수록, 무더위 쉼터의 개수도 많을 것이다.', divider = 'orange')
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
    st.pyplot(fig)
with tab3:
    st.subheader('무더위쉼터 종류가 다양한 만큼, 각 항목마다 고른 분포율을 보일 것이다.', divider = 'orange')
    silver_hall = []
    center = []
    bank = []
    library = []
    church = []
    sarangbang = []
    welfare = []
    green_smart = []
    
    shelter_type = []
    
    for i in df1['쉼터명칭']:
        if '경로당' in i:
            silver_hall.append(i)
        elif '주민센터' in i:
            center.append(i)
        elif '은행' in i or '금고' in i:
            bank.append(i)
        elif '도서관' in i:
            library.append(i)
        elif '교회' in i:
            church.append(i)
        elif '사랑방' in i:
            sarangbang.append(i)
        elif '복지' in i:
            welfare.append(i)
        elif '그린스마트' in i:
            green_smart.append(i)
            
    
    shelter_num = len(df1['쉼터명칭'])
    
    shelter_type.append(len(silver_hall)/shelter_num *100)
    shelter_type.append(len(center)/shelter_num *100)
    shelter_type.append(len(bank)/shelter_num *100)
    shelter_type.append(len(library)/shelter_num *100)
    shelter_type.append(len(church)/shelter_num *100)
    shelter_type.append(len(sarangbang)/shelter_num *100)
    shelter_type.append(len(welfare)/shelter_num *100)
    shelter_type.append(len(green_smart)/shelter_num *100)
    
    df3 = pd.DataFrame(shelter_type)
    df3.index = ['경로당','주민센터','은행','도서관','교회','사랑방','복지관','그린스마트 쉼터']
    fig, ax = plt.subplots(figsize=(7,7))
    ax.pie(shelter_type,
            labels = df3.index,
            autopct='%1.1f%%')
    
    ax.set_title('무더위 쉼터 종류')
    st.pyplot(fig)
    
with tab4:
    st.subheader('각 자치구별 인구수 대비 무더위 쉼터 개수 비율로 시급성을 따져 볼 수 있을 것이다.', divider = 'orange')
with tab5:
    with st.expander("위험 등급 기준 안내"):
        st.markdown("""
        - **매우 위험**: 고령자 및 장애인 1,000명당 무더위쉼터 수가 서울 평균보다 현저히 낮은 지역입니다.
        - **위험**: 인프라 부족이 우려되며, 개설 우선 검토가 필요한 수준입니다.
        - **주의**: 인프라 밀도는 중간 수준이며 추가 점검이 권장됩니다.
        - **보통**: 적절한 분포로 판단되지만 지역 내 균형 여부 확인 필요.
        - **양호**: 인구 대비 인프라 수준이 우수하며, 급박한 추가 개설 필요는 낮습니다.
        """)
    st.subheader('시급성 지수', divider = 'orange')
    gu = st.selectbox('',gu_count['자치구'])

    df_plot1 = df_plot1.sort_values('자치구')
    gu_count = gu_count.sort_values('자치구')
    priority_index = gu_count.copy()
    priority_index['시급성 지수'] = df_plot1['65세 이상 인구 수']/gu_count['무더위쉼터 개수']
    priority_index.drop('무더위쉼터 개수', axis = 1, inplace = True)
    priority_index['시급성 지수'] = priority_index['시급성 지수'].round(1)

    priority_index['code'] = pd.cut(
    priority_index['시급성 지수'],
    bins=[0, 299.9, 499.9, np.inf],
    labels=['양호', '주의', '위험']
    )

    priority_index = gu_count.copy()
    priority_index['시급성 지수'] = df_plot1['65세 이상 인구 수']/gu_count['무더위쉼터 개수']
    priority_index.drop('무더위쉼터 개수', axis = 1, inplace = True)
    priority_index['시급성 지수'] = priority_index['시급성 지수'].round(1)

    geo_path = "https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json"  # GeoJSON 파일 경로
    geo_data = gpd.read_file(geo_path)
    gu_count_df = df1['자치구'].value_counts().reset_index()
    gu_count_df.columns = ['자치구', '시급성 지수']
    data = priority_index.copy()
    
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
        data=priority_index,
        columns=['자치구', '시급성 지수'],
        key_on='feature.properties.name', # GeoJSON 데이터와 data의 자치구 정보를 연결
        fill_color='Reds',  # 색상 스케일
        line_color='black',
        fill_opacity=0.7,
        line_opacity=0.5,
        legend_name='시급성 지수'
    ).add_to(seoul_map)
    
    for _, row in geo_data.iterrows(): # geo_data 순회하면서 각 행(row)을 반복적으로 
        folium.GeoJson(
            row['geometry'],  # GeoJSON 형식의 geometry 데이터
            name=row['name'],
            tooltip=folium.Tooltip(f"{row['name']}: {row['시급성 지수']}"),  # Tooltip에 표시되는 내용
            popup=folium.Popup(f"{row['name']}<br>시급성 지수: {row['시급성 지수']}", 
                              max_width=300)  # Popup 추가
        ).add_to(seoul_map)
    sf.st_folium(seoul_map, width = 1000, height=1000)
