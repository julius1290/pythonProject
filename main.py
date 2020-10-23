# Imports
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# Import Data
data = pd.read_csv('Data.csv')
x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values



# Take care of mising data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])


# Encoding indepented Variable
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
columnTransformer = ColumnTransformer(transformers=[('enocder', OneHotEncoder(), [0])], remainder='passthrough')

x = np.array(columnTransformer.fit_transform(x))


#Encode depented class
from sklearn.preprocessing import LabelEncoder
labelEncoder = LabelEncoder()
y = labelEncoder.fit_transform(y)


# Split in Test and training
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)


# Feature Scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train[:, 3:] = scaler.fit_transform(x_train[:, 3:])
x_test[:, 3:] = scaler.transform(x_test[:, 3:])

print(x_train)
print(x_test)

value1 = input("Please give a number\n")
v1 = float(value1)

r1 = v1**2*math.pi

print(r1)

import sys
sys.exit()






















