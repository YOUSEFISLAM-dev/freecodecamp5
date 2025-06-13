import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    plt.figure(figsize=(12, 8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], 
                alpha=0.6, s=30)
    
    # Create first line of best fit using all data
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(
        df['Year'], df['CSIRO Adjusted Sea Level']
    )
    
    # Extend line to 2050
    years_extended = np.arange(df['Year'].min(), 2051)
    line1_extended = slope1 * years_extended + intercept1
    
    plt.plot(years_extended, line1_extended, 'r-')
    
    # Create second line of best fit using data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
        df_recent['Year'], df_recent['CSIRO Adjusted Sea Level']
    )
    
    # Extend recent trend line to 2050
    years_recent = np.arange(2000, 2051)
    line2_extended = slope2 * years_recent + intercept2
    
    plt.plot(years_recent, line2_extended, 'g-')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return fig (don't change this part)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
