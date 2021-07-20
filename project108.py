import csv
import plotly.figure_factory as ff
import pandas as pd
file = pd.read_csv("project108.csv")
fig = ff.create_distplot([file["Avg Rating"].tolist()], ["Average Mobile Brand Rating"], show_hist = False)
fig.show()