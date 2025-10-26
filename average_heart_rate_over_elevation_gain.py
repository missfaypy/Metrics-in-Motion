"""

This script produces a scatter plot, which plots for each run
the average heart rate of the runner against the elevation gain.

"""


import pandas as pd
import matplotlib.pyplot as pplt


def main ():
    #create dataframe from "runs_formatted_date.csv"
    df = pd.read_csv('/Users/jonassenn/Documents/vscode/Main/FHGR/datascience_project/Data/runs_formatted_date.csv')

    #Since not all rows of the df have a value for "Average Heart Rate", we discard the rows with no value
    df_clean = df.dropna(subset=["Average Heart Rate"])

    # elevation_gain_ints = []
    # for rate in df_clean["Elevation Gain"]:
    #     elevation_gain_ints.append(rate)
    # df_clean["Elevation Gain ints"] = elevation_gain_ints
    # print(df_clean["Elevation Gain ints"])
    





    #plot the Average Heart Rate against Elevation Gain
    my_plot = df_clean.plot(kind="scatter", x="Elevation Gain", y="Average Heart Rate")
    #change the names of the x-/y-axis
    my_plot.set_xlabel("Elevation Gain in meters")
    my_plot.set_ylabel("Average Heart Rate in bpm")
    #change the ticks of the y-axis and name them accordingly
    #pplt.xticks([0,50,100,200])

    pplt.show()
    #Uncomment next line to export plot as .png
    #pplt.savefig("average_speed_plot")


if __name__ == "__main__":
    main()