import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
   
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.figure(figsize=(12, 4))
    plt.scatter(x, y, label='Data points')

    # Create first line of best fit
    res = linregress(x, y)

    x_pred = pd.Series(range(x.min(), 2051))
    y_pred = res.slope * x_pred + res.intercept
    plt.plot(x_pred, y_pred, color='red', label='Regression line')

    # Create second line of best fit
    new_df = df[x >= 2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']

    new_res = linregress(new_x, new_y)

    x_pred = pd.Series(range(new_x.min(), 2051))
    y_pred = new_res.slope * x_pred + new_res.intercept
    plt.plot(x_pred, y_pred, color='blue', label='Regression line from 2000 up')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()