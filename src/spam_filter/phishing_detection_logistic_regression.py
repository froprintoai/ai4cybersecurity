import pandas as pd
import numpy as np
from sklearn import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

phishing_dataset = np.genfromtxt('phishing_dataset.csv', delimiter=',', dtype=np.int32)
print(phishing_dataset)

samples = phishing_dataset[:,:-1]
targets = phishing_dataset[:, -1]

training_samples, testing_samples, trainint_targets, testing_targets = train_test_split(samples, targets, test_size=0.2, random_state=0)

log_classifier = LogisticRegression()

log_classifier.fit(training_samples, trainint_targets)

predictions = log_classifier.predict(testing_samples)
accuracy = 100.0 * accuracy_score(testing_targets, predictions)
print("Logistic Regression Accuracy : " + str(accuracy))