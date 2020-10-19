import pandas as pd
import numpy as np
from sklearn import *
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import tree

phishing_dataset = np.genfromtxt('phishing_dataset.csv', delimiter=',', dtype=np.int32)

samples = phishing_dataset[:,:-1]
targets = phishing_dataset[:, -1]

training_samples, testing_samples, training_targets, testing_targets = train_test_split(samples, targets, test_size=0.2, random_state=0)

tree_classifier = tree.DecisionTreeClassifier()
tree_classifier.fit(training_samples, training_targets)

predictions = tree_classifier.predict(testing_samples)
accuracy = 100.0 * accuracy_score(testing_targets, predictions)
print("Decision Tree Accuracy : " + str(accuracy))