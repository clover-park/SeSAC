
import streamlit as st
import pandas as pd
import time

st.title('My petit Dashboard UWU')
st.header('currently working on it!:fire:')
st.text('This dashboard is made by Streamlit.')
url = 'https://docs.streamlit.io/'
st.markdown('**Here** you can try out buch of *Streamlit* functions.')
st.markdown('Click [here](url) to find out more.')
''
'---'
df = pd.DataFrame({'products':['A','B','C','D'],
                   'sales':[100,150,200,50],
                   'growth_loss':['+10%','+5%','+7%','-15%']})
st.write(df)

st.metric(label = 'max sales',value=max(df['sales']))

sel_prod = st.selectbox('Choose a product', options = df.products)
sale = df[df['products'] == sel_prod]['sales'].values[0]
st.write(f'{sel_prod} 의 판매량은 {sale}입니다.')
''
'---'
st.latex(r'l = 2\pi r')
''
'---'
st.image('data/waitan.jpg', width = 200,caption = '外滩')
''
'---'
st.code('''
print('Hello, Streamlit!')
''')
st.warning('This text is for warning!',icon='⚠️')
''
'---'
button = st.button('success')
if button:
    st.balloons()
    st.write('SUCCESS!!!')
''
'---'
name = st.text_input('write your name:')
st.write(f'Hello, {name}!!')
''
'---'
color = st.color_picker('Pick a color!')
st.write(f'You picked {color}')
''
'---'
progress = st.progress(0)
if st.button("진행 버튼") :
    for i in range(11) :
        time.sleep(1)
        progress.progress(i*10)
