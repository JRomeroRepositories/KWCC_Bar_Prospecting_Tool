import googlemaps
import pandas as pd
import time

API_KEY = open('API_KEY.txt', 'r').read()
map_client = googlemaps.Client(API_KEY)

## Rest_List_Gen(array[lat, long], radius, file)
##      Generates a list of restaurants within the radius of location input
##      The generated list is stored in file
##      Output list is: (name, address, status, phone number, type, hours, )
#Rest_List_Gen(
location = (43.48011918142259, -80.53160353205661) # Waterloo
radius = 10000 # 10km
business_list = []
#)
search_string = 'restaurant'

#business_list.extend(response.get('results'))
#next_page_token = response.get('next_page_token')
next_page_token = 1

while next_page_token:
    time.sleep(2)
    response = map_client.places_nearby(
        location = location,
        keyword = search_string,
        radius = radius,
        page_token = next_page_token
    )
    business_list.extend(response.get('results'))
    next_page_token = response.get('next_page_token')

df = pd.DataFrame(business_list)
df['url'] = 'www.google.com/maps/place/?q=place_id:' + df['place_id']

df.to_excel('Restaurant list.xlsx', index=False)
