import pandas as pd
data1['时间标识']=data1['年'].map(str)+'-'+data1['月'].map(str)+'-'+data1['日'].map(str)
data1['时间标识'].nunique()
data2['时间标识']=data2['年'].map(str)+'-'+data2['月'].map(str)+'-'+data2['日'].map(str) 
data2['时间标识'],nunique()
data=data1.merge(data2, left_on='时间标识', right_on='时间标识',how='left')
data=data[['年_x', '月_x', '日_x', 'AQI', '质量等级', 'PM10', 'O3', 'SO2', 'PM2.5', 'NO2',
       'CO', '时间标识',  '降水量', '平均气压', '平均2分钟风速',        '平均气温', '平均相对湿度']]
data.columns=['年', '月', '日', 'AQI', '质量等级', 'PM10', 'O3', 'SO2', 'PM2.5', 'NO2',
       'CO', '时间标识',  '降水量', '平均气压', '平均2分钟风速',
       '平均气温', '平均相对湿度']
data.isnull (). sum()
data.dropna(inplace=True)
data,rest_index(inplace=True,drop=True)
data3=pd.concat([data[['年', '月', '日','时间标识', 'AQI', 'PM10', 'O3', 'SO2', 'PM2.5', 'NO2',
       'CO',   '降水量', '平均气压', '平均2分钟风速',
       '平均气温', '平均相对湿度']],pd.get_dummies(data['质量等级'],prefix='质量等级')],axis=1) 
import pandas
as pd import
numpy as np
import xgboost
as xgb
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from lightgbm import LGBMRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split import matplotlib.pyplot as plt import warnings
warnings.filterwarnings('ignore')
from math import sqrt
# 分离X和Y
X= data3[['年', '月', '日','AQI', 'PM10', 'O3', 'SO2',  'NO2', 'CO',
       '降水量', '平均气压', '平均2分钟风速', '平均气温', '平均相对湿度', '质量等级_严重污染', '质
       '质量等级_优', '质量等级_无', '质量等级_良', '质量等级_轻度污染', '质量等级_重度污染']]
