import pandas as pd
import folium
from folium.plugins import MarkerCluster

data = pd.read_csv('listings-2.csv')
f_lat = data['latitude'][0]
f_lon = data['longitude'][0]
athens_map = folium.Map(location=[f_lat,f_lon],zoom_start = 13)
marker_cluster = MarkerCluster(name='Listings').add_to(athens_map)

for index, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        tooltip=row['name'],
    ).add_to(marker_cluster)

athens_map.save('athens_listings_map.html')

#i put this code in the ipynb file in the end
