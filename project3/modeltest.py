import warnings

warnings.filterwarnings("ignore")

import asyncio
import datetime
import logging
import traceback

import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor
from sklearn.metrics import r2_score
import pickle
import xgboost as xgb
from sklearn.metrics import mean_absolute_error, r2_score
from colormath.color_objects import LabColor, sRGBColor, XYZColor, LabColor
from colormath.color_diff import delta_e_cmc
from colormath.color_conversions import convert_color

from matplotlib import pyplot as plt
import matplotlib.colors as mcolors

from PIL import Image
import math
from math import sqrt
import copy
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow import keras
import tensorflow_addons as tfa
from tensorflow.keras.callbacks import ModelCheckpoint

from sklearn.preprocessing import LabelEncoder,StandardScaler,OneHotEncoder,MinMaxScaler
import pandas.core.algorithms as algos
from pandas import Series
import pickle
#from pandas import tools


from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cmc
import numpy as np
import pandas as pd
from colormath.color_objects import sRGBColor, XYZColor, LabColor
from colormath.color_conversions import convert_color
import pandas as pd
import math
import numpy as np
import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from PIL import Image
from matplotlib import pyplot as plt
import copy
from sklearn.preprocessing import LabelEncoder
import pandas.core.algorithms as algos
from pandas import Series
import pickle
#from pandas import tools


from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor,RandomForestRegressor
from sklearn.preprocessing import LabelEncoder,StandardScaler,OneHotEncoder,MinMaxScaler
from sklearn.svm import SVR
import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, LearningRateScheduler, ReduceLROnPlateau
from sklearn.linear_model import LinearRegression
from tensorflow import keras
import tensorflow_addons as tfa
import pandas as pd
import numpy as np
from tensorflow.keras import backend as K
# gpu 상태 확인 및 메모리 사용만큼 할당
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib._color_data as mcd
import matplotlib.patches as mpatch
import webcolors
from colormath.color_objects import LabColor, sRGBColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
from colormath import color_diff_matrix
import matplotlib.colors as mcolors

from math import sqrt
from sklearn.preprocessing import LabelEncoder

from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.cluster import KMeans
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

