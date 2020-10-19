import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv('sms_spam_perceptron.csv')
X = df.iloc[:, [1, 2]].values
y = df.iloc[:, 0].values
y = np.where(y == 'spam', -1, 1)

linear_regression = LinearRegression()
linear_regression.fit(X,y)
print(linear_regression.score(X,y))
