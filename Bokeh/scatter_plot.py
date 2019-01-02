""" 
Program for scatter plotting using bokeh
	by Aniruddha
"""

from bokeh.plotting import figure,output_file,show
import pandas as pd
from math import sin,radians

df = pd.DataFrame(columns=["x","sin x"])

for i in range(0,361,5):
	df = df.append({"x":i,"sin x":sin(radians(i))},ignore_index=True)

p=figure(plot_width = 1200, plot_height = 750,tools='pan,wheel_zoom,box_zoom,save,reset',logo = None)

p.title.text = "Graph for sine"
p.title.text_color = "Orange"
p.title.text_font = 'helvetica'
p.title.text_font_size = '50pt'
p.title.text_font_style='italic'
p.title.vertical_align = 'top'
p.title.align = 'center'
p.toolbar_location = "above"
p.xaxis.axis_label = "Angle(x) in degrees ----->"
p.yaxis.axis_label = "Sin x ----->"
p.xaxis.axis_label_text_font_size = "20pt"
p.yaxis.axis_label_text_font_size = "20pt"




p.circle(df["x"],df["sin x"],size = [abs(i)*20 for i in df["sin x"]], color = 'red',alpha=0.5)
	

output_file("Sine Chart.html")
show(p)


