
import streamlit as st
import pandas as pd

x, y = 1, 2
df = pd.DataFrame(data = {'칼럼1':[1,2,3],
                          '칼럼2':['a','b','c'],
                          '칼럼3':[True, False, True]})
# write함수 대신에 streamlit 매직커맨드로 동작시킬 수 있음.
'this is text' # 그냥 문자열처럼 써도됨;;;
x # 그냥 써도 출력이 됨;;;;
y
'' # 공백용
''
df

# 마크다운 색상 적용
'print in :blue[**BLUE**] color'
'print in :red[**RED**] color'

# 이모지 출력
'cool! :sunglasses:'
'thumbs up! :thumbsup:'
'cheese! :smile:'
