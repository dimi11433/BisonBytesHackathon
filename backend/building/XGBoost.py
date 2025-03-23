import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from xgboost import XGBClassifier, plot_importance
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


# df0 = pd.read_csv("balanced_health_data.csv")
# df1 = pd.read_csv("labeled_dataset.csv")
# df2 = pd.read_csv("50_generatedhealth_data.csv")

# df = pd.concat([df0,df2,df1], ignore_index = True)
# df.to_csv('combined.csv', index = False)

# STEP 1: Load your dataset
df = pd.read_csv("combined.csv")  # Replace with your dataset file

# STEP 2: Prepare Features & Labels
X = df.drop(columns=['Label'])
y = df['Label']

# STEP 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# STEP 4: Feature Scaling (optional for XGBoost but still helps sometimes)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# STEP 5: XGBoost Model with hyperparameter tuning
param_grid = {
    'max_depth': [5, 8, 10],
    'n_estimators': [100, 200],
    'learning_rate': [0.01, 0.1, 0.2]
}

xgb = XGBClassifier(use_label_encoder=False, eval_metric='mlogloss', random_state=42)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid = GridSearchCV(estimator=xgb, param_grid=param_grid, cv=cv, verbose=1, n_jobs=-1)
grid.fit(X_train_scaled, y_train)

# STEP 6: Evaluate
best_model = grid.best_estimator_
y_pred = best_model.predict(X_test_scaled)

print("Best Hyperparameters:", grid.best_params_)
print("Accuracy:", best_model.score(X_test_scaled, y_test))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred, zero_division=0))

# # STEP 7: Confusion Matrix Heatmap
# cm = confusion_matrix(y_test, y_pred)
# plt.figure(figsize=(8, 6))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=sorted(y.unique()), yticklabels=sorted(y.unique()))
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.title('Confusion Matrix (XGBoost)')
# plt.show()

# # STEP 8: Feature Importance Plot
# plt.figure(figsize=(10, 6))
# plot_importance(best_model, max_num_features=10)
# plt.title('Top 10 Feature Importances (XGBoost)')
# plt.show()
