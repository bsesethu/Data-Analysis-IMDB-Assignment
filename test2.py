import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Copy-paste from Gemini
# 1. Prepare numeric data
data = np.random.rand(4, 5) * 100 # Example numeric data

# 2. Prepare string annotations (e.g., categories, labels, or combined info)
annotations = np.array([
    ["Cat A", "Dog B", "Bird C", "Fish D", "Lion E"],
    ["Alpha 1", "Beta 2", "Gamma 3", "Delta 4", "Epsilon 5"],
    ["X-ray", "Yacht", "Zebra", "Apple", "Banana"],
    ["One", "Two", "Three", "Four", "Five"]
])

# Ensure annotations have the same shape as data
if annotations.shape != data.shape:
    raise ValueError("Shape of annotations must match shape of data.")

# Create a DataFrame for better labeling (optional)
df_data = pd.DataFrame(data, index=[f'Row {i+1}' for i in range(data.shape[0])],
                       columns=[f'Col {j+1}' for j in range(data.shape[1])])
df_annotations = pd.DataFrame(annotations, index=df_data.index, columns=df_data.columns)


# 3. Create the heatmap with string annotations
plt.figure(figsize=(8, 6))
sns.heatmap(df_data, annot=df_annotations, fmt="", cmap="viridis", linewidths=.5)
plt.title("Heatmap with String Annotations")
plt.show()