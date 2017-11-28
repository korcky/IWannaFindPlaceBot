from googlemaps import places, Client
from telegram import Location

import config

client = Client(key=config.API_KEY)


def find_places(user_location, user_radius, place_type):
    if type(user_location) == Location:
        location = (user_location['latitude'], user_location['longitude'])
    else:
        location = user_location

    result = places.places_nearby(client, location=location,
                                  radius=user_radius, type=place_type, language='ru')['results']
    for place in result:
        if 'rating' not in place:
            place['rating'] = 0
        if 'opening_hours' not in place:
            place['is_open'] = 'No information'
        elif place['opening_hours']['open_now']:
            place['is_open'] = 'Is open now'
        else:
            place['is_open'] = 'Is closed now'

    return sorted(result, key=lambda item: item['rating'], reverse=True)
