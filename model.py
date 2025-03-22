# load csv into pandas

import pandas as pd
from sklearn.svm import SVC

def score_row(row):
    score = 0
    max_score = 15  # Maximum raw score before normalization

    # ------------------------
    # 1. Context-Aware Heart Rate
    # ------------------------
    hr = row['Heartrate']
    active_min = row['Active_Minutes']
    
    if hr < 60:
        score += 0  # Bradycardia concern
    elif 60 <= hr <= 100:
        score += 1  # Normal range
    elif hr > 100:
        if active_min >= 30:
            score += 1  # Elevated HR justified by activity
        else:
            score += 0  # Resting tachycardia

    # ------------------------
    # 2. Blood Pressure (Context: Hydration & Activity)
    # ------------------------
    systolic = row['BP_Systolic']
    diastolic = row['BP_Diastolic']
    water = row['Water_Intake']
    
    if 90 <= systolic <= 120:
        score += 1
    elif systolic > 120 and water >= 3.0:
        score += 0.5  # Slightly high BP but good hydration

    if 60 <= diastolic <= 80:
        score += 1
    elif diastolic > 80 and water >= 3.0:
        score += 0.5

    # ------------------------
    # 3. Respiratory Rate (12-18 normal)
    # ------------------------
    rr = row['Respiratory_Rate']
    if 12 <= rr <= 18:
        score += 1

    # ------------------------
    # 4. Temperature
    # ------------------------
    temp = row['Temp']
    if 97 <= temp <= 99:
        score += 1

    # ------------------------
    # 5. Sleep Duration & Quality & Consistency
    # ------------------------
    sleep_dur = row['Sleep_Duration']
    sleep_q = row['Sleep_Quantity']
    sleep_c = row['Sleep_Consistency']

    if 7 <= sleep_dur <= 9:
        score += 1

    if sleep_q == 0:
        score += 1
    elif sleep_q == 1:
        score += 0.5

    if sleep_c == 0:
        score += 1
    elif sleep_c == 1:
        score += 0.5

    # ------------------------
    # 6. Steps & Active Minutes (Double check consistency)
    # ------------------------
    steps = row['Steps']

    if steps >= 10000:
        score += 1
    elif steps >= 7500:
        score += 0.5

    if active_min >= 60:
        score += 1
    elif active_min >= 30:
        score += 0.5

    # ------------------------
    # 7. Strength Training (Yes = 1)
    # ------------------------
    if row['Strength_Training'] == 1:
        score += 1

    # ------------------------
    # 8. Water Intake
    # ------------------------
    if water >= 3.0:
        score += 1

    # ------------------------
    # 9. Oxygen Level
    # ------------------------
    oxygen = row['Oxygen_Level']
    if oxygen >= 95:
        score += 1

    # ------------------------
    # 10. Blood Sugar
    # ------------------------
    sugar = row['Blood_Sugar']
    if 70 <= sugar <= 100:
        score += 1

    # ------------------------
    # 11. BMI (or Weight check if BMI missing)
    # ------------------------
    bmi = row.get('BMI', None)
    if bmi:
        if 18.5 <= bmi <= 24.9:
            score += 1

    # ------------------------
    # Normalize Score to 0-9
    # ------------------------
    normalized_score = round((score / max_score) * 9)
    return normalized_score


def load_csv_with_score(file_path):
    sleep_quality_map = {
        'Good': 0,
        'Average': 1,
        'Poor': 2
    }

    bedtime_consistency_map = {
        'High': 0,
        'Moderate': 1,
        'Low': 2
    }

    strength_training_map = {
        'No': 0,
        'Yes': 1
    }


    # Load the data into a DataFrame
    df = pd.read_csv('health_dataset.csv')

    # Map the categorical data to numerical data
    df['Sleep_Quantity'] = df['Sleep_Quantity'].map(sleep_quality_map)
    df['Sleep_Consistency'] = df['Sleep_Consistency'].map(bedtime_consistency_map)
    df['Strength_Training'] = df['Strength_Training'].map(strength_training_map)
    df['Label'] = df.apply(score_row, axis=1)
    return df


def train_model(df):
    X = df.drop(columns=['Label'])
    y = df['Label']
    model = SVC()
    model.fit(X, y)
    print("Model trained successfully!")
    return model

def predict_status(model, row):
    return model.predict(row)
    
    
def main():
    df = load_csv_with_score('health_dataset.csv')
    model = train_model(df)
    row = df.iloc[0].drop('Label').values.reshape(1, -1)
    res = predict_status(model, row)
    print(res[0])

if __name__ == '__main__':
    main()