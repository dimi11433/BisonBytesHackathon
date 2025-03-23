import pandas as pd

df = pd.read_csv('balanced_health_data.csv')
last_col = df.columns[-1]

df[last_col] = df[last_col].astype(str)


for i in range(min(273, len(df))):
    current_value = float(df.at[df.index[i], last_col])
    if  0 <= current_value <= 2:
        new_value = "Very Low"
    elif 2 < current_value <= 4:
        new_value = "Low"
    elif 4 < current_value <= 6:
        new_value = "Medium"
    elif  6 < current_value <= 8:
        new_value = "High"
    else:
        new_value = "Very High"
    df.at[df.index[i], last_col] = new_value 
    
df.to_csv('completed_dataset.csv', index = False)
    