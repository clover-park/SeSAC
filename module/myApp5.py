
import streamlit as st
import pandas as pd
import datetime

# button
# 똑같은 label로 여러개의 버튼을 만들 수 없으며 같은 버튼을 만드려면 key를 다르게 지정
st.button(label='click!', key=1)
st.button(label='click!', key=2, help='this is a :blue[button]')

# 버튼을 눌렀을 때 동작할 기능 설정
def buttons(*args):
    total = 0
    for i in args:
        total += i
    st.write(f'total: {total}')

# on_click: 버튼을 눌렀을 때 동작할 함수를 설정하는 매개변수(뒤의 args의 리스트에 있는 값들이 buttons의 매개변수로 들어감.)
st.button(label='click!', key=3, on_click = buttons, args = [1,2,3,4,5] , help='this is a :blue[button]')

# 변수에 넣을 수도 있음.
button = st.button('click!', key = 4)
st.write(button)
if button:
    st.write(':smile:') # 버튼을 누르면 smile 이모지로 바뀜.
else:
    st.write(':sunglasses:')

''
'---'
''
# checkbox
temp = st.checkbox('i agree')
st.write(temp)
''
'---'
''
# radio
radio = st.radio(label = 'choose one', options=['spread','dip'], key = 'a') # 위젯이 달라도 key값이 중복되면 에러 발생 so, a라고 씀.
st.write(f'my choice = {radio}')
''
'---'
''
# selectbox
selectbox = st.selectbox(label = 'choose one', options = ['spread','dip'])
st.write(f'my choice = {selectbox}')
''
'---'
''
# multiselect
multiselect = st.multiselect(label = "choose today's dinner", options = ['Pho','Burger','Pasta','Chicken','Ramen'])
st.write(f"today's dinner = {multiselect}") # 여러개의 값을 리스트 형태로 출력
''
'---'
''
# color picker: HEX 컬러코드 값으로 출력됨.
# HSL: Hue(색상), Saturation(채도), Lightness(명도)
color = st.color_picker('pick a color')
st.write(f'color picked = {color}')
''
'---'
''
# select slider
selectslider = st.select_slider('Would you recommend this page?', ['Highly recommend','recommend','No not really','Will never recommend'])
st.write(selectslider)
''
'---'
''
# slider: 정수 입력
# min_value: 최소값, max_value: 최대값, value:초기값, step: 최소 단위(디폴트는 1)
slider = st.slider('Rate this page from 0 to 10', min_value = 0, max_value = 10, value=5, step = 2)
st.write(f'rate = {slider}')

# number_input
num = st.number_input('Write your GPA:', min_value = 0.0, max_value = 4.5, value = 3.0, step = 0.1)
st.write(f'GPA = {num}')
''
'---'
''
# text_input
text = st.text_input('名字：')

# time_input
d_input = st.date_input('When is your birthday?', max_value = datetime.datetime.now())
t_input = st.time_input('What time were you born?', step = datetime.timedelta(hours = 1))
st.write(f'my name = {text}, my birthday = {d_input}, birthtime = {t_input}')
