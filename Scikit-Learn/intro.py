# INTRODUCTION TO SCIKIT LEARN
from sklearn.datasets import load_iris

# Step1 -> Load the dataset
iris = load_iris()
# print(iris)

X = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

print("Feature Name:-", feature_names)
print("Target_Name:-",target_names)

print(type(X))
print(X[:5])
print()

# import pandas as pd

# # we can create the dataset using pandas also in X and y form input and target
# data = pd.read_csv("F:\github\python\Scikit-Learn\weather.csv")
# print(data)

# print("Shape",data.shape)
# print("features",data.columns)

# X = data[data.columns[:-1]]
# y = data[data.columns[-1]]

# print("X(Input) data:-\n",X.head())
# print()
# print("y(Target) data:-\n",y.head())

# Step2 :- Splitting the dataset

from sklearn.model_selection import train_test_split

# X, y: These are the feature matrix and response vector which need to be split.
# test_size: It is the ratio of test data to the given data. For example, setting test_size = 0.4 for 150 rows of X produces test data of 150 x 0.4 = 60 rows.
# random_state: If you use random_state = some_number, then you can guarantee that your split will be always the same.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=1)

print("X-train shape:-", X_train.shape)
print("X-test shape:-", X_test.shape)
print("y-train shape:-", y_train.shape)
print("y-test shape:-", y_test.shape)
print()

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)

y_pred = knn.predict(X_test)

from sklearn import metrics
print("KNN Model Accuracy:-",metrics.accuracy_score(y_test,y_pred))
print()

# making prediction for out of sample test
sample = [[3,5,4,2],[2,3,5,4]]
pred = knn.predict(sample)
pred_speices = [iris.target_names[p] for p in pred]
print("Predict Species:-",pred_speices)
