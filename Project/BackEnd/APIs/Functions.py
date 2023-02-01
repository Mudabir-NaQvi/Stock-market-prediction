import numpy as np
import pandas as pd
from keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
def getLongTermPredictions(days,company,variable):
    lst_output=[]
    predicted=[]
    n_steps=100
    path=f"..\Data\Historical Data New (sorted)\{company}.csv"
    data=pd.read_csv(path, index_col='TIME', parse_dates=True)
    data=data.sort_values(by='TIME')
    feat_data=data[variable][-100:]
    scaler=MinMaxScaler(feature_range=(0,1))
    test_data=scaler.fit_transform(np.array(feat_data).reshape(-1,1))
    path=f"../Data/Trained Models/Historical/Kaggle/{variable}/{company}.h5"
    model=load_model(path, compile=False)
    x_input=test_data[len(test_data)-100:].reshape(1,-1)
    temp_input=list(x_input)
    temp_input=temp_input[0].tolist()
    for i in range(days):
        if(len(temp_input)>100):
            x_input=np.array(temp_input[1:])
            x_input=x_input.reshape(1,-1)
            x_input = x_input.reshape((1, n_steps, 1))
            yhat = model.predict(x_input, verbose=0)
            temp_input.extend(yhat[0].tolist())
            temp_input=temp_input[1:]
            lst_output.extend(yhat.tolist())
        else:
            x_input = x_input.reshape((1, n_steps,1))
            yhat = model.predict(x_input, verbose=0)
            temp_input.extend(yhat[0].tolist())
            lst_output.extend(yhat.tolist())
        predicted.append({i+1:round(float(scaler.inverse_transform([lst_output[-1]])),1)})
    return predicted
# print(Predictions(30,'ENGRO'))




def getLongTermData(n, company,variable):
    path=f"../Data/Historical Data New (sorted)/{company}.csv"
    data=pd.read_csv(path)
    data=data.sort_values(by='TIME')
    data=data[['TIME',variable]][-100:]
    time=data["TIME"]
    values=data[variable]
    previous_data=[]
    for i in data.index:
        previous_data.append({str(time[i]):values[i]})
    return previous_data[-n:]
# getData(30,'ENGRO','HIGH')





def getShortTermPredictions(days,company):
    lst_output=[]
    predicted=[]
    n_steps=25
    path=f"../Data/Daily Data Cleaned New (Hours)/{company}.csv"
    data=pd.read_csv(path, index_col='Date', parse_dates=True)
    data=data.sort_values(by='Date')
    feat_data=data["Value"][-25:]
    scaler=MinMaxScaler(feature_range=(0,1))
    test_data=scaler.fit_transform(np.array(feat_data).reshape(-1,1))
    path=f"../Data/Trained Models/Daily/{company}.h5"
    model=load_model(path)
    x_input=test_data[len(test_data)-25:].reshape(1,-1)
    temp_input=list(x_input)
    temp_input=temp_input[0].tolist()
    for i in range(days):
        if(len(temp_input)>25):
            x_input=np.array(temp_input[1:])
            x_input=x_input.reshape(1,-1)
            x_input = x_input.reshape((1, n_steps, 1))
            yhat = model.predict(x_input, verbose=0)
            temp_input.extend(yhat[0].tolist())
            temp_input=temp_input[1:]
            lst_output.extend(yhat.tolist())
        else:
            x_input = x_input.reshape((1, n_steps,1))
            yhat = model.predict(x_input, verbose=0)
            temp_input.extend(yhat[0].tolist())
            lst_output.extend(yhat.tolist())
        predicted.append({i+1:round(float(scaler.inverse_transform([lst_output[-1]])),1)})
    return predicted
# getShortTermPredictions(8,'ENGRO')





def getShortTermData(n, company):
    path=f"../Data/Daily Data Cleaned New (Hours)/{company}.csv"
    data=pd.read_csv(path)
    data=data.sort_values(by='Date')
    time=data["Date"]
    values=data["Value"]
    previous_data=[]
    for i in data.index:
        previous_data.append({str(time[i]):values[i]})
    return previous_data[-n:]
# getShortTermData(8,'ENGRO')