import json, math
print('"id","name","distance"')
with open('topsystems.json') as json_file:
    data = json.load(json_file)
    for p in data:
        c = p['coords']
        dist = math.sqrt(c['x']**2 + c['x']**2 + c['x']**2)
        print(
            str(p['id']) + ',' +  p['name'] + "," + str(dist)
        )