import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import tree

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
target = [0, 0, 0, 1, 1, 1]

X.shape

classifier = DecisionTreeClassifier()
classifier.fit(X,target)

tree.plot_tree(classifier)

y_pred = classifier.predict(X)

print(confusion_matrix(y_pred,target))
print(classification_report(y_pred,target))
