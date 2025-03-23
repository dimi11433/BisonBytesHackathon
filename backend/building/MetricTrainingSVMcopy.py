import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC 
from sklearn import svm
from sklearn.preprocessing import StandardScaler  
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


df0 = pd.read_csv("megan_dataset.csv")

X = df0.drop('Label', axis=1)
y = df0['Label']

#Split data into test and train
_, X_test, _, y_test = train_test_split(
X, y, test_size = 0.1, random_state=42)
model = SVC()
model.fit(X, y)
print("Model trained successfully!")
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", model.score(X_test, y_test))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))

# Optional: Confusion Matrix
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))

# clf = svm.SVC()
# clf.fit(X_train, y_train)

# y_pred = clf.predict(X_test)
# # Evaluate clearly with accuracy and classification report
# accuracy = accuracy_score(y_test, y_pred)
# report = classification_report(y_test, y_pred, output_dict = True)
# print(f"Accuracy: {accuracy:.2f}")
# print(classification_report(y_test, y_pred))

# # Predict clearly the label of the first row from test data
# sample =  X_test.iloc[0].values.reshape(1, -1)
# predicted_label = clf.predict(sample)

#report_df = pd.DataFrame(report).transpose()
# precison_values = [report_df.loc['High', 'precision'], report_df.loc['Low', 'precision'], report_df.loc['Medium', 'precision'], report_df.loc['macro avg', 'precision'], report_df.loc['weighted avg', 'precision']]
# precison_names = ['High', 'Low', 'Medium', 'macro avg', 'weighted avg']

# plt.bar(precison_names, precison_values)
# plt.title('Pecision Values')
# plt.xlabel('Precison Names')
# # plt.ylabel('Precision Values')
# # plt.show()
# print(f"Predicted Label: {predicted_label[0]}")
