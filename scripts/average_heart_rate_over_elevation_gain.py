"""

This script produces a scatter plot, which plots for each run
the average heart rate of the runner against the elevation gain.

"""


import pandas as pd
import matplotlib.pyplot as pplt


def main ():
    #create dataframe from "runs_formatted_date.csv"(path has to be set accordingly)
    df = pd.read_csv('/Users/jonassenn/Documents/vscode/Main/FHGR/datascience_project/Data/runs_formatted_date.csv')

    #Since not all rows of the df have a value for "Average Heart Rate", we discard the rows with no value
    df_clean = df.dropna(subset=["Average Heart Rate"])

    #Create a new column with elevation gain values being floats(df turns them into strings). 
    elevation_gain_values = []
    for elv_gain in df_clean["Elevation Gain"]:
        elevation_gain_values.append(float(elv_gain))
    df_clean["Elevation Gain floats"] = elevation_gain_values

    #plot the Average Heart Rate against Elevation Gain
    my_plot = df_clean.plot(kind="scatter", x="Elevation Gain floats", y="Average Heart Rate")
    #change the names of the x-/y-axis
    my_plot.set_xlabel("Elevation Gain in meters")
    my_plot.set_ylabel("Average Heart Rate in bpm")


    pplt.show()
    #Uncomment next line to export plot as .png
    #pplt.savefig("average_speed_plot")


if __name__ == "__main__":
    main()