import json

infile = open("US_fires_9_1.json", "r")
outfile = open("readable_fires_9_1.json", "w")

# json.load converted data into a formate python
# can work with (a giant dictionary)

fire_data = json.load(infile)

json.dump(fire_data, outfile, indent=4)

list_of_fires = fire_data

brights = []
lons = []
lats = []

for fire in list_of_fires:
    brightness = fire["brightness"]
    lon = fire["longitude"]
    lat = fire["latitude"]
    if brightness > 450:
        brights.append(brightness)
        lons.append(lon)
        lats.append(lat)

# print(brights[:10])
# print(lons[:10])
# print(lats[:10])


from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [0.02 * brightness for brightness in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]
Scattergeo(lon=lons, lat=lats)  # taking scatterplots and putting on a map

my_layout = Layout(title="Prominent US Fires")  # give layout for ^

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="us_fires.html")


"""
data = [Scattergeo(lon=lons, lat=lats)]  # taking scatterplots and putting on a map

my_layout = Layout(title="Global Fires")  # give layout for ^

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="global_fires.html")
"""
