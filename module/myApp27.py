
# 강사님 코드
import streamlit as st
import FinanceDataReader as fdr
import mplfinance as mpf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.subheader('주가 데이터 시각화')

# ================================== 함수 설정 ==================================
# 종목코드 및 기간 설정에 따른 DF 반환 함수
@st.cache_data
def getData(code, dateStart, dateEnd) :
    df = fdr.DataReader(code, dateStart, dateEnd)
    return df

# 시가총액을 기준으로 정렬된 종목코드, 회사명, 시총 반환 함수
@st.cache_data
def getStockCode(market='KOSPI', sort='Marcap') :
    df = fdr.StockListing(market)
    df.sort_values(by=sort, ascending=False, inplace=True)
    return df[['Code', 'Name', 'Marcap']]   # 종목 코드, 회사명, 시총 반환

# → getData 및 getStockCode는 외부 대규모 데이터에서 값을 가져오기 때문에 캐시를 적용하여 효율을 높임
# ===============================================================================


# ================================== 세션 설정 ==================================
# session_state에 종목코드 변경시 활용 될 'code_index' 키 설정(종목코드가 아니라 인덱스 번호)
if 'code_index' not in st.session_state :
    st.session_state['code_index'] = 0

# 기간 설정시 활용될 'ndays' 키 설정
if 'ndays' not in st.session_state :
    st.session_state['ndays'] = 120                # 기간은 수치값이므로 0이나 원하는 숫자를 초기값으로 지정
    
# 차트 스타일을 변경할 수 있는 'chart_style' 키 설정
if 'chart_style' not in st.session_state :
    st.session_state['chart_style'] = 'default'    # 차트 스타일이 문자열이므로 빈 문자열이나 원하는 기본 차트 형식을 초기값으로 지정

# 거래량 출력 여부를 결정할 수 있는 'volume' 키 설정
if 'volume' not in st.session_state :
    st.session_state['volume'] = True              # 거래량 출력 여부를 결정하는 값이므로 논리값이 들어가면 됨
# ===============================================================================


# ================================== 사이드바 설정 ==================================
# 사이드바에서 여러 요소들을 입력받아 메인의 차트로 출력할 수 있도록 폼으로 구성

with st.sidebar.form(key='form1', clear_on_submit=True) :
    st.header('입력값 설정')
    ''
    # 1. 종목 코드 선택을 위한 selectbox 만들기
     # 종목코드와 회사명을 같이 출력시키기 위해 1:1로 매핑 시켜주기
     # zip : 순서가 있고 길이가 같은 두 집합에서 같은 순서의 값들을 튜플로 묶어주는 함수
    choices_tuple = zip(getStockCode()['Code'], getStockCode()['Name'])
    # 종목코드(문자열)와 회사명(문자열)을 ' : '로 하나의 문자열로 이어서 리스트에 저장
    choices_list = [' : '.join(i) for i in choices_tuple]

    # index는 선택박스의 초기값(session_state의 code_index에는 0으로 초기화 되어있는 상태라서 시총이 가장 높은 삼성전자가 나오게 됨)
     # (getStockCode의 sort 기준을 바꾸게 되면 또 다른 값이 나올 수 있음)
    choice = st.selectbox('종목', choices_list, index=st.session_state['code_index'])
    # choice는 문자열을 받아주고 'code_index'는 정수값이라 맞지 않음
    code_index = choices_list.index(choice)   # 리스트 내부 특정값의 인덱스 번호 추출
    code = choice.split(' : ')[0]  # 주식코드만 추출(기존에 주식코드 : 회사명 으로 문자열이 지정되어 있었는데 코드만 추출하여 code 변수에 저장)
    ''
    # 2. 기간을 설정할 수 있는 슬라이더 만들기
     # value는 초기값으로 세션에 저장된 120일이 기본 적용
    ndays = st.slider('기간(days) :', min_value=5, max_value=720, value=st.session_state['ndays'], step=1)
    ''
    # 3. 차트 스타일 목록 및 선택 박스 만들기
    chart_style_list = ['binance', 'binancedark', 'blueskies', 'brasil', 'charles', 'checkers', 'classic', 'default',
                         'ibd', 'kenan', 'mike', 'nightclouds', 'sas', 'starsandstripes', 'tradingview', 'yahoo']
    # index 인자로 초기값을 설정(초기값은 session의 chart_style에 있는 'default'가 들어감)
    chart_style = st.selectbox('차트 스타일 :', chart_style_list, index=chart_style_list.index(st.session_state['chart_style']))
    ''
    # 4. 거래량 설정 체크 박스 만들기(기본값은 True)
    volume = st.checkbox('거래량', value=st.session_state['volume'])

    # 폼 제출 버튼(누르면 session_state에 데이터 값들을 업데이트 후 새로고침 되게 설정)
    if st.form_submit_button('입력!') :
        st.session_state['code_index'] = code_index
        st.session_state['ndays'] = ndays
        st.session_state['chart_style'] = chart_style
        st.session_state['volume'] = volume
        st.rerun()
# ===============================================================================


# ================================== 메인 화면 설정 ==================================
# plotChart 함수는 차트를 생성하는 함수인데 항상 입력값이 달라질 것이기 때문에 캐시 적용 X
def plotChart(data) :
    chart_style = st.session_state['chart_style']    # 유저가 선택한 값으로 차트 스타일 설정
    marketcolors = mpf.make_marketcolors(up='red', down='blue') 
    mpf_style = mpf.make_mpf_style(base_mpf_style=chart_style, marketcolors=marketcolors)

    fig, ax = mpf.plot(
        data = data,     # DF형태로 입력
        type = 'candle',
        style = mpf_style,       
        figsize = (12,7),        
        fontscale = 1.0,         
        mav = (5,20,60),        
        mavcolors = ('green', 'blue', 'orange'),   
        returnfig = True,        
        volume = st.session_state['volume']   # 유저가 선택하면 거래량 출력(선택하지 않으면 미출력)          
    )
    return st.pyplot(fig) 

date_end = datetime.today().date()
date_start = date_end - timedelta(days=st.session_state['ndays'])    # 유저가 선택한 기간을 입력
df = getData(code, date_start, date_end)   # 매개변수의 code가 위에서 작성한 종목코드 추출하는 코드 → code = choice.split(' : ')[0]

# 현재 저장되어 있는 code_index값으로 choices_list에 있는 값을 인덱싱하고 기업명만 슬라이싱
chart_title = choices_list[st.session_state['code_index']][9:]   # 코스피 종목 코드는 6자리이며 공백과 : 을 포함하면 종목 명은 9번째 인덱스부터 출력됨
st.write('현재 차트 ➡️ ', chart_title)
st.write('이동평균선(mav): :green[5일], :blue[20일], :orange[60일]')

# 주가 차트 출력
plotChart(df)
