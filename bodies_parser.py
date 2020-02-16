import json
print('"Name","Class","isScoopable","age","spectralClass","luminosity","absoluteMagnitude","solarMasses","solarRadius","surfaceTemperature"')
with open('bodies.json') as json_file:
    data = json.load(json_file)
    for p in data:
        if p['type']=="Star":
            ## We have a star!
            print(p['name'] +
                  "," + p['subType'] +
                  "," + str(p['isScoopable']) +
                  "," + str(p['age']) +
                  "," + p['spectralClass'] +
                  "," + p['luminosity'] +
                  "," + str(p['absoluteMagnitude']) +
                  "," + str(p['solarMasses']) +
                  "," + str(p['solarRadius']) +
                  "," + str(p['surfaceTemperature'])

            )