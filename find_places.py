from googlemaps import places, geolocation, convert, Client
from telegram import message
import config

client = Client(key='AIzaSyDJF4uTFFAZY2ekqeONNJcFTkpE76L67es')

def find_places(user_location, user_radius):
    result = places.places_nearby(client, location=user_location, radius=user_radius, type='bar') #keyword='cruise')
    for elements in sorted(result['results'], key=lambda elements: elements['rating'], reverse=True):
           print(elements['name'], ' ', elements['rating'], ' ', elements['vicinity'], ' ') #elements['opening hours'])

#res = find_places(client)