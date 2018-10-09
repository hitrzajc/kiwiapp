import sys
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

if '--help' in sys.argv:
    print(_help)
else:
    try:
        response = requests.get(api)
        response.raise_for_status()
        data = json.loads(response.content)
    except(requests.exceptions.HTTPError, ValueError) as error:
        print('Something went wrong:', error)
        sys.exit(1)
    
    for location in data['locations']:
        city = location['city']['name']
        airport = location['name']
        iata = location['code']
        lon = location['location']['lon']
        lat = location['location']['lat']
    
        for command in sys.argv[1:]:
            if command == '--cities':
                print(city, airport)
            elif command == '--coords':
                print(lat, lon)
            elif command == 'iata':
                print(iata)
            elif command == 'names':
                print(airport)
            elif command == '--full':
                for key, val in location.items():
                    print(key, '=', val)
        else:
            print(airport, city, iata, lat, lon)
