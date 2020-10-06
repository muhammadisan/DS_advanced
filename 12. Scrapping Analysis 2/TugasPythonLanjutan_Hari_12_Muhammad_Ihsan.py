import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def model_knn():
  df = pd.read_csv('pulsar_stars.csv')
  x = df[[' Excess kurtosis of the integrated profile', ' Skewness of the integrated profile']]
  y = df['target_class']
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25,random_state=150)

  list_score = []
  for i in range(2,51):
    model_knn = KNN(n_neighbors=i)
    model_knn.fit(x_train, y_train)
    y_pred = model_knn.predict(x_test)
    list_score.append(accuracy_score(y_test, y_pred))

  fig, ax = plt.subplots(figsize=(16,8))
  ax.plot(range(2,51), list_score, marker='x')
  ax.set_title('Accuracy')
  ax.set_xlabel('K-Value')
  ax.set_ylabel('Scores')

  plt.show()

  knn = KNN(n_neighbors=14)
  knn.fit(x_train, y_train)
  y_pred = knn.predict(x_test)

  print(confusion_matrix(y_test, y_pred))
  print(classification_report(y_test, y_pred))

def model_svm():
  df = pd.read_csv('pulsar_stars.csv')
  x = df[[' Excess kurtosis of the integrated profile', ' Skewness of the integrated profile']]
  y = df['target_class']
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25,random_state=150)

  svm = SVC()
  svm.fit(x_train, y_train)
  y_pred_svm = svm.predict(x_test)

  print(confusion_matrix(y_test, y_pred_svm))
  print(classification_report(y_test, y_pred_svm))

model_knn()
model_svm()