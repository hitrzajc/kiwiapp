from sys import argv
import requests
import json

halp = """type in any of the fallowing command:
            --help - print help message
            --cities - cities with airports
            --coords - coordinates of each airport
            --iata - IATA codes
            --names - name of the airport
            --full - print every detail from each airport
"""
api = "https://api.skypicker.com/locations?type=subentity&term=GB&locale=en-US&location_types=airport&limit=60&sort=name"
data = json.loads(requests.get(api).content)

city=[]
airport=[]
iata=[]
location=[]
if '--help' in argv:
    print(halp)
else:
    for i in data['locations']:
        city.append(i['city']['name'])
        airport.append(i['name'])
        iata.append(i['code'])
        location.append([[i['location']['lat'],i['location']['lon']]])

    if len(argv) == 1:
        for i in range(len(city)):
            print(airport[i],city[i],iata[i],location[i])
    else:
        for command in range(1, len(argv)): 
            if command == '--cities':
                for i in range(len(city)):
                    print(city[i],airport[i])      
            elif command == '--coords':
                for i in range(len(city)):
                    print(location[i][0],location[i][1])   
            elif command == 'iata':
                for i in range(len(city)):
                    print(iata[i])      
            elif command == 'names':
                for i in range(len(city)):
                    print(airport[i])        
            elif command == '--full':
                print(data['locations'])





