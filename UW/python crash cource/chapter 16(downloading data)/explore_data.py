import json

file='/Users/vadim/Documents/Programming languages/Python/Python code/UW/python crash cource/chapter 16(downloading data)/data/eq_data_1_day_m1.json'
with open(file) as f:
    load_json=json.load(f)

dict_data=load_json['features']
mags,lons,lats=[],[],[]
# print(len(dict_data))
for i in dict_data:
    mag=i['properties']['mag']
    lon=i['geometry']['coordinates'][0]
    lat=i['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
print(mags[:10])
print(lons[:5])
print(lats[:5])

