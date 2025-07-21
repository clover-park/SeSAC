
import streamlit as st
import pandas as pd

# csv 파일 업로드 후 데이터 값 자체 출력(code 함수로 출력)
myFile1 = st.file_uploader('1. choose .csv file: ', type=['csv'], key=1)
cont1 = st.container()

if myFile1: # 파일을 입력받았을 때
    cont1.write('file uploaded') # 이 텍스트 출력
    # file_uploader 객체의 read메소드로 파일을 읽고
    # decode 메소드로 디코딩(텍스트에서 코드로)진행
    code = myFile1.read().decode('euc-kr')
    cont1.code(code) # cont1에 내용 출력
''
'---'
''
myFile2 = st.file_uploader('2. choose .py file: ', type=['py'], key=2)
cont2 = st.container()

if myFile2:
    cont2.write('file uploaded')
    code = myFile2.read().decode('utf-8')
    cont2.code(code)
''
'---'
''
# csv 파일 업로드 후 df로 출력
myFile3 = st.file_uploader('3. choose .csv file: ', type=['csv'], key=3)
cont3 = st.container()

if myFile3:
    cont3.write('file uploaded')
    df = pd.read_csv(myFile3, encoding='euc-kr')
    cont3.write(df)

# 여러개 파일 동시에 올리기(파일 이름 및 용량 출력까지!)
# type 지정 불필요, accept_multiple_files = True
myFiles = st.file_uploader('4. choose multiple files: ', accept_multiple_files = True)
cont4 = st.container()

if myFiles:
    cont4.write('file uploaded')
    # name: file_uploader객체가 가진 파일 이름 반환 메소드
    file_names = [i.name for i in myFiles] # 한 줄 for문
    # size: file_uploader 객체가 가진 파일 용량 반환 메소드(Byte단위로 출력)
    file_sizes = [str(i.size) for i in myFiles] # join을 쓰기 위해 str로 형변환
    
    # join: 리스트 형태보다는 한 줄 문자열로 출력시키기
    cont4.write(f'- file names: {", ".join(file_names)}')
    cont4.write(f'- file sizes: {", ".join(file_sizes)}')

# 파일 다운로드
df = pd.DataFrame(data = {'col1': [1,2,3],
                          'col2': ['a', 'b', 'c'],
                          'col3': [True,False,True]})
st.dataframe(df)
data = df.to_csv(encoding = 'utf-8')

# download 버튼(문구, 실제 데이터, 데이터가 저장될 경로 및 파일명)
# 저장 위치는 브라우저에서 설정한 위치로 다운로드
st.download_button('download file', data, 'data/myDF.csv')
