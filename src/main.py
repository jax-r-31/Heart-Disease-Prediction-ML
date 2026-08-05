# Importing necessary libraries.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import preprocessing

# Loading and handling missing values from the dataset.
disease_df = pd.read_csv("../dataset/dataset.csv")
disease_df.drop(columns=["education"], inplace=True, axis=1)
disease_df.rename(columns={"male":"Sex_male"}, inplace=True)

disease_df.dropna(axis=0, inplace=True)
disease_df

print(disease_df.TenYearCHD.value_counts())

# Splitting the dataset into Train and Test sets.
X = np.asarray(disease_df[["age", "Sex_male", "cigsPerDay", "totChol", "sysBP", "glucose"]])
y = np.asarray(disease_df["TenYearCHD"])
X = preprocessing.StandardScaler().fit(X).transform(X)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=4)
print("Train set: ", X_train.shape, y_train.shape)
print("Test set: ", X_test.shape, y_test.shape) 

# This shows how many individuals have heart disease (1) vs. how many don’t (0).
plt.figure(figsize=(7, 5))
sns.countplot(x="TenYearCHD", data=disease_df, palette="BuGn_r")
plt.show()

# Counting number of patients affected by CHD where (0= Not Affected; 1= Affected).
laste = disease_df["TenYearCHD"].plot()
plt.show(laste)

# Creating the model.
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)

# Evaluating Logistic regression model.
from sklearn.metrics import accuracy_score
print("Accuracy of the Logistic Regression model: ", accuracy_score(y_test, y_pred))

# Plotting the confusion matrix.
from sklearn.metrics import confusion_matrix, classification_report

print("The details for Confusion Matrix is: ")
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
con_matrix = pd.DataFrame(data=cm, 
                          columns=["Predicted: 0", "Predicted: 1"], 
                          index=["Acutal: 0", "Actual: 1"])
plt.figure(figsize=(8, 5))
sns.heatmap(con_matrix, annot=True, fmt="d", cmap="Reds")

plt.show()

