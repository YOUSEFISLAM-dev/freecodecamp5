import pandas as pd
from scipy.stats import linregress

# Load and analyze the data
df = pd.read_csv('epa-sea-level.csv')
print('Dataset shape:', df.shape)
print('Year range:', df['Year'].min(), 'to', df['Year'].max())
print('\nSample of the data:')
print(df.head())
print('\nData from 2000 onwards:')
df_recent = df[df['Year'] >= 2000]
print(df_recent)
print('\nLast few rows:')
print(df.tail())

# Calculate regression for all data
slope1, intercept1, r_value1, p_value1, std_err1 = linregress(
    df['Year'], df['CSIRO Adjusted Sea Level']
)
print(f'\nAll data regression:')
print(f'Slope: {slope1}, Intercept: {intercept1}')
print(f'Prediction for 2050: {slope1 * 2050 + intercept1}')

# Calculate regression for data from 2000 onwards
slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
    df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
)
print(f'\n2000+ data regression:')
print(f'Slope: {slope2}, Intercept: {intercept2}')
print(f'Prediction for 2050: {slope2 * 2050 + intercept2}')
print(f'Value at 2000: {slope2 * 2000 + intercept2}')
