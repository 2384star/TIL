import math
import matplotlib.pyplot as plt
import numpy as np

def lab2rgb(l_s, a_s, b_s):
    var_Y = (l_s + 16) / 116.0
    var_X = a_s / 500.0 + var_Y
    var_Z = var_Y - b_s / 200.0

    if var_Y**3 > 0.008856:
        var_Y = var_Y**3
    else:
        var_Y = (var_Y - 16/116) / 7.787
    if var_X**3 > 0.008856:
        var_X = var_X**3
    else:
        var_X = (var_X - 16/116) / 7.787
    if var_Z**3 > 0.008856:
        var_Z = var_Z**3
    else:
        var_Z = (var_Z - 16/116) / 7.787

    X = 95.047 * var_X
    Y = 100.000 * var_Y
    Z = 108.883 * var_Z

    var_X = X / 100.0
    var_Y = Y / 100.0
    var_Z = Z / 100.0

    var_R = var_X * 3.2406 + var_Y * -1.5372 + var_Z * -0.4986
    var_G = var_X * -0.9689 + var_Y * 1.8758 + var_Z * 0.0415
    var_B = var_X * 0.0557 + var_Y * -0.2040 + var_Z * 1.0570

    if var_R > 0.0031308:
        var_R = 1.055 * (var_R ** (1/2.4)) - 0.055
    else:
        var_R = 12.92 * var_R
    if var_G > 0.0031308:
        var_G = 1.055 * (var_G ** (1/2.4)) - 0.055
    else:
        var_G = 12.92 * var_G
    if var_B > 0.0031308:
        var_B = 1.055 * (var_B ** (1/2.4)) - 0.055
    else:
        var_B = 12.92 * var_B

    R = var_R * 255.0
    G = var_G * 255.0
    B = var_B * 255.0

    return R, G, B

def plot_rgb_color(df):
    color = df.iloc[0][['R', 'G', 'B']].values
    color = color / 255 if np.any(color > 1) else color

    fig, ax = plt.subplots(figsize=(2, 2))  # figure와 axis를 생성
    ax.imshow([[(color[0], color[1], color[2])]])  # RGB 값으로 채워진 이미지 생성
    ax.axis('off')  # 축을 숨깁니다.
    return fig