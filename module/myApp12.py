
import streamlit as st

with st.expander('expander1'):
    st.write('外滩')
    st.image('data/waitan.jpg',width=400)
with st.expander('expander2'):
    st.write('宿舍')
    st.image('data/dorm.jpg',width=400)
with st.expander('expander3'):
    st.write('迪斯尼')
    st.image('data/disneyland.jpg',width=400)
