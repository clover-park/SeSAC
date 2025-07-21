
import streamlit as st
import pandas as pd

# 다양한 방식으로 DF 출력하기(디폴트로 최대 10개까지 한 번에 보여줌.)
df = pd.DataFrame(data = {'칼럼1':[1,2,3],
                          '칼럼2':['a','b','c'],
                          '칼럼3':[True, False, True]})
'1. Using magic command'
df
'2. Using write function -> same result as 1.'
st.write(df)
'3. Using dataframe function'
st.dataframe(df,width = 400)
'4. Using table function -> True, False printed as literal'
st.table(df)
''
'---' # 구분선 출력
''

# JSON 형식으로 출력
st.json([{'name':'Clover','age':23,'gender':'female'},
         {'name':'Toby','age':22,'gender':'male'}])

# 데이터 상태 변화 출력
st.metric(label = 'temperature', value = '36°C', delta = '15°C') # value값은 크게 나옴.
st.metric(label = 'Samsung', value = '63,000', delta = '-1000')
