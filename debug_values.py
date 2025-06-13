import pandas as pd
import numpy as np
from scipy.stats import linregress

# Read data
df = pd.read_csv('epa-sea-level.csv')

print(f"Dataset has {len(df)} rows")
print(f"Year range: {df['Year'].min()} to {df['Year'].max()}")

# Calculate first line of best fit (all data)
slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
print(f"\nAll data regression:")
print(f"Slope: {slope1:.6f}")
print(f"Intercept: {intercept1:.6f}")

# Predict for 1880 and 2050
y_1880 = slope1 * 1880 + intercept1
y_2050 = slope1 * 2050 + intercept1
print(f"Line 1 - 1880: {y_1880:.6f}, 2050: {y_2050:.6f}")

# Calculate second line of best fit (2000 onwards)
df_recent = df[df['Year'] >= 2000]
print(f"\nData from 2000: {len(df_recent)} rows")
slope2, intercept2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
print(f"Recent data regression:")
print(f"Slope: {slope2:.6f}")
print(f"Intercept: {intercept2:.6f}")

# Predict for 2000 and 2050
y_2000 = slope2 * 2000 + intercept2
y_2050_recent = slope2 * 2050 + intercept2
print(f"Line 2 - 2000: {y_2000:.6f}, 2050: {y_2050_recent:.6f}")

print("\nExpected test values:")
print("Line 1: 1880 -> -0.54, 2050 -> 15.85")
print("Line 2: 2000 -> 6.95, 2050 -> 14.38")
