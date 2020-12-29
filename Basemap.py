import folium
import pandas

data = pandas.read_excel("Volcanoes.xlsx", sheet_name=0, engine='openpyxl')
lat = list(data["Latitude"])
lon = list(data["Longitude"])
elev = list(data["Elevation"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=[40.747032397778284, -
                           73.988125863582], zoom_starts=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")


for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=5,
                                      popup=str(el) + " m", fill_color=color_producer(el), color='gray', fill_opacity=0.9))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'pink' if x['properties']['POP2005'] < 10000000
                                                       else 'yellow' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Basemap1.html")
