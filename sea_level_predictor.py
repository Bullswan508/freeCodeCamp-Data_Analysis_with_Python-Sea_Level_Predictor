import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df = pd.read_csv('./epa-sea-level.csv')

    print(df)

    # Create scatter plot

    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")





    # Create first line of best fit

    slope1, y_intercept1, *others1 = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    plt.axline(xy1=(0, y_intercept1), slope=slope1)


    # Create second line of best fit

    adjusted_df = df.loc[df["Year"] >= 2000]

    slope2, y_intercept2, *others2 = linregress(adjusted_df["Year"], adjusted_df["CSIRO Adjusted Sea Level"])

    plt.axline(xy1=(0, y_intercept2), slope=slope2, color='red')


    # Add labels and title

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.xlim(1850, 2075)
    plt.ylim(-1, 30)

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')

    return plt.gca()