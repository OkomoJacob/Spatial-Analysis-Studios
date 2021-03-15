import folium #A basic map where we ll render
import pandas as pd 
data = pd.read_csv('stadium.csv', encoding="cp1252")

# Exctracting each row from the data and aassigning it to a new list data for pop ups
LAT = list(data['LAT'])
LON = list(data['LON'])
name = list(data['NAME'])
capacity = list(data['capacity'])
website = list(data['website'])
picture = list(data['picture'])

fg = folium.FeatureGroup('My Map')
# Create a for loop to pop up the contents
    # fg.add_child(folium.Marker(location = [lt, ln], popup = "<b> Name: </b>" +nm+ "<br> <b> capacity : </b>"+ str(cp) + "<br><b>Wikipedia Link: </b><a href = "+ws+">click here</a>"))

for lt,ln,nm,cp,ws,pic in zip(LAT, LON,name,capacity,website,picture):

    fg.add_child(folium.Marker(location=[lt,ln],popup="<b>name  : </b>"+nm+ "<br> <b>capacity : </b> "+str(cp)+"<br><b>wikipidea link: </b><a href="+ws+">click here</a>"+"<br> <img src="+pic+" height=142 width=290>",icon=folium.Icon(color='green')))
fg.add_child(folium.GeoJson(data=(open('kenyan_stadiums.json','r',encoding='utf-8-sig').read())))

map = folium.Map(location = [0.0236, 37.9062], zoom_start = 6)
# Create a featureGroup to handle multiple layers in a folium map

fg.add_child(folium.GeoJson(data = (open('kenyan_stadiums.json','r', encoding='utf-8-sig').read())))
map.add_child(fg)
map.save('jaymap.html')

