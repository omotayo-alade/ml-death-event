# Importing the libraries
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

# Loading dataset
dataset = pd.read_csv('data/processed/processed_data.csv')

x = dataset[['CP', 'EF', 'SC', 'Time']]
y = dataset['Death_Event']

# Splitting dataset into training and testing data
np.random.seed(25)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Creating and fitting pipeline
lr = LogisticRegression(solver='liblinear', penalty='l2', C=1, max_iter=200)
model = Pipeline([('scaler', StandardScaler()), ('estimator', lr)])
model = model.fit(x_train, y_train)

# Saving model to disk
pickle.dump(model, open('outputs/models/model.pkl','wb'))