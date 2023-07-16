import json
  
f = open('sample_UWS.geojson')
  
data = json.load(f)

for i in data['features']:
    print(i)
  
f.close()