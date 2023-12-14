import pandas as pd
from changecolor import *
data=pd.read_csv("/Users/b32/Desktop/github/TIL/project3/X_train.csv",index_col=0)


data2=data.tail(2)
# 352번째 인덱스값쓰기  #때마침 염료 회사 1쓰네


# data2의 첫 번째 행을 복사
new_row = data2.iloc[0].copy()
# 새로 할당할 값
new_values = {
    70: 0.166667,  # Yellow
    71: 0.0,       # Red
    72: 0.083333,  # Blue
    79: 0,        # Black
    82: 0,        # Grey
    86: 0         # DarkGrey
}

# 총합 계산 (모든 값의 합)
# 총합 계산
total_sum = sum(new_values.values())

# 비율 계산 및 비율 컬럼 업데이트
new_row['배합_염료1_Yellow_prop_std'] = new_values[70] / total_sum if total_sum != 0 else 0
new_row['배합_염료1_Red_prop_std'] = new_values[71] / total_sum if total_sum != 0 else 0
new_row['배합_염료1_Blue_prop_std'] = new_values[72] / total_sum if total_sum != 0 else 0
new_row['배합_염료1_Black_prop_std'] = new_values[79] / total_sum if total_sum != 0 else 0
new_row['배합_염료1_Grey_prop_std'] = new_values[82] / total_sum if total_sum != 0 else 0
new_row['배합_염료1_Brown_prop_std'] = new_values[86] / total_sum if total_sum != 0 else 0


# 새로운 값들을 new_row에 저장
for col_index, value in new_values.items():
    new_row[col_index] = value

new_row_df = pd.DataFrame([new_row])

# 업데이트된 행을 원본 데이터프레임 'data'에 추가
data = pd.concat([data, new_row_df], ignore_index=True)

