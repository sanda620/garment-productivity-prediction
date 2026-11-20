
import os
from ucimlrepo import fetch_ucirepo

# Create the raw data directory
os.makedirs("data/raw", exist_ok=True)

# Download the Garment Productivity dataset
dataset = fetch_ucirepo(id=597)

df = dataset.data.original

# Save the dataset
df.to_csv("data/raw/garment_productivity.csv", index=False)

# Display dataset information
print("Dataset downloaded successfully!")
print("Shape:", df.shape)
print(df.head())
df.info()
