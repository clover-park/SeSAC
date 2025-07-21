
import streamlit as st
import pandas as pd

# 기본 함수 사용해보기
st.title('This is *title*') # * *는 마크다운 기호로 italic을 적용함. 근데, text와 code 은 이거 적용 안 됨.
st.header('This is header')
st.subheader('This is subheader')
st.text('This is text *blablablablablablblaballba*') # 마크다운 인식 못 함.

 # 마크다운 출력
st.markdown('This is *markdown*') # italic
st.markdown('This is **markdown**') # bold
st.markdown('This is ***markdown***') # italic + bold
st.markdown('~This is markdown~') # strikethrough (취소선) 적용
st.markdown('[뉴스 원문 클릭](https://n.news.naver.com/mnews/article/008/0005220971)') # 하이퍼링크 적용
st.markdown(':smile: :100: :ocean: :streamlit:') #이모지 적용

# 텍스트 및 변수/객체 출력(파이썬의 print문과 유사함)
x, y = 1, 2
st.write(x,y) # 초록색으로 출력됨.
st.write('This is similar to Python print')
st.write(f'x = {x}, y = {y}') # 초록색이 아니라 검은색으로 출력됨.

df = pd.DataFrame(data = {'칼럼1':[1,2,3], # 숫자는 우측 정렬
                          '칼럼2':['a','b','c'], # 문자는 좌측 정렬
                          '칼럼3':[True, False, True]}) # True는 웹 상에서 체크표시로 뜨고, False는 빈칸으로 뜸.
st.write(df)

# 수식 출력
# latex 함수에서 '\'는 특정한 수식을 표현하는 기호인데 파이썬 문자열 이스케이프 코드로 인식되지 않도록 문자열 앞에 r(raw string)을 붙여 방지
st.latex('E = mc^2')
st.latex(r'Area = \pi r^2 \ 입니다.') # \pi: 파이
st.latex(r'\frac{a}{b} = c') # 분수: \frac{분자}{분모}
st.latex(r'\sqrt{3}') # 제곱근: \sqrt{표현식}

# 코드 출력(코드 형식으로 출력하지만 실제 코드 내부 연산이 진행되어 결과가 나오지는 않음.) 복사도 할 수 있음.
myCode = '''
total = 0
for i in range(5):
    total += i
print(total)
'''
st.code(myCode)

# 캡션 출력
st.caption('This is **caption**!')
