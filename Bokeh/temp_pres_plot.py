from bokeh.plotting import figure,output_file,show
import pandas as pd

df = pd.read_excel("http://pythonhow.com/verlegenhuken.xlsx")
#print(df)

p=figure(plot_width = 1000, plot_height = 750,tools='pan,save,reset',logo = None)

p.scatter(df["Temperature"]/10,df["Pressure"]/10)


p.title.text = "Temperature & Air Pressure"
p.title.text_color = "Red"
p.title.text_font = 'helvetica'
p.title.text_font_size = '50pt'
p.title.text_font_style='italic'
p.title.vertical_align = 'top'
p.title.align = 'center'
p.toolbar_location = "above"
p.xaxis.axis_label = "Temperature(°C) ----->"
p.yaxis.axis_label = "Pressure(hPa) ----->"
p.xaxis.axis_label_text_font_size = "20pt"
p.yaxis.axis_label_text_font_size = "20pt"

show(p)

