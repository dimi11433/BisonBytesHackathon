import pandas as pd
import csv
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("please_work2.csv")

# Split features and target
X = df.drop(columns=['Label'])
y = df['Label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Scaling is essential for Logistic Regression!
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Logistic Regression with class weights to handle imbalance
logreg = LogisticRegression(class_weight='balanced', max_iter=1000, multi_class='multinomial', solver='lbfgs')
logreg.fit(X_train_scaled, y_train)

# Predictions
y_pred = logreg.predict(X_test_scaled)

# Evaluation
print("Accuracy:", logreg.score(X_test_scaled, y_test))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))

# # Confusion Matrix Heatmap
# cm = confusion_matrix(y_test, y_pred)
# plt.figure(figsize=(8,6))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Oranges', xticklabels=['Very Low', 'Low', 'Medium', 'High', 'Very High'], yticklabels=['Very Low', 'Low', 'Medium', 'High', 'Very High'])
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.title('Confusion Matrix (Logistic Regression)')
# plt.show()
