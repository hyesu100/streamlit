# streamlit run main.py

# 메인화면 구현
import streamlit as st
import pandas as pd
import numpy as np

# 로고
st.markdown("<h5 style='text-align: center; color: deep grey; margin-top: 100px;'>영어 주관식 서술형 자동채점 프로그램</h5>", unsafe_allow_html=True)
# st.markdown("<h1 style='text-align: center; color: black;'>채끝</h1>", unsafe_allow_html=True)

# 이미지
from PIL import Image
image = Image.open('small logo.png')
st.image(image)

# 자동채점 버튼 (왼쪽)
st.markdown("<button style='text-align: center; float: left; padding: 20px 100px; margin-top: 150px; font-size:25px; color:white; background-color:skyblue; border-radius : 20px; border: none;'>자동 채점</button>", unsafe_allow_html=True)
# st.button("자동 채점",help="자동채점 프로그램으로 가는 버튼입니다.")

# db 버튼 (오른쪽)
st.markdown("<button style='text-align: center; float: right; padding: 20px 100px; margin-top: -95px; font-size:25px; color:white; background-color:skyblue; border-radius : 20px; border: none;'>채끝 저장소</button>", unsafe_allow_html=True)
# st.button("채끝 저장소",help="사용자의 데이터가 저장된 DB로 이동하는 버튼입니다.")

# 챗봇 버튼 (오른쪽 하단, 버튼에 이미지 삽입)
image = Image.open('main pig.png')
st.image(image, width=100)
