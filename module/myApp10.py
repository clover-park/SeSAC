
import streamlit as st

tab1, tab2, tab3 = st.tabs(['迪斯尼','长城', '外滩'])
with tab1:
    # divider: 구분선 색 지정
    st.header('tab1', divider='orange')
    st.image('data/disneyland.jpg')

with tab2:
    # divider: 구분선 색 지정
    st.header('tab2', divider='blue')
    st.image('data/thegreatwall.jpg')

with tab3:
    # divider: 구분선 색 지정
    st.header('tab3', divider='rainbow')
    st.image('data/waitan.jpg')
