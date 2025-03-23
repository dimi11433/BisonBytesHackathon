import pandas as pd


# df = pd.read_csv("250_labeled_new_dataset.csv")
# df1 = pd.read_csv("completed_dataset.csv")
# df0 = pd.concat([df, df1], ignore_index=True)
# df0.to_csv('megan_dataset.csv', index = False)


#df = pd.read_csv("a_new_world1.csv")
last_col = df.columns[-1]

df[last_col] = df[last_col].astype(str)
counter_m, counter_low, counter_high, counter_vl, counter_vh = 0, 0, 0 ,0, 0
for i in range(min(523, len(df))):
    current_value = df.at[df.index[i], last_col]
    if current_value == "Very Low":
        counter_vl += 1
    elif current_value == "Low":
        counter_low += 1
    elif current_value == "Medium":
        counter_m += 1
    elif current_value == "High":
        counter_high += 1
    else:
        counter_vh += 1
print(counter_vl, counter_low, counter_m, counter_high, counter_vh)

        