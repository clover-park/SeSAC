
import streamlit as st
import folium
import streamlit_folium as sf
import numpy as np

# 위도, 경도 입력을 위한 컬럼 생성
col1, col2 = st.columns([1,1])

with col1:
    # 기본값으로 서울시청의 위도, 경도 값을 넣음. (value)
    lat0 = st.number_input('write latitude: ', value = 37.55, format = "%.2f", step = 0.01)

with col2:
    lon0 = st.number_input('write longitude: ', value = 126.99, format = "%.2f", step = 0.01)

# folium 지도 생성
myMap = folium.Map(location = [lat0, lon0], zoom_start=10)

# 지도 마커표시를 위해 랜덤 함수에 들어갈 시드(초기값) 생성
if 'seed' not in st.session_state:
    st.session_state['seed'] = 1

# 마커의 랜덤 시드를 변경시켜주는 버튼
if st.button('마커 시드 변경'):
    st.session_state['seed'] += 1 # 꼭 +1 아니어도 됨.

# 랜덤으로 마커의 좌표를 만들어주는 사용자 정의 함수
# 새로고침했을 때 마커가 바로 표시되도록 캐시 적용
@st.cache_resource
def randomMarkers(n, lat, lon, seed): # (마커개수, 위도, 경도, 시드값)
    # 시드값 고정
    np.random.seed(seed)
    # n 번 반복해서 랜덤한 위도와 경도 값을 2차원 리스트에 저장
    markers = [[lat+np.random.randn()/20, lon+np.random.randn()/20] for i in range(n)]
    return markers

# 마커들을 랜덤하게 생성하게 지도에 반복하여 붙여주기
marker_cnt = 20
popup_cnt = 1

# randomMarkers 함수의 출력 형태가 2차원 리스트이기 떄문에 변수를 2개로 받아주면 내부 리스트의 값들이 각각 lat, lon에 들어가 동작하게 됨.
for lat, lon in randomMarkers(marker_cnt, lat0, lon0, st.session_state['seed']):
    # Marker: Folium의 마커 생성 함수
    mk = folium.Marker(location=[lat, lon],           # 마커가 찍힐 위도, 경도
                       popup = f'popup: {popup_cnt}', # 마커 클릭 시 출력될 팝업 문구
                       tooltip = 'click it!',         # 마커에 마우스 오버시 출력되는 문구
                       icon = folium.Icon(color = 'blue', icon = 'cloud')) # icon: 마커 출력 모양 설정('star','home','cloud','info-sign' 등)
    # 맵에 마커 추가
    mk.add_to(myMap)
    popup_cnt += 1

sf.st_folium(myMap, width = 500, height=500)
