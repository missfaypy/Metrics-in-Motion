"""

This script produces a scatter plot, which shows the runners average speed per run on 
different (starting-)times of the day, using the data from "runs_formatted_date.csv".

"""


import pandas as pd
import matplotlib.pyplot as pplt


def main ():
    #create dataframe from "runs_formatted_date.csv"
    df = pd.read_csv('/Users/jonassenn/Documents/vscode/Main/FHGR/datascience_project/Data/runs_formatted_date.csv')

    #for every "Formatted Date"-string, get rid of everything except h:m, turn h:m into an int by adding up total minutes, append this int to time_of_day_ints.
    time_of_day_ints = []
    for date in df["Formatted Date"]:
        _, time_of_day = date.rsplit(" ", 1)
        hours, minutes = time_of_day.split(":")
        time_of_day_ints.append((int(hours)*60)+int(minutes))   
    #add the list back as a column to the dataframe
    df["time_of_day_as_int"] = time_of_day_ints


    #take the new column and plot it against Average Speed
    my_plot = df.plot(kind="scatter", x="Average Speed", y="time_of_day_as_int")
    #change the names of the y-axis
    my_plot.set_ylabel("Time of Day")
    #change the ticks of the y-axis and name them accordingly
    pplt.yticks([0,360,720,1080,1440],["0:00", "6:00", "12:00", "18:00", "24:00"])
    pplt.show()
    #Uncomment next line to export plot as .png
    #pplt.savefig("time_of_day_plot")


if __name__ == "__main__":
    main()