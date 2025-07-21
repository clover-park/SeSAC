
import streamlit as st
from streamlit_option_menu import option_menu

# 사이드바에 네비게이션 메뉴 삽입
with st.sidebar:
    myNavi1 = option_menu(menu_title = 'sidebar menu',           # 네비게이션 메뉴 박스 이름
                          menu_icon = 'list',                    # 명칭 앞에 붙는 아이콘 유형 (list는 햄버거)
                          options = ['home', 'save','settings'], # 출력되는 메뉴 탭 명칭
                          icons = ['house','device-hdd','gear'], # 각 탭 이름 앞에 붙는 아이콘 형태
                          orientation = 'vertical')              # 네비게이션 탭 출력 형태(수직-vertical or 수평-horizontal)
    # 탭 클릭시 선택된 메뉴명이 반환됨(따라서 탭을 눌렀을 때 원하는 작업을 진행하게끔 코드를 짤 수 있음.)
    f'selected menu = {myNavi1}'

# 메인 화면에 네비게이션 메뉴 삽입
myNavi2 = option_menu(menu_title = 'main page menu',
                          menu_icon = 'list',
                          options = ['home', 'save','contacts'],
                          icons = ['house','device-hdd','people'],
                          orientation = 'horizontal',
                          # 깃험의 CSS style definition예시 그대로 사용
                          styles={
                              # container: 메뉴 탭들을 감싸는 전체 공간
                              # padding: 요소 내부의 여백(현재 0이며 !important는 해당 스타일을 우선적용 하라는 뜻)
                              # background-color: 배경색
                              # HEX값 확인 사이트: http://htmlcolorcodes.com/
                              # nav-link: 메뉴 탭 내부 공간
                              # margin: 메뉴 탭들을 감싸고 있는 박스와의 사이 공간
                              # --hover-color: 마우스 오버시 변경되는 색상
                            "container": {"padding": "0!important", "background-color": "#22f0f3"},
                            "icon": {"color": "black", "font-size": "25px"}, 
                            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                            "nav-link-selected": {"background-color": "lime"},
                                }
                     )

f'selected menu = {myNavi2}'
