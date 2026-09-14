import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

df = pd.DataFrame(data)

print("Full DataFrame:")
print(df)

print("\nSelected Rows:")
print(df.loc[[0, 2]])