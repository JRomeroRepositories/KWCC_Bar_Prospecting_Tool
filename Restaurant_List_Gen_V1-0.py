import time
import googlemaps # pip install googlemaps
import pandas as pd # pip install pandas
import re

## Google API Key is unique to all google API platform users, and is used in
##  reference to the GCP account and billing
API_KEY = 'KEY NEEDED'
map_client = googlemaps.Client(API_KEY)

## List of search queries, inteded to encompass all terms that may be used to reference a particular
##  restaurant or bar.
search_strings = ['bar', 'restaurant', 'pub', 'nightclub', 'tavern', 'bistro', 'cafe',
                  'eatery', 'lounge', 'public house', 'drinkery', 'taphouse', 'grill', 
                  'brewery', 'beer', 'alehouse', 'establishment'] ## list of search queries

radius = 3 * 1000 # Radius in km
business_list = []


## Main Data-building loop.
for search_string in search_strings:
    response = map_client.places_nearby(
        location=(43.65162067487806, -79.47599887066528), ## Set to Runnymede station in Toronto
        keyword=search_string,
        radius=radius,
        min_price=1,
        max_price=4
    )
    ## Building the data by appending all attributes with some relevance to alcoholic beverage sales
    for place in response['results']:
        place_details = map_client.place(
            place_id=place['place_id'],
            fields=['name', 
                    'formatted_address', 
                    'formatted_phone_number',
                    'opening_hours',
                    'business_status',
                    'price_level',
                    'reservable', 
                    'delivery', 
                    'dine_in', 
                    'curbside_pickup', 
                    'url',
                    'website',
                    'serves_beer', 
                    'serves_wine',
                    'rating', 
                    'user_ratings_total',
                    'reviews']
        )
        if place_details['result']['business_status'] == 'OPERATIONAL': ## No filtering by serves_beer
            business_list.append(place_details['result'])
        ## Below it the optional 'serves_beer' filter
        if 'serves_beer' in place_details['result']: ## Filter by serves_beer and operational
           if place_details['result']['serves_beer'] == True and place_details['result']['business_status'] == 'OPERATIONAL':
               business_list.append(place_details['result'])

## Extract top 3 reviews and put them into separate columns
def extract_reviews(reviews):
    if isinstance(reviews, float): # Addresses the float issue
        return ['', '', '']
    review_texts = []
    for review in reviews[:3]:
        review_texts.append(review['text'])
    while len(review_texts) < 3:
        review_texts.append('')
    return review_texts

## Extract weekday_text from opening hours and concatenate into one column
def extract_weekday_text(opening_hours):
    if not isinstance(opening_hours, dict) or 'weekday_text' not in opening_hours: # Addresses the float issue
        return ''
    return '|'.join(opening_hours['weekday_text'])

## Extract postal code from the 'formatted_address' attribute
def extract_postal_code(address):
    for component in address.split(','):
        component = component.strip()
        match = re.search(r'\b[A-Z][0-9][A-Z] [0-9][A-Z][0-9]\b', component)
        if match:
            return match.group()
    return ''                

df = pd.DataFrame(business_list)
if df.empty:
    print('No Search Results Error')
else:
    df = df.drop_duplicates(subset=['name', 'formatted_address'])  ## Remove duplicate rows based on name and address
    df['postal_code'] = df['formatted_address'].apply(lambda x: extract_postal_code(x) if x else '')
    df[['review_1', 'review_2', 'review_3']] = df['reviews'].apply(lambda x: pd.Series(extract_reviews(x)))
    df['weekday_text'] = df['opening_hours'].apply(lambda x: extract_weekday_text(x) if x else '')
    df = df.drop(columns=['reviews', 'opening_hours'])
    df.to_excel('EXCEL_TITLE HERE.xlsx', index=False)