# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import pickle 

data=pd.read_csv("C:\\Users\\AKammari\\Downloads\\advertising.csv")
dataset = pd.DataFrame(data)
dataset.head()
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.3, random_state = 1 )
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

pickle.dump(regressor,open("model.pkl","wb"))
model = pickle.load(open('model.pkl',"rb"))