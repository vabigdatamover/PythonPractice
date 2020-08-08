import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

map.add_child(folium.Marker())

map.save("Map2.html")
