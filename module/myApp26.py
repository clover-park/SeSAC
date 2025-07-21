
import streamlit as st
import FinanceDataReader as fdr
import mplfinance as mpf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.header('Stock Market Data Visualization 📊')

#=============================================함수 설정================================================

# 종목코드 및 기간 설정에 따른 DF 반환 함수
@st.cache_data
def getData(code, dateStart, dateEnd):
    df = fdr.DataReader(code, dateStart, dateEnd)
    return df

# 시가총액을 기준으로 정렬된 종목코드, 회사명, 시총 반환 함수
@st.cache_data
def getStockCode(market = 'KOSPI', sort = 'Marcap'):
    df = fdr.StockListing(market)
    df.sort_values(by = sort, ascending=False, inplace = True) # 내림차순, 바로 데이터프레임에 반영
    return df[['Code', 'Name','Marcap']] # 종목 코드, 회사명, 시가총액 반환
# getData 및 getStockCode는 외부 대규모 데이터에서 값을 가져오기 때문에 캐시를 적용하여 효율을 높여야함.

# =============================================세션 설정================================================

# session_state에 종목코드 변경시 활용될 'code_index' 키 설정
# 세션은 없으면 하나 만들어주는 방식으로 가야함.
if 'code_index' not in st.session_state:
    st.session_state['code_index'] = 0 # 종목코드가 아니라 종목코드 인덱스 번호!

# 기간설정시 활용될 'ndays' 키 설정
if 'ndays' not in st.session_state:
    st.session_state['ndays'] = 120 # 0이나 원하는 숫자를 초기값으로 지정


# 차트 스타일을 변경할 수 있는 'chart_style'키 설정
if 'chart_style' not in st.session_state:
    st.session_state['chart_style'] = 'charles' # 빈 문자열이나 원하는 기본 차트 형식을 초기값으로 지정
    
# 거래량 출력 여부를 결정할 수 있는 'volume'키 설정
if 'volume' not in st.session_state:
    st.session_state['volume'] = True # 거래량 출력 여부를 결정하는 값이므로 논리값이 들어가면 됨.

# ==========================================사이드바 설정================================================
# sidebar에서 여러 요소들을 입력받아 메인의 차트로 출력할 수 있도록 폼으로 구성
with st.sidebar.form(key = 'form1', clear_on_submit = True):
    st.subheader('options')
    ""
    # 1. 종목 코드 선택을 위한 selectbox 만들기
    # 종몰 코드와 회사명을 같이 출력시키기 위해 1:1로 매핑 시켜주기 -> zip 함수 사용
    # zip: 순서가 있고 길이가 같은 두 집합에서 같은 순서의 값들을 튜플로 묶어주는 함수
    choices_tuple = zip(getStockCode()['Code'],getStockCode()['Name'])
    
    # 종목코드 회사명을 : 로 이어줘서 리스트에 저장
    choice_list = [' : '.join(i) for i in choices_tuple]
    
    # index는 선택박스의 위에서 설정한 초기값(session_state['code_index'])
    # 0으로 설정해둬서 초기값은 삼성전자가 나옴.
    # getStockCode의 sort 기준을 바꾸게 되면 또 다른 값이 나올 수 있음.
    choice = st.selectbox('stock item', choice_list, index = st.session_state['code_index'])

    # choice는 문자열인데, 인덱스는 정수여야함.
    # .index()로 인덱스 번호 추출
    choice_index = choice_list.index(choice)
    code = choice.split(':')[0] # 주식코드만 추출(기존에 주식코드 : 회사명 으로 문자열이 지정되어 있었는데 코드만 추출하여 code 변수에 저장)
    ""
    # 2. 기간을 설정해주는 슬라이더 만들기
    # value에는 초기값으로 세션에 저장된 120일이 기본으로 적용
    ndays = st.slider('term',min_value = 5,max_value = 720,value=st.session_state['ndays'], step = 1)
    ""
    # 3. 차트 스타일 선택박스 만들기
    chart_style_list = ['binance','binancedark','blueskies','brasil','charles','checkers','classic','default',
                         'ibd','kenan','mike','nightclouds','sas','starsandstripes','tradingview','yahoo']
    chart_style = st.selectbox('chart style',chart_style_list, index = chart_style_list.index(st.session_state['chart_style']))
    ""
    # 4. 거래량 출력 여부를 선택하는 체크박스 만들기 (초기값은 st.session_state['volume'] 즉, True)
    volume = st.checkbox('trade volume', value = st.session_state['volume'])
    ""
    # 5. 폼 제출 버튼: 누르면 session_state에 선택한 정보가 업데이트되고 새로고침 되게 설정
    # 메인 화면으로 넘어가도 값이 유지되어야함. 폼에서만 진행할 거면 session 필요없음! 다른 곳에서 데이터를 활용할 거면 세션 반드시 필요
    if st.form_submit_button('see chart'):
        st.session_state['code_index'] = choice_index
        st.session_state['ndays'] = ndays
        st.session_state['chart_style'] = chart_style
        st.session_state['volume'] = volume
        st.rerun()

# ==========================================메인화면 설정================================================
# plotChart함수는 차트를 생성하는 함수인데 항상 입력값이 달라질 것이기 때문에 캐시 적용 X
def plotChart(data):
    chart_style = st.session_state['chart_style'] # 세션 값으로 넣어주기
    marketcolors = mpf.make_marketcolors(up = 'red', down = 'blue')
    mpf_style = mpf.make_mpf_style(base_mpf_style = chart_style, marketcolors = marketcolors)
    
    fig, ax = mpf.plot(
        data = data, # df 형태가 들어감.
        type = 'candle',
        style = mpf_style,
        figsize = (12,7),
        fontscale = 1.0,
        mav = (5, 20, 60),
        mavcolors = ('green', 'blue','orange'),
        returnfig = True,
        volume = st.session_state['volume'] # 세션 값으로 넣어주기
    )
    return st.pyplot(fig)

date_end = datetime.today().date()
date_start = date_end - timedelta(days = st.session_state['ndays']) # 세션 값으로 넣어주기
df = getData(code, date_start, date_end) # 여기서 code는 위에서 작성한 종목코드 추출하는 코드 -> code = choice.split(':')[0]

# 차트 제목을 선택한 주식 종목이 나오게 설정
chart_title = choice_list[st.session_state['code_index']][9:] # [9:]한 이유? '005930 : ' 가 9자리라
st.write('current chart>> ', chart_title)
st.write('mav: :green[5-days], :blue[20-days], :orange[60-days]')

# 차트 출력
plotChart(df)
