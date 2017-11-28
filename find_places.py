from googlemaps import places, geolocation, convert, Client
from telegram import  InlineQueryResultPhoto

import config

client = Client(key=config.API_KEY)


def find_places(user_location, user_radius):
    location = (user_location['latitude'], user_location['longitude'])
    result = places.places_nearby(client, location=location, radius=user_radius, type='bar') #keyword='cruise')
    #opening_hours = result['opening hours']
    #open_now = opening_hours['open now']

    result = result['results']
    for elements in result:
        if 'rating' not in elements:
            elements['rating'] = 0
        if 'opening_hours' not in elements:
            elements['is_open'] = 'No information.'
        elif (elements['opening_hours']['open_now'] == True):
            elements['is_open'] = 'Is open now.'
        elif (elements['opening_hours']['open_now'] == False):
            elements['is_open'] = 'Is closed now.'

    res = []
    i = 1
    for elements in sorted(result, key=lambda elements: elements['rating'], reverse=True):
        #print(elements['is_open'])
        #res.append(elements['name'] + ' ' + str(elements['rating']) + ' ' + elements['vicinity'])
        res.append('{}. {}\nRating: {}\nAddress: {}\nOpening hours: {}\n'.format(i, elements['name'], elements['rating'],
                                                              elements['vicinity'], elements['is_open']))
        i = i+1

    for i in res:
        print(i)

    return res
#res = find_places(client)

