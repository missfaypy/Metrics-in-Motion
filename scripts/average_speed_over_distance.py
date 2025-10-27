"""

This script produces a scatter plot, which plots the average 
running speed of each run against the total distance per run.

"""


import pandas as pd
import matplotlib.pyplot as pplt


def main ():
    #create dataframe from "runs_formatted_date.csv"(path has to be set accordingly)
    df = pd.read_csv('/Users/jonassenn/Documents/vscode/Main/FHGR/datascience_project/Data/runs_formatted_date.csv')

    #plot the Average Speed against the Distance
    my_plot = df.plot(kind="scatter", x="Distance", y="Average Speed")
    #change the names of the x-/y-axis
    my_plot.set_xlabel("Distance in km")
    my_plot.set_ylabel("Average Speed in m/s")

    pplt.show()
    #Uncomment next line to export plot as .png
    #pplt.savefig("average_speed_plot")


if __name__ == "__main__":
    main()