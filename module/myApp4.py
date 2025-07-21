
import streamlit as st

'Image of Waitan, Shanghai :cn:'
st.image('data/waitan.jpg', width = 500, caption = '外滩')

# 음성 출력
# 1. open 함수로 파일 불러와서 저장
# rb: 읽기 전용
with open('data/clockbell.wav','rb') as f:
    audio_data = f.read()

# 2. 음성 출력
'Ringtone'
st.audio(audio_data)

# 영상 출력
with open('data/wave.mp4', 'rb')as f:
    video_data = f.read()

'Wave Video'
st.video(video_data)
