import pandas as pd
import json
df = pd.read_csv('health_dataset.csv')

json_data = []
headers = df.columns.values
i = 0
for _, row in df.iterrows():
    if i == 10:
        break
    i += 1
    json_data.append(dict(zip(headers, row)))
    
# write to json file
with open('health_dataset.json', 'w') as f:
    json.dump(json_data, f, indent=4)
