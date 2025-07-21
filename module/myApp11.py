
import streamlit as st

tab1, tab2 = st.tabs(['上海','北京'])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('L_column1', divider='orange')
        st.image('data/disneyland.jpg')
        st.caption('迪斯尼，上海')
    with col2:
    # divider: 구분선 색 지정
        st.header('L_column2', divider='blue')
        st.image('data/dorm.jpg')
        st.caption('宿舍，上海')
    with col3:
    # divider: 구분선 색 지정
        st.header('L_column3', divider='rainbow')
        st.image('data/waitan.jpg')
        st.caption('外滩，上海')

with tab2:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header('R_column1', divider='orange')
        st.image('data/disneyland.jpg')
        st.caption('迪斯尼，上海')
    with col2:
    # divider: 구분선 색 지정
        st.header('R_column2', divider='blue')
        st.image('data/thegreatwall.jpg')
        st.caption('长城，北京')
    with col3:
    # divider: 구분선 색 지정
        st.header('R_column3', divider='rainbow')
        st.image('data/waitan.jpg')
        st.caption('外滩，上海')
