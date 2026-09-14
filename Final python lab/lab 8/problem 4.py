import pandas as pd


titanic = pd.read_csv("titanic.csv")

print("Original Dataset:")
print(titanic.head())



print("\nMissing Values:")
print(titanic.isnull().sum())

# Fill missing Age with mean
if "Age" in titanic.columns:
    titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

# Fill missing Embarked with mode
if "Embarked" in titanic.columns:
    titanic["Embarked"] = titanic["Embarked"].fillna(
        titanic["Embarked"].mode()[0]
    )



titanic = titanic.drop_duplicates()


# Convert Age to numeric
if "Age" in titanic.columns:
    titanic["Age"] = pd.to_numeric(
        titanic["Age"], errors="coerce"
    )



# Remove impossible Age values
if "Age" in titanic.columns:
    titanic = titanic[
        (titanic["Age"] >= 0) &
        (titanic["Age"] <= 100)
    ]



print("\nCleaned Dataset:")
print(titanic.head())

print("\nMissing Values After Cleaning:")
print(titanic.isnull().sum())

print("\nDataset Information:")
titanic.info()