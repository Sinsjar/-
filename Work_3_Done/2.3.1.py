from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

x_train, x_test, y_train, y_test = train_test_split(iris.iloc[:, :-1],

iris.iloc[:, -1], test_size = 0.15)

model = KNeighborsClassifier(n_neighbors = 5)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

plt.figure(figsize=(10, 8))
sns.scatterplot(x = 'petal_width', y = 'petal_length', data = iris, hue = 'species', s = 70)
plt.xlabel('Длиная лепестка, см')
plt.ylabel('Ширина лепестка, см')
plt.legend(loc = 2)
plt.grid()
plt.show()

for i in range(len(y_test)):
    if np.array(y_test)[i] != y_pred[i]:
        plt.scatter(x_test.iloc[i, 3], x_test.iloc[i, 2], color = 'red', s = 150)
print(f'accuracy: {accuracy_score(y_test, y_pred) :.5}')
