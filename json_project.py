import json

## open files
infile = open('US_fires_9_1.json','r')
outfile = open('readable_9_1.json','w')

## load json data
fire_data = json.load(infile)

## dump data
json.dump(fire_data, outfile, indent=4)

## create lists
brightness = []
lats = []
lons = []

## for loop
for fire in fire_data:
    bright = fire['brightness']
    lat = fire['latitude']
    lon = fire['longitude']
    if(bright > 450):
        brightness.append(bright)
        lats.append(lat)
        lons.append(lon)

## print("BRIGHTS:\n",brightness,"\nLATS:\n",lats,"\nLONS:\n",lons)

from plotly.graph_objects import Scattergeo, Layout
from plotly import offline

data = [{
    'type': 'scattergeo',
    'lon' : lons,
    'lat' : lats,
    'marker': {
        'size': 15,
        'color': brightness,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar' : {'title':'Brightness'},
    }
    
}]
myLayout = Layout(title="California Fires | 9/1-9/13")
fig = {'data':data, 'layout':myLayout}

offline.plot(fig, filename='calif_fires_9_1.html')
