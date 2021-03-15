from flask import Flask
import folium
# from folium import folium, Map

app = Flask(__name__)
@app.route('/')


def index():
    global folium_map
    latitude = 1.00
    longitude = 36.00
    folium_map = folium.Map(location = [latitude, longitude], zoom_start = 10)
    # To return the folium's HTML representation
    return folium_map._repr_html_()


if __name__ == "__main__": app.run(debug = True)  


"""Paste this just before the single comment in line 13:
    ws = 'https://github.com/Jarvis2030'
    folium_map.add_child(folium.Marker(location=[latitude,longitude],
        popup="<b>Location : Kenya </b>" + "<br><b>GitHub link: </b><a href="+ws+">\
        Click here</a>",icon=folium.Icon(color='green')))
    folium_map.add_child('r',encoding='utf-8-sig').read()
"""
   