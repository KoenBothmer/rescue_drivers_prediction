import pandas as pd
import os
import shutil
import pickle
from sklearn.linear_model import LinearRegression
import six
import sys
import joblib
sys.modules['sklearn.externals.joblib'] = joblib
sys.modules['sklearn.externals.six'] = six
from pmdarima import auto_arima
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

drivers_model = pickle.load(open("drivers_model.sav", 'rb'))
calls_model = pickle.load(open("calls_model.sav", 'rb'))
sick_model = pickle.load(open("sick_model.sav", 'rb'))

def update_df(last_csv,new_csv):
    df_last = pd.read_csv(last_csv, index_col='date', parse_dates=True)
    df_last.head()
    df_last = pd.DataFrame(df_last[['n_sick', 'calls']].copy())

    df_new = pd.read_csv(new_csv, index_col='date', parse_dates=True)
    df_new = pd.DataFrame(df_new[['n_sick', 'calls']].copy())
    
    df_new = df_last.append(df_new)
    df_new.to_csv("df_up_to_date.csv")
    
    shutil.move(new_csv,'Archive/')
    
    return df_new

def predict(df):
    df['n_sick_monthly'] = df['n_sick'].resample('MS').mean()
    df['calls_monthly'] = df['calls'].resample('MS').mean()
    df_c=df
    df_s=df
    df_c=df_c.drop(['n_sick','calls','n_sick_monthly'],1)
    df_s=df_s.drop(['n_sick','calls','calls_monthly'],1)
    df_c=df_c.dropna()
    df_s=df_s.dropna()
    
    calls_model.fit(df_c)
    sick_model.fit(df_s)

    predicted_calls = calls_model.predict(1)  
    predicted_sick = sick_model.predict(1)[0]
    
    drivers_predicted = drivers_model.predict([predicted_calls])
    return [drivers_predicted[0][0] + predicted_sick,predicted_calls[0], predicted_sick]

filelist = (os.listdir('Updates'))
if (len(filelist)>0):
    if(filelist[0].endswith(".csv")):
        df = update_df('df_up_to_date.csv','Updates/'+filelist[0])
        prediction = predict(df)
else: print("No updates available")
print(prediction)

predicted = predict(df)
dict = {'drivers_predicted': predicted[0], 'calls_predicted': predicted[1], 'sick_predicted': predicted[2]}  
df_r = pd.DataFrame(dict, index=[0]) 
    
df_r.to_csv('prediction.csv')
 