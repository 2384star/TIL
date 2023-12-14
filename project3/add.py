import streamlit as st
import pandas as pd
import numpy as np

### 다른 헤더파일 
from modeltest import * 
from config import num_feature_col, cate_feature_col
from RGBgender import lab2rgb
from new_data import prepare_training_data
from mainmodel import model_build
from RGBgender import plot_rgb_color

import streamlit as st
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from changecolor import add_row_with_color_and_proportion

model = model_build()
model.load_weights("/Users/b32/Desktop/github/TIL/project3/save1.h5")



data=pd.read_csv("/Users/b32/Desktop/github/TIL/project3/기초데이터/X_train.csv",index_col=0)


# Streamlit 슬라이더로부터 입력값 받기
yellow_color = st.select_slider(
    'Select a color of the Yellow',
    options=['0.00000', '0.00283', '0.00550', '0.00833', '0.01116', '0.01666', '0.02783','0.05550','0.08333','0.11116','0.13883','0.16666','0.22216','0.25000','0.27783','0.33333','0.41666','0.44450','0.50000','0.66666','1.00000'],
    key='yellow_slider')
st.write('Selected Yellow color is', yellow_color)

red_color = st.select_slider(
    'Select a color of the Red',
    options=['0.00000', '0.00283', '0.00550', '0.00833', '0.01116', '0.01666', '0.02783','0.05550','0.08333','0.11116','0.13883','0.16666','0.22216','0.25000','0.27783','0.33333','0.41666','0.44450','0.50000','0.66666','1.00000'],
    key='red_slider')
st.write('Selected Red color is', red_color)

blue_color = st.select_slider(
    'Select a color of the Blue',
    options=['0.00000', '0.00283', '0.00550', '0.00833', '0.01116', '0.01666', '0.02783','0.05550','0.08333','0.11116','0.13883','0.16666','0.22216','0.25000','0.27783','0.33333','0.41666','0.44450','0.50000','0.66666','1.00000'],
    key='blue_slider')
st.write('Selected Blue color is', blue_color)


black_color = st.select_slider(
    'Select a color of the Black',
    options=['0.00000', '0.00283', '0.00550', '0.00833', '0.01116', '0.01666', '0.02783','0.05550','0.08333','0.11116','0.13883','0.16666','0.22216','0.25000','0.27783','0.33333','0.41666','0.44450','0.50000','0.66666','1.00000'],
    key='black_slider')
st.write('Selected Black color is', black_color)



Grey_color = st.select_slider(
    'Select a color of the Grey',
    options=['0.00000', '0.00283', '0.00550', '0.00833', '0.01116', '0.01666', '0.02783','0.05550','0.08333','0.11116','0.13883','0.16666','0.22216','0.25000','0.27783','0.33333','0.41666','0.44450','0.50000','0.66666','1.00000'],
    key='grey_slider')
st.write('Selected Grey color is', Grey_color)


DarkGrey_color = st.select_slider(
    'Select a color of the Blue',
    options=['0.00000', '0.00283', '0.00550', '0.00833', '0.01116', '0.01666', '0.02783','0.05550','0.08333','0.11116','0.13883','0.16666','0.22216','0.25000','0.27783','0.33333','0.41666','0.44450','0.50000','0.66666','1.00000'],
    key='darkgrey_slider')
st.write('Selected DarkGrey color is', DarkGrey_color)








if st.button('Submit'):
    # 슬라이더 값들을 실수형으로 변환
    yellow_value = float(yellow_color)
    red_value = float(red_color)
    blue_value = float(blue_color)
    black_value = float(black_color)
    grey_value = float(Grey_color)
    darkgrey_value = float(DarkGrey_color)

    # 변환된 값들 출력
    st.write('Selected Yellow color value:', yellow_value)
    st.write('Selected Red color value:', red_value)
    st.write('Selected Blue color value:', blue_value)
    st.write('Selected Black color value:', black_value)
    st.write('Selected Grey color value:', grey_value)
    st.write('Selected Dark Grey color value:', darkgrey_value)
    data = add_row_with_color_and_proportion(data, yellow_value, red_value, blue_value, black_value, grey_value, darkgrey_value)
    new_training_dataset = prepare_training_data(cate_feature_col, num_feature_col, data)
    # 새로운 데이터에 대한 모델 예측 수행
#   # 예측 결과 생성
#     Y_pred = pd.DataFrame(model.predict(new_training_dataset))
#     Y_pred.columns = ['색상_L*', '색상_a*', '색상_b*']


#     # 결과 표시
#     st.write("예측 결과 (LAB):")
#     st.dataframe(Y_pred)
    # LAB 값을 RGB로 변환
    Y_pred = pd.DataFrame(model.predict(new_training_dataset))
    Y_pred.columns = ['색상_L*', '색상_a*', '색상_b*']

    Y_pred_rgb = Y_pred.apply(lambda row: lab2rgb(row['색상_L*'], row['색상_a*'], row['색상_b*']), axis=1)
    Y_pred_rgb = pd.DataFrame(Y_pred_rgb.tolist(), columns=['R', 'G', 'B'])

    # 결과 표시
    st.write("예측 결과 (LAB):")
    st.dataframe(Y_pred)

    st.write("예측 결과 (RGB):")
    st.dataframe(Y_pred_rgb)
    plot_rgb_color(Y_pred_rgb)  # 항상 첫 번째 행 사용
    st.pyplot() 



# ### 나중에 지워야 할부분
# yellow_value = float(yellow_color)
# red_value = float(red_color)
# blue_value = float(blue_color)
# black_value = float(black_color)
# grey_value = float(Grey_color)
# darkgrey_value = float(DarkGrey_color)
# data = add_row_with_color_and_proportion(data, yellow_value, red_value, blue_value, black_value, grey_va

#new_row_to_train.to_csv("/Users/b32/Desktop/github/TIL/project3/newdatasave.csv")
    



