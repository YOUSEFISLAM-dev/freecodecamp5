import pandas as pd
from scipy.stats import linregress

# Read the data
df = pd.read_csv('epa-sea-level.csv')

print(f"Dataset shape: {df.shape}")
print(f"Years: {df['Year'].min()} to {df['Year'].max()}")
print(f"First few rows:")
print(df.head())
print(f"Last few rows:")
print(df.tail())

# Check for any missing values
print(f"\nMissing values in CSIRO column: {df['CSIRO Adjusted Sea Level'].isna().sum()}")

# All data regression
slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
print(f"\nAll data regression:")
print(f"Slope: {slope1:.6f} (expected: 0.096412)")
print(f"Intercept: {intercept1:.6f} (expected: -181.794118)")

# Test predictions
pred_1880 = slope1 * 1880 + intercept1
pred_2050 = slope1 * 2050 + intercept1
print(f"Predictions: 1880={pred_1880:.2f} (expected: -0.54), 2050={pred_2050:.2f} (expected: 15.85)")

# Recent data regression (2000+)
df_recent = df[df['Year'] >= 2000]
print(f"\nRecent data ({len(df_recent)} rows):")
print(df_recent)

slope2, intercept2, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
print(f"\nRecent data regression:")
print(f"Slope: {slope2:.6f} (expected: 0.148600)")
print(f"Intercept: {intercept2:.6f} (expected: -290.250000)")

# Test predictions
pred_2000 = slope2 * 2000 + intercept2
pred_2050_recent = slope2 * 2050 + intercept2
print(f"Predictions: 2000={pred_2000:.2f} (expected: 6.95), 2050={pred_2050_recent:.2f} (expected: 14.38)")

print("\n" + "="*50)
print("DIFFERENCES:")
print(f"Slope 1 diff: {abs(slope1 - 0.096412):.6f}")
print(f"Slope 2 diff: {abs(slope2 - 0.148600):.6f}")
