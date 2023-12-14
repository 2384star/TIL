import pandas as pd

def add_row_with_color_and_proportion(data, yellow, red, blue, black, grey, darkgrey):
    # data의 마지막에서 두 번째 행을 복사
    data2=data.tail(3)
    new_row = data2.iloc[0].copy()

    # 새로 할당할 값
    new_values = {
        70: yellow,  # Yellow
        71: red,     # Red
        72: blue,    # Blue
        79: black,   # Black
        82: grey,    # Grey
        86: darkgrey # DarkGrey
    }

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

    # 업데이트된 행을 데이터프레임에 추가
    updated_data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
    new_row_to_train = updated_data.iloc[-1:]
    new_row_to_train.to_csv("/Users/b32/Desktop/github/TIL/project3/newdatasave2.csv")
    #return updated_data
    return new_row_to_train   
