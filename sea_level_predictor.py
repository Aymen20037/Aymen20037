import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Observed Data')

    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_pred1 = res1.intercept + res1.slope * years_extended
    plt.plot(years_extended, sea_level_pred1, 'r', label='Best Fit: 1880–2050')

    df_2000 = df[df['Year'] >= 2000]
    res2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_extended2 = pd.Series(range(2000, 2051))
    sea_level_pred2 = res2.intercept + res2.slope * years_extended2
    plt.plot(years_extended2, sea_level_pred2, 'g', label='Best Fit: 2000–2050')

    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()

    plt.savefig('sea_level_plot.png')
    return plt.gca()