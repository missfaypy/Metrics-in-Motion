"""
This script creates a scatter plot from the data in "runs_formatted_date.csv", by
plotting the calories burned per run against the distance of each run.

"""

import pandas as pd
import matplotlib.pyplot as pplt


def main ():
    #create dataframe from "runs_formatted_date.csv"
    df = pd.read_csv('/Users/jonassenn/Documents/vscode/Main/FHGR/datascience_project/Data/runs_formatted_date.csv')

    #plot the Calories against the Distance
    my_plot = df.plot(kind="scatter", x="Distance", y="Calories")
    #change the names of the x-/y-axis
    my_plot.set_xlabel("Distance in km")
    my_plot.set_ylabel("Calories burned")

    pplt.show()
    #Uncomment next line to export plot as .png
    #pplt.savefig("average_speed_plot")


if __name__ == "__main__":
    main()
