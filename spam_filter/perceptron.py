import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

df = pd.read_csv('sms_spam_perceptron.csv')
y = df.iloc[:, 0].values # row : all  / column : 0
y = np.where(y == 'spam', -1, 1)
X = df.iloc[:, [1, 2]].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0) # 30% -> test

p = Perceptron(max_iter=40, eta0=0.1, random_state=0)
p.fit(X_train, y_train)

y_pred = p.predict(X_test)

print('Misclassified samples: %d' % (y_test != y_pred).sum())
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

