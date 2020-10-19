import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt

df = pd.read_csv('sms_spam_svm.csv')
y = df.iloc[:, 0].values
X = df.iloc[:, [1,2]].values
y = np.where(y == 'spam', -1, 1)

# scatter plot
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
X_ham = [X[i] for i in range(len(X)) if y[i] == 1]
X_spam = [X[i] for i in range(len(X)) if y[i] == -1]
ax.scatter([e[0] for e in X_ham], [e[1] for e in X_ham], color='r')
ax.scatter([e[0] for e in X_spam], [e[1] for e in X_spam], color='b')
ax.set_xlabel('suspect')
ax.set_ylabel('neutral')
ax.set_title('scatter plot')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

svm = SVC(kernel='linear', C=1.0, random_state=0)
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)

print('Misclassified samples: %d' % (y_test != y_pred).sum())
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))