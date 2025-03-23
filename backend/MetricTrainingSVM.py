import csv
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC 
from sklearn import svm
from sklearn.preprocessing import StandardScaler  
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix



df0 = pd.read_csv("TheWorldOverHeaven.csv")

X = df0.drop('Label', axis=1)
y = df0['Label']

#Split data into test and train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.3, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# SVM with class_weight and hyperparameter tuning
param_grid = {
    'C': [0.1, 1, 10],
    'gamma': [0.01, 0.1, 1],
    'kernel': ['rbf', 'linear']
}

grid = GridSearchCV(SVC(class_weight='balanced', probability=True), param_grid, cv=5, verbose=1)
grid.fit(X_train_scaled, y_train)

best_model = grid.best_estimator_

y_pred = best_model.predict(X_test_scaled)

# Evaluation
print("Best Hyperparameters:", grid.best_params_)
print("Accuracy:", best_model.score(X_test_scaled, y_test))
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
