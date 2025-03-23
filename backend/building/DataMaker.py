import pandas as pd
import numpy as np

# Function to generate synthetic data
def generate_synthetic_data(num_samples):
    data = {
        'Heartrate': np.random.randint(50, 100, num_samples),
        'BP_Systolic': np.random.randint(110, 140, num_samples),
        'BP_Diastolic': np.random.randint(70, 90, num_samples),
        'Respiratory_Rate': np.random.randint(12, 20, num_samples),
        'Temp': np.round(np.random.uniform(36.5, 37.5, num_samples), 1),
        'Sleep_Duration': np.round(np.random.uniform(5, 9, num_samples), 1),
        'Steps': np.random.randint(1000, 15000, num_samples),
        'Active_Minutes': np.random.randint(10, 180, num_samples),
        'Water_Intake': np.round(np.random.uniform(1.0, 3.5, num_samples), 2),
        'Weight': np.round(np.random.uniform(50.0, 100.0, num_samples), 1),
        'BMI': np.round(np.random.uniform(18.5, 35.0, num_samples), 1),
        'Age': np.random.randint(18, 70, num_samples),
        'Oxygen_Level': np.random.randint(90, 100, num_samples),
        'Blood_Sugar': np.round(np.random.uniform(70, 140, num_samples), 1),
        'Sleep_Quantity': np.random.choice([0, 1, 2], num_samples),  # Matches your mapping!
        'Sleep_Consistency': np.random.choice([0, 1, 2], num_samples),
        'Strength_Training': np.random.choice([0, 1], num_samples)
        #'Label': np.random.choice(['Very Low', 'Low', 'Medium', 'High', 'Very High'], num_samples)
    }
    df = pd.DataFrame(data)
    return df

# Generate synthetic data
new_data = generate_synthetic_data(1000)  # Change 100 to however many rows you want


# Save it to CSV
new_data.to_csv('MaidenHeaven.csv', index=False)
print("Generated data saved to 'generated_data.csv'")
