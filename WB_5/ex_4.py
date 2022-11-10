"""Постройте классификатор на основе дерева принятия решений"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix

x = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
target = [0, 0, 0, 1, 1, 1]

x_train, x_test, y_train, y_test = train_test_split(
    x, target, test_size=0.2
)

classifier = DecisionTreeClassifier()
classifier.fit(x_train, y_train)
tree.plot_tree(classifier)
y_pred = classifier.predict(x_test)

print(y_pred)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
