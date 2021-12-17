import json
from typing import Dict
from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

# file='/Users/vadim/Documents/Programming languages/Python/Python code/UW/python crash cource/chapter 16(downloading data)/data/eq_data_1_day_m1.json'
file='/Users/vadim/Documents/Programming languages/Python/Python code/UW/python crash cource/chapter 16(downloading data)/data/eq_data_30_day_m1.json'
with open(file) as f:
    load_json=json.load(f)

dict_data=load_json['features']
mags,lons,lats,hover_text=[],[],[],[]
for i in dict_data:
    mags.append(i['properties']['mag'])
    lons.append(i['geometry']['coordinates'][0])
    lats.append(i['geometry']['coordinates'][1])
    hover_text.append(i['properties']['title'])

data=[{
    'type':'scattergeo',
    'lon':lons,
    'lat':lats,
    'text':hover_text,
    'marker':{'size':[5*mag for mag in mags],
    'color':mags,
    'colorscale':'Viridis',
    'reversescale':True,
    'colorbar':{'title':'magnitude'}},
}]
my_layout=Layout(title='global earthquakes')

fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='global_earthquakes.html')

# print(f'{mags,lons,lats,hover_text}\n')