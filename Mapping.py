import folium
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[38.2, -99.1], [38.3, -99.2]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a marker", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")
