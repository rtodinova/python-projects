import folium
import pandas

map = folium.Map(location=[42.7339, 25.4858], zoom_start=7)
markers = folium.FeatureGroup("Markers")

html_volcanoes_marker = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

volcanoes_data = pandas.read_csv("Volcanoes.csv")
volcanoes_coordinate_latitudes = list(volcanoes_data["x"])
volcanoes_coordinate_longtitudes = list(volcanoes_data["y"])
elevations = list(volcanoes_data['ELEV'])
names = list(volcanoes_data['NAME'])

def color_of_marker(elevation):
    if elevation <= 1000:
        return 'green'
    elif 1000 < elevation < 3000:
        return 'yellow'
    else:
        return 'red'

for latitude, longtitude, elevation, name in zip(volcanoes_coordinate_latitudes, volcanoes_coordinate_longtitudes, elevations, names):
    iframe = folium.IFrame(html=html_volcanoes_marker % (name, name, elevation), width=200, height=100)
    markers.add_child(folium.CircleMarker(location=[latitude, longtitude], popup=folium.Popup(iframe),
    fill_color=color_of_marker(elevation), fill_opacity=0.7))

population_feature_group = folium.FeatureGroup(name="Population")
population = folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x:{'fillColor' : 'green' if x['properties']['POP2005'] < 10000000 else 'yellow' if x['properties']['POP2005'] < 20000000 else 'red'})
population_feature_group.add_child(population)

map.add_child(markers)
map.add_child(population_feature_group)
map.add_child(folium.LayerControl())

map.save("webmap.html")
