#LSTM 모델 설계
from modeltest import * 
#LSTM 모델 설계
def model_build():
    keras.backend.clear_session()

    ##범주형변수, 수치형 변수 갯수 만큼 설정
    cate_input = keras.layers.Input((12,))
    num_input = keras.layers.Input((158,))

    #카테고리변수설정(모두 소재)
    emb1 = keras.layers.Embedding(1,8)(cate_input[:,0])
    emb2 = keras.layers.Embedding(1,8)(cate_input[:,1])
    emb3 = keras.layers.Embedding(1,8)(cate_input[:,2])
    emb4 = keras.layers.Embedding(1,8)(cate_input[:,3])
    emb5 = keras.layers.Embedding(1,8)(cate_input[:,4])
    emb6 = keras.layers.Embedding(1,8)(cate_input[:,5])
    emb7 = keras.layers.Embedding(1,8)(cate_input[:,6])
    emb8 = keras.layers.Embedding(1,8)(cate_input[:,7])
    emb9 = keras.layers.Embedding(1,8)(cate_input[:,8])
    emb10 = keras.layers.Embedding(1,8)(cate_input[:,9])
    emb11 = keras.layers.Embedding(1,8)(cate_input[:,10])
    emb12 = keras.layers.Embedding(1,8)(cate_input[:,11])

    #소재 부
    part1_layer = keras.layers.Concatenate()([num_input[:,0:24],
                                              emb1,emb2,emb3,emb4,
                                              emb5,emb6,emb7,emb8,
                                              emb9,emb10,emb11,emb12
                                             ])
    part1_layer = keras.layers.Dense(96,activation="selu")(part1_layer)
    part1_layer = keras.layers.Dropout(0.3)(part1_layer)
    part1_layer = tf.expand_dims(part1_layer,axis=1)
    print(part1_layer.shape)  # 여기를 수정했습니다.

    # 전처리_1차
    part2_layer = keras.layers.Dense(24,activation="selu")(num_input[:,24:52])
    part2_layer = keras.layers.Dense(96,activation="selu")(part2_layer)
    part2_layer = keras.layers.Dropout(0.3)(part2_layer)
    print(part2_layer.shape)  # 여기를 수정했습니다.
    part2_layer = tf.expand_dims(part2_layer,axis=1)

    # 전처리_2차
    part3_layer = keras.layers.Dense(24,activation="selu")(num_input[:,52:58])
    part3_layer = keras.layers.Dense(96,activation="selu")(part3_layer)
    part3_layer = keras.layers.Dropout(0.3)(part3_layer)
    print(part3_layer.shape)  # 여기를 수정했습니다.
    part3_layer = tf.expand_dims(part3_layer,axis=1)

    # 배합부
    part4_layer = keras.layers.Concatenate()([num_input[:,58:82],num_input[:,140:158]])
    part4_layer = keras.layers.Dense(96,activation="selu")(part4_layer)
    part4_layer = keras.layers.Dropout(0.3)(part4_layer)
    print(part4_layer.shape)
    part4_layer = tf.expand_dims(part4_layer,axis=1)

    # 염색부
    part5_layer = keras.layers.Dense(24,activation="selu")(num_input[:,82:104])

    part5_layer = keras.layers.Dense(96,activation="selu")(part5_layer)
    part5_layer = keras.layers.Dropout(0.3)(part5_layer)
    print(part5_layer.shape)
    part5_layer = tf.expand_dims(part5_layer,axis=1)

    #후처리부
    part6_layer = keras.layers.Dense(24,activation="selu")(num_input[:,104:134])
    part6_layer = keras.layers.Dense(96,activation="selu")(part6_layer)
    part6_layer = keras.layers.Dropout(0.3)(part6_layer)
    print(part6_layer.shape)
    part6_layer = tf.expand_dims(part6_layer,axis=1)

    #후가공_1차 공정
    part7_layer = keras.layers.Dense(24,activation="selu")(num_input[:,134:136])
    print(part7_layer.shape)  # 여기를 수정했습니다.
    part7_layer = keras.layers.Dense(96,activation="selu")(part7_layer)
    part7_layer = keras.layers.Dropout(0.3)(part7_layer)
    part7_layer = tf.expand_dims(part7_layer,axis=1)

    #후가공_2차 공정
    part8_layer = keras.layers.Dense(24,activation="selu")(num_input[:,136:140])
    part8_layer = keras.layers.Dense(96,activation="selu")(part8_layer)
    part8_layer = keras.layers.Dropout(0.3)(part8_layer)
    part8_layer = tf.expand_dims(part8_layer,axis=1)

    # Concatenate
    total_concat_be = keras.layers.Concatenate(axis=1)([part8_layer,
                                                        part7_layer,
                                                        part6_layer,
                                                        part5_layer,
                                                        part4_layer,
                                                        part3_layer,
                                                        part2_layer,
                                                        part1_layer])
    # total_concat_be2  = AttentionLayer(96,96,2,0.01)(total_concat_be)

    # LSTM Layer
    total_concat = keras.layers.LSTM(96)(total_concat_be)

    # Dense Layer
    total_concat = keras.layers.Concatenate()([total_concat,num_input,
                                              #  total_concat_be2
                                               ])
    total_concat = keras.layers.Dense(96,activation="selu")(total_concat)

    output = keras.layers.Dense(3,name="l_loss")(total_concat)

    # CIE94 Keras Custom Loss 함수 설계
    def cie94(y_true, y_pred):
        """Calculate color difference by using CIE94 formulae

        See http://en.wikipedia.org/wiki/Color_difference or
        http://www.brucelindbloom.com/index.html?Eqn_DeltaE_CIE94.html.

        cie94(rgb2lab((255, 255, 255)), rgb2lab((0, 0, 0)))
        >>> 58.0
        cie94(rgb2lab(rgb(0xff0000)), rgb2lab(rgb('#ff0000')))
        >>> 0.0
        """

        L1, a1, b1 = y_true[:,0],y_true[:,1],y_true[:,2]
        L2, a2, b2 = y_pred[:,0],y_pred[:,1],y_pred[:,2]


        C1 = K.sqrt(K.pow(a1,2) + K.pow(b1,2))
        C2 = K.sqrt(K.pow(a2,2) + K.pow(b2,2))
        delta_L = L1 - L2
        delta_C = C1 - C2
        delta_a = a1 - a2
        delta_b = b1 - b2
        delta_H_square = K.pow(delta_a,2) + K.pow(delta_b,2) - K.pow(delta_C,2)
        loss_a = (K.sqrt(K.pow(delta_L,2)
                + K.pow(delta_C,2) / K.pow(1.0 + 0.045 * C1,2)
                + delta_H_square / K.pow(1.0 + 0.015 * C1,2)))
        return loss_a

    model = keras.models.Model(inputs=[cate_input,num_input],outputs=output)
    model.compile(optimizer=tf.keras.optimizers.Adam(0.01),loss=[cie94], metrics=[cie94])
    return(model)

    # CIE94 Keras Custom Loss 함수 설계
    def cie94(y_true, y_pred):
        """Calculate color difference by using CIE94 formulae

        See http://en.wikipedia.org/wiki/Color_difference or
        http://www.brucelindbloom.com/index.html?Eqn_DeltaE_CIE94.html.

        cie94(rgb2lab((255, 255, 255)), rgb2lab((0, 0, 0)))
        >>> 58.0
        cie94(rgb2lab(rgb(0xff0000)), rgb2lab(rgb('#ff0000')))
        >>> 0.0
        """

        L1, a1, b1 = y_true[:,0],y_true[:,1],y_true[:,2]
        L2, a2, b2 = y_pred[:,0],y_pred[:,1],y_pred[:,2]


        C1 = K.sqrt(K.pow(a1,2) + K.pow(b1,2))
        C2 = K.sqrt(K.pow(a2,2) + K.pow(b2,2))
        delta_L = L1 - L2
        delta_C = C1 - C2
        delta_a = a1 - a2
        delta_b = b1 - b2
        delta_H_square = K.pow(delta_a,2) + K.pow(delta_b,2) - K.pow(delta_C,2)
        loss_a = (K.sqrt(K.pow(delta_L,2)
                + K.pow(delta_C,2) / K.pow(1.0 + 0.045 * C1,2)
                + delta_H_square / K.pow(1.0 + 0.015 * C1,2)))
        return loss_a

    model = keras.models.Model(inputs=[cate_input,num_input],outputs=output)
    model.compile(optimizer=tf.keras.optimizers.Adam(0.01),loss=[cie94], metrics=[cie94])
    return(model)



# lab를 rgb로 변환하는 함수
def lab_to_rgb(data):
    r_list=[]
    g_list=[]
    b_list=[]
    for i in range(len(data)):
        lab=LabColor(data[data.columns[0]][data.index[i]],data[data.columns[1]][data.index[i]],data[data.columns[2]][data.index[i]])#lab좌표
        rgb=convert_color(lab,sRGBColor)#rgb좌표
        rgb_list=[color for color in rgb.get_value_tuple()]
        r_list.append(rgb_list[0])
        g_list.append(rgb_list[1])
        b_list.append(rgb_list[2])
    df = pd.DataFrame(
                {'r' : r_list,
                 'g' : g_list,
                 'b' : b_list}
                )
    df.index=data.index
    return(df)

# CMC 색차를 계산합니다.
def cmc_color_difference(Lab1, Lab2, l=1, c=1):

    # CMC 색차를 계산합니다.
    SL = 0.04079 * Lab1[0] + 0.968 * Lab1[0] / 100
    SC = 0.06377 * Lab1[1] + 0.839 * Lab1[1] / 100
    SH = 0.07275 * Lab1[2] + 1.037 * Lab1[2] / 100

    delta_L = Lab2[0] - Lab1[0]
    delta_C = Lab2[1] - Lab1[1]
    delta_H = Lab2[2] - Lab1[2]

    delta_E = ((delta_L / (l * SL)) ** 2 + (delta_C / (c * SC)) ** 2 + (delta_H / SH) ** 2) ** 0.5

    return delta_E


def cie94_color_difference(y_pred, y_true):
    """Calculate color difference by using CIE94 formulae

    See http://en.wikipedia.org/wiki/Color_difference or
    http://www.brucelindbloom.com/index.html?Eqn_DeltaE_CIE94.html.

    cie94(rgb2lab((255, 255, 255)), rgb2lab((0, 0, 0)))
    >>> 58.0
    cie94(rgb2lab(rgb(0xff0000)), rgb2lab(rgb('#ff0000')))
    >>> 0.0
    """

    L1, a1, b1 = y_true[0],y_true[1],y_true[2]
    L2, a2, b2 = y_pred[0],y_pred[1],y_pred[2]


    C1 = np.sqrt(a1**2 + b1**2)
    C2 = K.sqrt(K.pow(a2,2) + K.pow(b2,2))
    delta_L = L1 - L2
    delta_C = C1 - C2
    delta_a = a1 - a2
    delta_b = b1 - b2
    delta_H_square = delta_a**2 + delta_b**2 - delta_C**2
    loss_a = (np.sqrt((delta_L)**2
            + (delta_C)**2 / (1.0 + 0.045 * C1)**2
            + delta_H_square / (1.0 + 0.015 * C1)**2))
    return loss_a