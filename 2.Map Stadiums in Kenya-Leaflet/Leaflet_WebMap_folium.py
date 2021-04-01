import folium #A basic map where we ll render
import pandas as pd 
data = pd.read_csv()

map = folium.Map(location = [21.1458, 79.0882], zoom_start = 5)
# Create a featureGroup to handle multiple layers in a folium map
fg = folium.FeatureGroup('My Map')
# fg.add_child(folium.GeoJson(data = (open('indian_states.json','r', encoding='utf-8-sig').read())))
map.add_child(fg)
map.save('testmapi.html')

