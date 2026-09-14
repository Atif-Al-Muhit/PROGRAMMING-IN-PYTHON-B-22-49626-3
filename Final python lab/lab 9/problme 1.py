import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


# --------------------------------
# Load Iris Dataset
# --------------------------------

iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)

df["species"] = [
    iris.target_names[i]
    for i in iris.target
]

print("Iris Dataset:")
print(df.head())


# =================================
# 1. Line Plot
# =================================

plt.figure()

plt.plot(
    df.index[:30],
    df["sepal_length"][:30]
)

plt.title("Iris Sepal Length - Line Plot")
plt.xlabel("Sample Number")
plt.ylabel("Sepal Length")

plt.show()


# =================================
# 2. Scatter Plot
# =================================

plt.figure()

plt.scatter(
    df["sepal_length"],
    df["petal_length"]
)

plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")

plt.show()


# =================================
# 3. Bar Chart
# =================================

species_count = df["species"].value_counts()

plt.figure()

plt.bar(
    species_count.index,
    species_count.values
)

plt.title("Number of Iris Flowers by Species")
plt.xlabel("Species")
plt.ylabel("Number of Flowers")

plt.show()


# =================================
# 4. Histogram
# =================================

plt.figure()

plt.hist(
    df["sepal_length"],
    bins=10
)

plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")

plt.show()


# =================================
# 5. Pie Chart
# =================================

plt.figure()

plt.pie(
    species_count.values,
    labels=species_count.index,
    autopct="%1.1f%%"
)

plt.title("Iris Species Distribution")

plt.show()


# =================================
# 6. Subplots
# =================================

fig, ax = plt.subplots(1, 2)

# First subplot
ax[0].scatter(
    df["sepal_length"],
    df["sepal_width"]
)

ax[0].set_title("Sepal")
ax[0].set_xlabel("Sepal Length")
ax[0].set_ylabel("Sepal Width")


# Second subplot
ax[1].scatter(
    df["petal_length"],
    df["petal_width"]
)

ax[1].set_title("Petal")
ax[1].set_xlabel("Petal Length")
ax[1].set_ylabel("Petal Width")


plt.tight_layout()
plt.show()