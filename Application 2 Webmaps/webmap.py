""" 
Program to make a webpage containing webmaps 
with volcanoes and population distribution
	by Aniruddha

"""

import folium
import pandas
import numpy


#loading data about volcanoes
data = pandas.read_excel("Volcanoes.xlsx")
data = data.replace(numpy.nan, '', regex=True)

lat 	= list(data["Latitude (dd)"])
lon 	= list(data["Longitude (dd)"])
elev 	= list(data["Elevation (m)"])
country = list(data["Country"])
Type 	= list(data["Type"])

#details=["Country : "+row["Country"]+"<br>Type : "+row["Type"]+
#	"<br>Elevation : "+str(row["Elevation (m)"])
#	+" m" for index,row in data.iterrows()]



#use these to create selection dictionary
#	v_type=data.Type.unique() #to generate unique list of type of volcanoes
#	v_color = ['#d9bfff','#ccff00','#e6acac','#4c3300','#2b3326',
#		'#2a2633','#002e73','#73cfe6','#d900ca','#00ffcc',
#		'#4073ff', '#b23000','#8c233f','#e5b800','#138c00']
#	selection = dict(zip(v_type,v_color))
#	print(selection)
selection = {
		'': '#d9bfff', 'Dome ': ' #ccff00', 
		'Shield ': '#e6acac', 'Volcanic Field ': '#4c3300', 
		'Plug ': '#2b3326', 'Fissure vents ': '#2a2633', 
		'Submarine ': ' #002e73', 'Somma Volcano ': '#73cfe6', 
		'Maar ': '#d900ca', 'Cinder Cone ': ' #00ffcc', 
		'Pyroclastic Cone ': ' #4073ff', 'Complex Volcano ': '#b23000', 
		'Tuff Ring ': '#8c233f', 'Stratovolcano ': '#e5b800', 
		'Caldera ': '#138c00'}

#method to return a colour based on type of volcanoes
def clr(type):
	return selection[type]




#creating map layers
map = folium.Map(
		location=[21,17], 
		height = "90%",
		zoom_start = 2 ,
		 min_zoom= 2, control_scale = True,
		tiles = "Mapbox Control Room")		#night view
folium.TileLayer(
		 min_zoom= 2, 
		tiles = "http://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", 
		attr="Google Maps").add_to(map)		#satellite view
folium.TileLayer(
		 min_zoom= 2, 
		tiles = "Mapbox Bright").add_to(map)	#normal view(default)



#Creating features groups
fgv = folium.FeatureGroup(name = "Volcanoes")
fgp = folium.FeatureGroup(name = "Population")


#adding volcano points to volcano feature group
for lt,ln,cn,tp,el in zip(lat,lon,country,Type,elev):
	fgv.add_child(
		folium.CircleMarker(
			location=[lt,ln],
			popup = folium.Popup(
				"Country : "+str(cn)+
				"<br>Type : "+str(tp)+
				"<br>Elevation : "+str(el)+" m") ,
			fill=True,
			fill_opacity=0.7,
			radius = 6,
			color="gray",
			fill_color=clr(tp)))
			
			
#for lt,ln,det,tp in zip(lat,lon,details,Type):
#	fg.add_child(
#		folium.CircleMarker(
#			location=[lt,ln],
#			popup = folium.Popup(det),
#			fill=True,
#			fill_opacity=0.7,
#			radius = 6,
#			color="gray",
#			fill_color=clr(tp)))
#		


#adding GeoJson to population feature group
fgp.add_child(
	folium.GeoJson(
		data=open ('world.json',encoding='utf-8-sig').read(),
		style_function = lambda x: {'weight':1,'smooth_factor':0.7,
			'fillColor': '#FFFFFF' if x['properties']['POP2005'] <10 
				else '#FFFF00' if  10<= x['properties']['POP2005'] <10000000
				else '#FFD700' if  10000000<= x['properties']['POP2005'] <30000000
				else '#FFA500' if  30000000<= x['properties']['POP2005'] <60000000
				else '#FF4500' if  60000000<= x['properties']['POP2005'] <100000000
				else '#FF0000' if  100000000<= x['properties']['POP2005'] <200000000
				else '#B22222' if  200000000<= x['properties']['POP2005'] <1000000000
				else '#8B0000'
				}
		))



#adding both feature group to map
map.add_child(fgp)
map.add_child(fgv)


#adding layer control
map.add_child(folium.LayerControl())



#creating legend for population
pop_legend_html = '''
        <div style="position:fixed; bottom:35px; left:20px; width:160px; height:210px; border:2px solid grey; z-index:9998; font-size:14px;background:#F3F9FB7F">
        	<center>Population(in Millions)</center><br>
            &nbsp;<span style="padding-left:30px;background:#FFFFFF;"></span>&nbsp;&nbsp;Zero Population<br>
            &nbsp;<span style="padding-left:30px;background:#FFFF00;"></span>&nbsp;&nbsp;<10<br>
            &nbsp;<span style="padding-left:30px;background:#FFD700;"></span>&nbsp;&nbsp;10-30<br>
            &nbsp;<span style="padding-left:30px;background:#FFA500;"></span>&nbsp;&nbsp;30-60<br>
            &nbsp;<span style="padding-left:30px;background:#FF4500;"></span>&nbsp;&nbsp;60-100<br>
            &nbsp;<span style="padding-left:30px;background:#FF0000;"></span>&nbsp;&nbsp;100-200<br>
            &nbsp;<span style="padding-left:30px;background:#B22222;"></span>&nbsp;&nbsp;>200-1000<br>
            &nbsp;<span style="padding-left:30px;background:#8B0000;"></span>&nbsp;&nbsp;>1000<br>
        </div>'''

     		
#creating legend for volcanoes
vol_legend_html = '''
        <div style="position:fixed; bottom:35px; right:17px; width:160px; height:355px; border:2px solid grey; z-index:9998; font-size:14px;background:#F3F9FB7F">
    	<center>Volcanoes</center><br>
    	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#e6acac;"></i>&nbsp;&nbsp;Shield <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#e5b800;"></i>&nbsp;&nbsp;Stratovolcano <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#138c00;"></i>&nbsp;&nbsp;Caldera <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#002e73;"></i>&nbsp;&nbsp;Submarine <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#b23000;"></i>&nbsp;&nbsp;Complex Volcano <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#ccff00;"></i>&nbsp;&nbsp;Dome <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#00ffcc;"></i>&nbsp;&nbsp;Cinder Cone <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#4073ff;"></i>&nbsp;&nbsp;Pyroclastic Cone <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#d900ca;"></i>&nbsp;&nbsp;Maar <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#4c3300;"></i>&nbsp;&nbsp;Volcanic Field <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#2b3326;"></i>&nbsp;&nbsp;Plug <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#73cfe6;"></i>&nbsp;&nbsp;Somma Volcano <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#2a2633;"></i>&nbsp;&nbsp;Fissure vents <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#8c233f;"></i>&nbsp;&nbsp;Tuff Ring <br>
	&nbsp;&nbsp;<i class="fa fa-circle"style="color:#d9bfff;"></i>&nbsp;&nbsp;Unknown<br>
        </div>'''

     		


#creating header and adding both legends and map
fig = folium.Figure()
fig.html.add_child(folium.Element("<h3><center>Map showing Volcanoes and Population areas <br>-- by <a href =\"https://anianiruddha.wordpress.com\">Aniruddha &nbsp;<i class=\"fa fa-external-link\"></i></a></center></h3>"))
fig.html.add_child(folium.Element(pop_legend_html))
fig.html.add_child(folium.Element(vol_legend_html))
fig.add_child(map)


#saving webpage
fig.save("Home.html")
