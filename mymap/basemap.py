import folium
import pandas

data = pandas.read_csv("mymap/Volcanoes.txt")
lat =list(data["LAT"])
lon =list(data["LON"])

elev = list(data["ELEV"])

def color_pro(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'pink'
    else:
        return 'red'    

map = folium.Map(location=[48.7767982,-121.8109970], zoom_start=12, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
#    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el), icon=folium.Icon(color=color_pro(el))))
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 10, popup=str(el),
    fill_color=color_pro(el), color = 'grey',fill=True, fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Pop")

fgp.add_child(folium.GeoJson(data=open('mymap/world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'black'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("mymap/Map1.html")