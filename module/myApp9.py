
import streamlit as st

st.title('This is the main page')
'---' # 이건 메인페이지 구분선
# with문을 활용해서 사이드바, 컬럼 설정할 수 있음!!!
with st.sidebar:
    # 사이드바 생성
    st.sidebar.title('This is a sidebar.')
    st.sidebar.header('You can write a header.')
    st.sidebar.subheader('Also a subheader!')

    st.sidebar.write('---') # 이건 사이드바 구분선
    select = st.sidebar.selectbox('select one',['spread','dip'])
    st.sidebar.write(f'you chose {select}')

# 컬럼 생성
col1, col2, col3 = st.columns([1,2,1]) # 만들고자하는 컬럼 객체 수에 맞게 정수 입력
# 아니면 리스트로 컬럼의 너비 비율을 지정할 수 있음.
with col1:
    # divider: 구분선 색 지정
    st.header('column1', divider='orange')
    st.image('data/disneyland.jpg')
    st.caption('迪斯尼，上海')
with col2:
    # divider: 구분선 색 지정
    st.header('column2', divider='blue')
    st.image('data/thegreatwall.jpg')
    st.caption('长城，北京')
with col3:
    # divider: 구분선 색 지정
    st.header('column3', divider='rainbow')
    st.image('data/waitan.jpg')
    st.caption('外滩，上海')
