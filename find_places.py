from googlemaps import places, geolocation, convert, Client

import config

client = Client(key=config.API_KEY)


def find_places(user_location, user_radius):
    location = (user_location['latitude'], user_location['longitude'])
    result = places.places_nearby(client, location=location, radius=user_radius, type='bar') #keyword='cruise')
    for elements in sorted(result['results'], key=lambda elements: elements['rating'], reverse=True):
           print(elements['name'], ' ', elements['rating'], ' ', elements['vicinity'], ' ') #elements['opening hours'])

#res = find_places(client)