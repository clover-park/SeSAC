
import json
import requests as req
import time
import pandas as pd
import streamlit as st
import folium
import streamlit_folium as sf
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud
from PIL import Image
from bs4 import BeautifulSoup as bs

# ======================================================함수 설정==============================================================
# 네이버 검색 API를 활용한 뉴스 검색 결과를 반환해 주는 함수
def getRequest(keyword, display, start):
    url = f'https://openapi.naver.com/v1/search/news.json?query={keyword}&display={display}&start={start}'
    N_A = {"X-Naver-Client-Id":st.session_state['client_id'], # 세션 설정에서 초기화를 시켜줄 예정
           "X-Naver-Client-Secret":st.session_state['client_secret']} # 세션 설정에서 초기화를 시켜줄 예정
    res = req.get(url, headers=N_A)
    my_json = json.loads(res.text)
    return my_json['items']

# 워드클라우드 시각화 함수
def wcChart(corpus, back_mask, max_words, emp): # 매개변수: 문자열 텍스트, 배경 이미지, 최대 출력 단어수, empty공간
    if back_mask == 'oval':
        img = Image.open('data/background_1.png')
    elif back_mask == 'bubble':
        img = Image.open('data/background_2.png')
    elif back_mask == 'heart':
        img = Image.open('data/background_3.png')
    else:
        img = Image.open('data/background_0.png')
    
    # 워드클라우드에 적용하기 위해 이미지를 배열로 변환    
    my_mask = np.array(img)
    
    wc = WordCloud(font_path = "C:\Windows\Fonts\Gulim.ttc", # 한글 글꼴 지정
               background_color = 'black',
               max_words = max_words,
               random_state = 99,
               stopwords = ['등','있다','및','수','이','a','the','an','of','to','in','and','said','was','is','by'],
               mask = my_mask) # 배경 지정
    
    # generate: 문자열에서 단어의 빈도(띄워쓰기 기준)를 자동 계산하여 워드클라우드 생성
    wc.generate(corpus) # corpus: 말뭉치라는 뜻
    
    fig = plt.figure(figsize=(10,10))

    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)
    
    emp.info(':orange[**WordCloud Image generated successfully!**]', icon = ':smile:')

# ======================================세션 설정===========================================
if 'client_id' not in st.session_state:
    st.session_state['client_id'] = '' # id 써도 됨.

if 'client_secret' not in st.session_state:
    st.session_state['client_secret'] = '' # pw 써도 됨.

# ===============================사이드바 설정(client_id, client_secret 입력 부분)===============================

with st.sidebar.form(key = 'form1', clear_on_submit = False):
    st.header('Naver API settings')
    client_id = st.text_input('Client ID: ', value = st.session_state['client_id'])
    
    # type = 'password': 텍스트 입력시 보이지 않게 처리(비밀번호 등을 입력받을 때 사용)
    client_secret = st.text_input('Client Secret: ', value = st.session_state['client_secret'], type = 'password')
    if st.form_submit_button('OK'):
        st.session_state['client_id'] = client_id
        st.session_state['client_secret'] = client_secret
        st.write('setting complete!:)')
        st.rerun()

# =========================================메인 화면 설정===================================================
# 진행상황을 띄워줄 빈 공간 설정(문구는 최종 출력만 나오도록 empty로 설정)
chart_emp = st.empty()

try:
    with st.form(key='Search', clear_on_submit=False):
        search_keyword = st.selectbox('keyword: ',['경제','정치','사회','국제','언어','IT','문화'])
        data_amount = st.slider('volume(100): ',min_value = 1, max_value = 5, value = 1, step = 1)
        # 워드클라우드 배경 마스크 이미지 선택
        back_mask = st.radio('choose a background: ',['default','oval','bubble','heart'], horizontal = True)
        if st.form_submit_button('print'):
            chart_emp.info('red[**loading data...**]', icon = '💤')
            corpus = '' # 수집된 문자열이 담길 변수 설정
            items = [] # 뉴스 항목이 담길 리스트
            
            # 입력받은 수집 분량(data_amount)만큼 반복해서 뉴스 기사 정보 가져오기
            for i in range(data_amount):
                items.extend(getRequest(search_keyword, 100, 100*i+1)) # 검색어, 한번에 표시할 양, 시작지점
                
            # 네이버 검색 API로 얻은 링크로 각각 들어가서 본문 내용 크롤링
            for item in items: # 위에서 먼저 데이터를 수집해야 items에 값이 들어감.
                if 'n.news.naver' in item['link']: # item은 딕셔너리, items는 리스트 타입
                    news_url = item['link']
                    res = req.get(news_url, headers = {'User_Agent':'Mozilla'}) # 헤더에 브라우저로 인식되게 설정
                    soup = bs(res.text, 'lxml')                                # 파싱(bs 객체화)
                    news_tag = soup.select_one('#dic_area')                     # 뉴스 본문을 품은 dic_area 아이디로 접근
                    
                    if news_tag:
                        corpus += news_tag.text + ' ' # 본문의 텍스트를 corpus에 계속 추가하기
                        
            st.write('수집된 corpus이 길이: ', len(corpus))
            
            # 워드클라우드 생성(corpus길이가 적으면 별루임. 길이가 100개 이상일 때 출력되게 조건 설정)
            if len(corpus) >= 100:
                chart_emp.info(':red[**creating image...**]', icon = '💤')
                wcChart(corpus, back_mask, 70, chart_emp)
            else:
                chart_emp.error(':red[**not enough corpus...**]', icon = '😓')

except:
    chart_emp.error('please fill out the form.')
