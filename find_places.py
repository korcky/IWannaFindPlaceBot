from googlemaps import places, geolocation, convert, Client
from telegram import  InlineQueryResultPhoto

import config

client = Client(key=config.API_KEY)


def find_places(user_location, user_radius):
    location = (user_location['latitude'], user_location['longitude'])
    result = places.places_nearby(client, location=location, radius=user_radius, type='restaurant') #keyword='cruise')
    #opening_hours = result['opening hours']
    #open_now = opening_hours['open now']

    result = result['results']
    for elements in result:
        if 'rating' not in elements:
            elements['rating'] = 0

    res = []
    for elements in sorted(result, key=lambda elements: elements['rating'], reverse=True):
        res.append(elements['name'] + ' ' + str(elements['rating']) + ' ' + elements['vicinity'])
    for i in res:
        print(i)

    return res
#res = find_places(client)

