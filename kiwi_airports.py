from sys import argv
import requests
import json
_help = '''type in any of the fallowing command:
            --help - print help message
            --cities - cities with airports
            --coords - coordinates of each airport
            --iata - IATA codes
            --names - name of the airport
            --full - print every detail from each airport
'''
api = ('https://api.skypicker.com/locations?type=subentity&term=GB'
'&locale=en-US&location_types=airport&limit=60&sort=name')

data = json.loads(requests.get(api).content)

city = []
airport = []
iata = []
lat = []
lon = []
if '--help' in argv:
    print(_help)
else:
    for location in data['locations']:
        city.append(location['city']['name'])
        airport.append(location['name'])
        iata.append(location['code'])
        lon.append(location['location']['lon'])
        lat.append(location['location']['lat'])
    
    if len(argv) == 1:
        for i in range(len(city)):
            print(airport[i], city[i], iata[i], lat[i], lon[i])
    
    for command in argv[1:]:
        if command == '--cities':
            for i in range(len(city)):
                print(city[i], airport[i])
        elif command == '--coords':
            for i in range(len(city)):
                print(lat[i], lon[i])
        elif command == 'iata':
            for i in range(len(city)):
                print(iata[i])
        elif command == 'names':
            for i in range(len(city)):
                print(airport[i])
        elif command == '--full':
            for location in range(len(city)):
                for key, val in data['locations'][location].items():
                   print(key, '=', val)
