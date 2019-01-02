""" 
Program for time series graph using bokeh
	by Aniruddha
"""
from bokeh.plotting import figure,output_file,show
import pandas as pd
from bokeh.models.formatters import DatetimeTickFormatter

df = pd.read_excel("JanTemp.xlsx")

p=figure(x_axis_type = "datetime",sizing_mode='stretch_both',tools='pan,box_zoom,save,reset',logo = None)

p.title.text="January 2018 Temperature in Kolkata"

p.xaxis.axis_label = "Date ----->"
p.yaxis.axis_label = "Temperature(°C) ----->"

p.line(df["Date"],df["Temp"],color='Gray',line_width = 3)
p.circle(df["Date"],df["Temp"],color='Blue',fill_color = "White",size=[i/2 for i in df["Temp"]])
p.xaxis.formatter = DatetimeTickFormatter(days = ["%e %b '%y"])
show(p)

